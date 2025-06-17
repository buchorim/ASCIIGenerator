#!/usr/bin/env python3
"""
Advanced Video to ASCII Art Converter
Converts videos to high-quality ASCII art with depth and customization options.
Optimized for low-end devices with CLI interface.
"""

import cv2
import numpy as np
import argparse
import os
import sys
import time
import threading
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List, Optional
import json
import shutil

class VideoASCIIConverter:
    def __init__(self):
        # ASCII character sets for different quality levels
        self.ascii_chars = {
            'simple': ' .:-=+*#%@',
            'standard': ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$',
            'detailed': ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$',
            'gradient': ' ░▒▓█',
            'blocks': ' ▁▂▃▄▅▆▇█'
        }
        
        # Color modes
        self.color_modes = ['grayscale', 'color', 'ansi']
        
        # Default settings
        self.settings = {
            'width': 80,
            'height': 24,
            'fps': 10,
            'char_set': 'standard',
            'color_mode': 'grayscale',
            'contrast': 1.0,
            'brightness': 0.0,
            'gamma': 1.0,
            'invert': False,
            'edge_detection': False,
            'depth_effect': False,
            'blur': 0,
            'quality': 'medium'
        }

    def load_video(self, video_path: str) -> cv2.VideoCapture:
        """Load video file and return VideoCapture object"""
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {video_path}")
        
        return cap

    def apply_image_effects(self, frame: np.ndarray) -> np.ndarray:
        """Apply various image effects to enhance ASCII conversion"""
        # Convert to float for processing
        frame = frame.astype(np.float32) / 255.0
        
        # Brightness adjustment
        if self.settings['brightness'] != 0:
            frame = np.clip(frame + self.settings['brightness'], 0, 1)
        
        # Contrast adjustment
        if self.settings['contrast'] != 1.0:
            frame = np.clip((frame - 0.5) * self.settings['contrast'] + 0.5, 0, 1)
        
        # Gamma correction
        if self.settings['gamma'] != 1.0:
            frame = np.power(frame, 1.0 / self.settings['gamma'])
        
        # Convert back to uint8
        frame = (frame * 255).astype(np.uint8)
        
        # Blur effect
        if self.settings['blur'] > 0:
            kernel_size = max(1, int(self.settings['blur'] * 5))
            if kernel_size % 2 == 0:
                kernel_size += 1
            frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
        
        # Edge detection
        if self.settings['edge_detection']:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame
            edges = cv2.Canny(gray, 50, 150)
            frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) if len(frame.shape) == 3 else edges
        
        # Invert colors
        if self.settings['invert']:
            frame = 255 - frame
        
        return frame

    def create_depth_map(self, frame: np.ndarray) -> np.ndarray:
        """Create a simple depth map for depth effect"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame
        
        # Simple depth estimation using blur difference
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        depth = cv2.absdiff(gray, blurred)
        
        # Normalize depth map
        depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
        
        return depth

    def frame_to_ascii(self, frame: np.ndarray) -> str:
        """Convert a single frame to ASCII art"""
        # Apply effects
        frame = self.apply_image_effects(frame)
        
        # Resize frame to target dimensions
        if len(frame.shape) == 3:
            height, width = frame.shape[:2]
        else:
            height, width = frame.shape
        
        aspect_ratio = width / height
        new_width = self.settings['width']
        new_height = int(new_width / aspect_ratio * 0.5)  # Adjust for character aspect ratio
        
        if self.settings['height'] > 0:
            new_height = min(new_height, self.settings['height'])
        
        frame = cv2.resize(frame, (new_width, new_height))
        
        # Convert to grayscale for ASCII conversion
        if len(frame.shape) == 3:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            gray_frame = frame
        
        # Apply depth effect if enabled
        if self.settings['depth_effect']:
            depth_map = self.create_depth_map(frame)
            depth_map = cv2.resize(depth_map, (new_width, new_height))
            # Combine intensity with depth for character selection
            gray_frame = (gray_frame * 0.7 + depth_map * 0.3).astype(np.uint8)
        
        # Get ASCII character set
        chars = self.ascii_chars[self.settings['char_set']]
        
        # Convert pixels to ASCII
        ascii_lines = []
        for y in range(new_height):
            line = ""
            for x in range(new_width):
                pixel_value = gray_frame[y, x]
                char_index = int(pixel_value * (len(chars) - 1) / 255)
                line += chars[char_index]
            ascii_lines.append(line)
        
        return '\n'.join(ascii_lines)

    def convert_to_txt(self, video_path: str, output_path: str):
        """Convert video to text file with ASCII frames"""
        cap = self.load_video(video_path)
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Calculate frame skip for target FPS
        frame_skip = max(1, int(original_fps / self.settings['fps']))
        
        frames_to_process = total_frames // frame_skip
        
        print(f"Converting video to ASCII text...")
        print(f"Total frames to process: {frames_to_process}")
        print(f"Target FPS: {self.settings['fps']}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            frame_count = 0
            processed_frames = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                if frame_count % frame_skip == 0:
                    ascii_frame = self.frame_to_ascii(frame)
                    f.write(f"Frame {processed_frames + 1}:\n")
                    f.write(ascii_frame)
                    f.write("\n" + "="*80 + "\n\n")
                    
                    processed_frames += 1
                    if processed_frames % 10 == 0:
                        progress = (processed_frames / frames_to_process) * 100
                        print(f"Progress: {progress:.1f}%")
                
                frame_count += 1
        
        cap.release()
        print(f"ASCII text saved to: {output_path}")

    def convert_to_gif(self, video_path: str, output_path: str):
        """Convert video to animated GIF with ASCII frames"""
        cap = self.load_video(video_path)
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Calculate frame skip for target FPS
        frame_skip = max(1, int(original_fps / self.settings['fps']))
        
        frames_to_process = total_frames // frame_skip
        
        print(f"Converting video to ASCII GIF...")
        print(f"Total frames to process: {frames_to_process}")
        
        # Create PIL images for GIF
        pil_images = []
        frame_count = 0
        processed_frames = 0
        
        # Try to use a monospace font
        try:
            font = ImageFont.truetype("DejaVuSansMono.ttf", 8)
        except:
            try:
                font = ImageFont.truetype("Courier.ttf", 8)
            except:
                font = ImageFont.load_default()
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % frame_skip == 0:
                ascii_frame = self.frame_to_ascii(frame)
                
                # Create PIL image from ASCII text
                lines = ascii_frame.split('\n')
                char_width = 6
                char_height = 12
                img_width = len(lines[0]) * char_width if lines else 480
                img_height = len(lines) * char_height
                
                img = Image.new('RGB', (img_width, img_height), color='black')
                draw = ImageDraw.Draw(img)
                
                for i, line in enumerate(lines):
                    draw.text((0, i * char_height), line, fill='white', font=font)
                
                pil_images.append(img)
                processed_frames += 1
                
                if processed_frames % 10 == 0:
                    progress = (processed_frames / frames_to_process) * 100
                    print(f"Progress: {progress:.1f}%")
            
            frame_count += 1
        
        cap.release()
        
        if pil_images:
            # Calculate duration per frame in milliseconds
            duration = int(1000 / self.settings['fps'])
            
            # Save as GIF
            pil_images[0].save(
                output_path,
                save_all=True,
                append_images=pil_images[1:],
                duration=duration,
                loop=0
            )
            print(f"ASCII GIF saved to: {output_path}")
        else:
            print("No frames were processed!")

    def convert_to_mp4(self, video_path: str, output_path: str):
        """Convert video to MP4 with ASCII frames"""
        cap = self.load_video(video_path)
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Calculate frame skip for target FPS
        frame_skip = max(1, int(original_fps / self.settings['fps']))
        
        frames_to_process = total_frames // frame_skip
        
        print(f"Converting video to ASCII MP4...")
        print(f"Total frames to process: {frames_to_process}")
        
        # Get first frame to determine output dimensions
        ret, first_frame = cap.read()
        if not ret:
            print("Could not read first frame!")
            return
        
        ascii_frame = self.frame_to_ascii(first_frame)
        lines = ascii_frame.split('\n')
        
        # Calculate output video dimensions
        char_width = 8
        char_height = 16
        output_width = len(lines[0]) * char_width if lines else 640
        output_height = len(lines) * char_height
        
        # Make dimensions even (required for some codecs)
        output_width = output_width + (output_width % 2)
        output_height = output_height + (output_height % 2)
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.settings['fps'], (output_width, output_height))
        
        # Reset video capture
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        frame_count = 0
        processed_frames = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % frame_skip == 0:
                ascii_frame = self.frame_to_ascii(frame)
                
                # Create image from ASCII text
                img = np.zeros((output_height, output_width, 3), dtype=np.uint8)
                lines = ascii_frame.split('\n')
                
                for i, line in enumerate(lines):
                    y_pos = i * char_height
                    if y_pos + char_height < output_height:
                        for j, char in enumerate(line):
                            x_pos = j * char_width
                            if x_pos + char_width < output_width:
                                # Simple character rendering (could be improved)
                                if char != ' ':
                                    cv2.rectangle(img, (x_pos, y_pos), 
                                                (x_pos + char_width, y_pos + char_height), 
                                                (255, 255, 255), -1)
                
                out.write(img)
                processed_frames += 1
                
                if processed_frames % 10 == 0:
                    progress = (processed_frames / frames_to_process) * 100
                    print(f"Progress: {progress:.1f}%")
            
            frame_count += 1
        
        cap.release()
        out.release()
        print(f"ASCII MP4 saved to: {output_path}")

    def save_config(self, config_path: str):
        """Save current settings to JSON file"""
        with open(config_path, 'w') as f:
            json.dump(self.settings, f, indent=2)
        print(f"Configuration saved to: {config_path}")

    def load_config(self, config_path: str):
        """Load settings from JSON file"""
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                loaded_settings = json.load(f)
                self.settings.update(loaded_settings)
            print(f"Configuration loaded from: {config_path}")
        else:
            print(f"Configuration file not found: {config_path}")

def main():
    parser = argparse.ArgumentParser(description="Advanced Video to ASCII Art Converter")
    parser.add_argument("input", help="Input video file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-f", "--format", choices=['txt', 'gif', 'mp4'], default='txt',
                        help="Output format (default: txt)")
    
    # Dimension settings
    parser.add_argument("-w", "--width", type=int, default=80, help="ASCII width (default: 80)")
    parser.add_argument("-h", "--height", type=int, default=24, help="ASCII height (default: 24)")
    
    # Quality settings
    parser.add_argument("--fps", type=float, default=10, help="Target FPS (default: 10)")
    parser.add_argument("--char-set", choices=['simple', 'standard', 'detailed', 'gradient', 'blocks'],
                        default='standard', help="ASCII character set (default: standard)")
    parser.add_argument("--quality", choices=['low', 'medium', 'high'], default='medium',
                        help="Processing quality (default: medium)")
    
    # Image effects
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast adjustment (default: 1.0)")
    parser.add_argument("--brightness", type=float, default=0.0, help="Brightness adjustment (default: 0.0)")
    parser.add_argument("--gamma", type=float, default=1.0, help="Gamma correction (default: 1.0)")
    parser.add_argument("--blur", type=float, default=0.0, help="Blur effect (0.0-1.0, default: 0.0)")
    parser.add_argument("--invert", action='store_true', help="Invert colors")
    parser.add_argument("--edge-detection", action='store_true', help="Enable edge detection")
    parser.add_argument("--depth-effect", action='store_true', help="Enable depth effect")
    
    # Configuration
    parser.add_argument("--save-config", help="Save current settings to config file")
    parser.add_argument("--load-config", help="Load settings from config file")
    parser.add_argument("--preview", action='store_true', help="Show preview of first frame only")
    
    args = parser.parse_args()
    
    # Create converter instance
    converter = VideoASCIIConverter()
    
    # Load configuration if specified
    if args.load_config:
        converter.load_config(args.load_config)
    
    # Update settings from command line arguments
    converter.settings.update({
        'width': args.width,
        'height': args.height,
        'fps': args.fps,
        'char_set': args.char_set,
        'quality': args.quality,
        'contrast': args.contrast,
        'brightness': args.brightness,
        'gamma': args.gamma,
        'blur': args.blur,
        'invert': args.invert,
        'edge_detection': args.edge_detection,
        'depth_effect': args.depth_effect
    })
    
    # Save configuration if specified
    if args.save_config:
        converter.save_config(args.save_config)
    
    # Preview mode
    if args.preview:
        cap = converter.load_video(args.input)
        ret, frame = cap.read()
        if ret:
            ascii_frame = converter.frame_to_ascii(frame)
            print("Preview of first frame:")
            print("=" * 80)
            print(ascii_frame)
            print("=" * 80)
        cap.release()
        return
    
    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found!")
        sys.exit(1)
    
    # Convert video based on format
    try:
        start_time = time.time()
        
        if args.format == 'txt':
            converter.convert_to_txt(args.input, args.output)
        elif args.format == 'gif':
            converter.convert_to_gif(args.input, args.output)
        elif args.format == 'mp4':
            converter.convert_to_mp4(args.input, args.output)
        
        end_time = time.time()
        print(f"Conversion completed in {end_time - start_time:.2f} seconds")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

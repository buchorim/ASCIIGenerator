# Examples and Use Cases

This document provides comprehensive examples of using the Video ASCII Art Converter for different scenarios and creative effects.

## 📋 Table of Contents

- [Basic Usage](#basic-usage)
- [Creative Effects](#creative-effects)
- [Performance Optimization](#performance-optimization)
- [Batch Processing](#batch-processing)
- [Configuration Management](#configuration-management)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)

## 🚀 Basic Usage

### Simple Text Conversion

```bash
# Convert a video to ASCII text file
python video_ascii.py input.mp4 -o output.txt

# Specify custom dimensions
python video_ascii.py input.mp4 -o output.txt -w 100 --height 30

# Change frame rate
python video_ascii.py input.mp4 -o output.txt --fps 5
```

### Creating Animated GIFs

```bash
# Basic GIF conversion
python video_ascii.py clip.mp4 -o animation.gif -f gif

# High-quality GIF with custom settings
python video_ascii.py clip.mp4 -o hq_animation.gif -f gif \
  -w 150 --fps 20 --char-set detailed

# Compact GIF for sharing
python video_ascii.py clip.mp4 -o compact.gif -f gif \
  -w 80 --fps 10 --quality low
```

### ASCII Video (MP4) Output

```bash
# Create ASCII video
python video_ascii.py input.mp4 -o ascii_video.mp4 -f mp4

# Custom resolution ASCII video
python video_ascii.py input.mp4 -o custom.mp4 -f mp4 \
  -w 120 --height 40 --fps 15
```

## 🎨 Creative Effects

### Cinematic Depth Effect

```bash
# Movie-like depth and contrast
python video_ascii.py movie.mp4 -o cinematic.txt \
  --depth-effect \
  --contrast 1.3 \
  --gamma 0.8 \
  --char-set detailed \
  --brightness 0.1
```

**Result**: Creates a film-like appearance with enhanced depth perception and dramatic contrast.

### Comic Book Style

```bash
# Bold, high-contrast comic book effect
python video_ascii.py animation.mp4 -o comic.gif -f gif \
  --edge-detection \
  --contrast 1.8 \
  --char-set detailed \
  --fps 12
```

**Result**: Emphasizes outlines and creates a graphic novel aesthetic.

### Retro Terminal Look

```bash
# Old-school computer terminal style
python video_ascii.py retro.mp4 -o terminal.txt \
  --invert \
  --char-set gradient \
  --brightness 0.3 \
  --contrast 0.9 \
  -w 80 --height 24
```

**Result**: Mimics classic green-on-black terminal displays.

### Dreamy Blur Effect

```bash
# Soft, artistic blur with enhanced contrast
python video_ascii.py nature.mp4 -o dreamy.gif -f gif \
  --blur 0.4 \
  --contrast 1.5 \
  --gamma 1.2 \
  --char-set blocks
```

**Result**: Creates a soft, ethereal appearance perfect for artistic content.

### High-Contrast Technical Drawing

```bash
# Technical/blueprint style
python video_ascii.py technical.mp4 -o blueprint.txt \
  --edge-detection \
  --invert \
  --contrast 2.0 \
  --char-set simple \
  --brightness -0.2
```

**Result**: Produces clean, technical drawing-like output.

## ⚡ Performance Optimization

### Low-End Device Settings

```bash
# Optimized for devices with limited resources
python video_ascii.py large_video.mp4 -o optimized.txt \
  --quality low \
  --fps 5 \
  -w 60 \
  --height 20 \
  --char-set simple
```

**Memory Usage**: ~50MB  
**Processing Speed**: 3-4x faster than default

### High-End Device Settings

```bash
# Maximum quality for powerful systems
python video_ascii.py video.mp4 -o premium.gif -f gif \
  --quality high \
  --fps 30 \
  -w 200 \
  --height 60 \
  --char-set detailed \
  --depth-effect \
  --contrast 1.2
```

**Memory Usage**: ~500MB  
**Processing Speed**: Slower but highest quality

### Balanced Settings

```bash
# Good quality with reasonable performance
python video_ascii.py video.mp4 -o balanced.mp4 -f mp4 \
  --quality medium \
  --fps 15 \
  -w 120 \
  --height 35 \
  --char-set standard
```

**Memory Usage**: ~150MB  
**Processing Speed**: Standard baseline

## 🔄 Batch Processing

### Processing Multiple Videos

Create a simple bash script for batch processing:

```bash
#!/bin/bash
# batch_convert.sh

# Directory containing videos
VIDEO_DIR="./input_videos"
OUTPUT_DIR="./ascii_output"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Process each video file
for video in "$VIDEO_DIR"/*.mp4; do
    filename=$(basename "$video" .mp4)
    echo "Processing: $filename"
    
    python video_ascii.py "$video" \
        -o "$OUTPUT_DIR/${filename}_ascii.txt" \
        --fps 10 \
        -w 100 \
        --char-set standard
    
    echo "Completed: $filename"
done

echo "Batch processing complete!"
```

### Different Formats for Same Video

```bash
#!/bin/bash
# multi_format.sh

VIDEO="input.mp4"
BASE_NAME="output"

# Generate all formats
python video_ascii.py "$VIDEO" -o "${BASE_NAME}.txt" --fps 10
python video_ascii.py "$VIDEO" -o "${BASE_NAME}.gif" -f gif --fps 15 -w 120
python video_ascii.py "$VIDEO" -o "${BASE_NAME}.mp4" -f mp4 --fps 12
```

## ⚙️ Configuration Management

### Creating Preset Configurations

#### Preset 1: Social Media Ready
```bash
# Create and save social media preset
python video_ascii.py sample.mp4 -o test.gif -f gif \
  -w 100 \
  --fps 15 \
  --char-set gradient \
  --contrast 1.2 \
  --save-config social_media.json
```

**Use case**: Perfect for sharing on social platforms

#### Preset 2: High Detail Analysis
```bash
# Create detailed analysis preset
python video_ascii.py sample.mp4 -o test.txt \
  -w 200 \
  --height 60 \
  --char-set detailed \
  --depth-effect \
  --edge-detection \
  --contrast 1.1 \
  --save-config detailed_analysis.json
```

**Use case**: For detailed video analysis and documentation

#### Preset 3: Performance Mode
```bash
# Create fast processing preset
python video_ascii.py sample.mp4 -o test.txt \
  --quality low \
  --fps 5 \
  -w 60 \
  --height 15 \
  --char-set simple \
  --save-config performance.json
```

**Use case**: Quick previews and testing

### Using Saved Presets

```bash
# Apply social media preset to new video
python video_ascii.py new_video.mp4 -o social.gif -f gif \
  --load-config social_media.json

# Apply detailed analysis to multiple videos
for video in *.mp4; do
    python video_ascii.py "$video" -o "${video%.mp4}_detailed.txt" \
        --load-config detailed_analysis.json
done
```

## 🔍 Preview and Testing

### Quick Preview Before Processing

```bash
# Test settings on first frame only
python video_ascii.py large_video.mp4 -o preview.txt --preview

# Preview with effects
python video_ascii.py video.mp4 -o preview.txt --preview \
  --depth-effect --contrast 1.5 --char-set detailed
```

### A/B Testing Different Settings

```bash
#!/bin/bash
# compare_settings.sh

VIDEO="test_video.mp4"

echo "Testing different character sets..."

# Test different character sets
for charset in simple standard detailed gradient blocks; do
    echo "Testing: $charset"
    python video_ascii.py "$VIDEO" -o "test_${charset}.txt" \
        --char-set "$charset" --preview
    echo "---"
done
```

## 🎯 Specific Use Cases

### Educational Content

```bash
# Clear, readable educational videos
python video_ascii.py lecture.mp4 -o lecture_ascii.txt \
  -w 120 \
  --height 40 \
  --char-set standard \
  --contrast 1.1 \
  --fps 8
```

### Art Projects

```bash
# Artistic interpretation with multiple effects
python video_ascii.py artwork.mp4 -o art_ascii.gif -f gif \
  --depth-effect \
  --blur 0.2 \
  --contrast 1.4 \
  --gamma 1.1 \
  --char-set blocks \
  --fps 18
```

### Technical Documentation

```bash
# Clean, technical documentation style
python video_ascii.py demo.mp4 -o technical_doc.txt \
  --edge-detection \
  --contrast 1.6 \
  --char-set simple \
  --brightness 0.1 \
  -w 100
```

### Entertainment/Memes

```bash
# Fun, shareable content
python video_ascii.py meme.mp4 -o funny.gif -f gif \
  --invert \
  --char-set gradient \
  --contrast 1.3 \
  --fps 20 \
  -w 80
```

## 🛠️ Troubleshooting Common Issues

### Issue: Poor Quality Output

**Problem**: ASCII art looks unclear or poorly defined

**Solutions**:
```bash
# Increase contrast and try different character set
python video_ascii.py input.mp4 -o better.txt \
  --contrast 1.5 \
  --char-set detailed \
  --brightness 0.1

# Use edge detection for better definition
python video_ascii.py input.mp4 -o edges.txt \
  --edge-detection \
  --contrast 1.3
```

### Issue: File Too Large

**Problem**: Output GIF or MP4 is too large

**Solutions**:
```bash
# Reduce resolution and frame rate
python video_ascii.py input.mp4 -o smaller.gif -f gif \
  -w 80 \
  --fps 10 \
  --quality low

# Use simpler character set
python video_ascii.py input.mp4 -o compact.gif -f gif \
  --char-set simple
```

### Issue: Slow Processing

**Problem**: Conversion takes too long

**Solutions**:
```bash
# Use performance optimizations
python video_ascii.py slow_video.mp4 -o fast.txt \
  --quality low \
  --fps 5 \
  -w 60 \
  --height 20

# Preview first to test settings
python video_ascii.py slow_video.mp4 -o test.txt --preview \
  --your-settings-here
```

### Issue: Memory Problems

**Problem**: Running out of memory during processing

**Solutions**:
```bash
# Minimize memory usage
python video_ascii.py large.mp4 -o output.txt \
  --quality low \
  -w 50 \
  --height 15 \
  --fps 3
```

## 📊 Performance Guidelines

### Resolution vs. Performance

| Width | Height | Memory Usage | Relative Speed |
|-------|--------|--------------|----------------|
| 60    | 15     | ~50MB        | 4x faster     |
| 80    | 24     | ~100MB       | 2x faster     |
| 120   | 35     | ~150MB       | 1x baseline   |
| 200   | 60     | ~300MB       | 0.3x slower   |

### Effect Impact on Performance

| Effect | Performance Impact | Quality Improvement |
|--------|-------------------|-------------------|
| `--depth-effect` | -20% | High |
| `--edge-detection` | -15% | Medium |
| `--blur 0.5` | -10% | Medium |
| `--detailed charset` | -5% | High |

---

**💡 Tip**: Always use `--preview` to test your settings before processing long videos!

**🎯 Remember**: The best settings depend on your specific video content, target audience, and performance requirements. Experiment with different combinations to find what works best for your use case.

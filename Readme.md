# Video ASCII Art Converter

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)](https://github.com)

A powerful, feature-rich command-line tool that converts videos into high-quality ASCII art. Designed for performance and flexibility, it supports multiple output formats and advanced visual effects while remaining optimized for low-end devices.

![ASCII Art Demo](https://via.placeholder.com/800x400/000000/FFFFFF?text=ASCII+VIDEO+DEMO)

## ✨ Features

### 🎯 **Multiple Output Formats**
- **TXT**: ASCII frames with frame separators for easy viewing
- **GIF**: Animated ASCII art as image files
- **MP4**: ASCII art video with proper timing and playback

### 🎨 **Advanced Visual Effects**
- **Depth Effect**: 3D-like depth simulation using blur analysis
- **Edge Detection**: Canny edge detection for outline effects
- **Image Enhancement**: Contrast, brightness, and gamma correction
- **Blur Effects**: Gaussian blur for artistic styling
- **Color Inversion**: Reverse black/white for different aesthetics

### 🔧 **Extensive Customization**
- **5 Character Sets**: From simple to highly detailed ASCII characters
- **Resolution Control**: Custom width and height settings
- **FPS Control**: Adjustable frame rate for smooth or stylized playback
- **Quality Levels**: Low/medium/high processing options
- **Configuration Files**: Save and load custom presets

### ⚡ **Performance Optimized**
- **Low Memory Usage**: Frame-by-frame processing
- **Device Optimization**: Configurable quality for different hardware
- **Progress Monitoring**: Real-time conversion progress
- **Smart Frame Skipping**: Automatic optimization for target FPS

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/video-ascii-converter.git
   cd video-ascii-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run your first conversion**
   ```bash
   python video_ascii.py input.mp4 -o output.txt
   ```

### Basic Usage

```bash
# Convert to ASCII text file
python video_ascii.py video.mp4 -o ascii_art.txt

# Create animated GIF
python video_ascii.py video.mp4 -o ascii_art.gif -f gif

# Generate ASCII MP4 video
python video_ascii.py video.mp4 -o ascii_video.mp4 -f mp4
```

## 📚 Documentation

### Command Line Arguments

#### **Required Arguments**
```bash
python video_ascii.py INPUT_VIDEO -o OUTPUT_FILE
```

#### **Format Options**
| Flag | Options | Default | Description |
|------|---------|---------|-------------|
| `-f, --format` | `txt`, `gif`, `mp4` | `txt` | Output format |

#### **Dimension Settings**
| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-w, --width` | Integer | `80` | ASCII art width in characters |
| `--height` | Integer | `24` | ASCII art height in characters |

#### **Quality & Performance**
| Flag | Options/Type | Default | Description |
|------|-------------|---------|-------------|
| `--fps` | Float | `10` | Target frames per second |
| `--char-set` | `simple`, `standard`, `detailed`, `gradient`, `blocks` | `standard` | ASCII character complexity |
| `--quality` | `low`, `medium`, `high` | `medium` | Processing quality level |

#### **Visual Effects**
| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--contrast` | Float | `1.0` | Contrast adjustment (0.5-2.0) |
| `--brightness` | Float | `0.0` | Brightness adjustment (-1.0 to 1.0) |
| `--gamma` | Float | `1.0` | Gamma correction (0.5-2.0) |
| `--blur` | Float | `0.0` | Blur effect intensity (0.0-1.0) |
| `--invert` | Flag | - | Invert black/white colors |
| `--edge-detection` | Flag | - | Enable edge detection effect |
| `--depth-effect` | Flag | - | Enable 3D depth simulation |

#### **Configuration Management**
| Flag | Type | Description |
|------|------|-------------|
| `--save-config` | String | Save current settings to JSON file |
| `--load-config` | String | Load settings from JSON file |
| `--preview` | Flag | Show preview of first frame only |

### Character Sets Explained

| Set Name | Characters | Best For |
|----------|------------|----------|
| `simple` | ` .:-=+*#%@` | Fast processing, minimal detail |
| `standard` | Full ASCII range (70+ chars) | Balanced quality and performance |
| `detailed` | Extended ASCII set | High detail, slower processing |
| `gradient` | `░▒▓█` | Smooth gradients, modern look |
| `blocks` | `▁▂▃▄▅▆▇█` | Vertical intensity representation |

## 💡 Usage Examples

### Basic Conversions

```bash
# Simple text conversion
python video_ascii.py movie.mp4 -o movie_ascii.txt

# High-resolution GIF
python video_ascii.py clip.mp4 -o clip.gif -f gif -w 150 --fps 20

# Edge-detected MP4
python video_ascii.py video.mp4 -o edges.mp4 -f mp4 --edge-detection
```

### Advanced Effects

```bash
# Cinematic depth effect
python video_ascii.py film.mp4 -o cinematic.txt \
  --depth-effect --contrast 1.3 --gamma 0.8 --char-set detailed

# Retro terminal style
python video_ascii.py retro.mp4 -o terminal.gif -f gif \
  --invert --char-set gradient --brightness 0.2

# High contrast artistic
python video_ascii.py art.mp4 -o artistic.mp4 -f mp4 \
  --edge-detection --contrast 2.0 --blur 0.3
```

### Configuration Management

```bash
# Save your favorite settings
python video_ascii.py test.mp4 -o test.txt \
  --contrast 1.5 --depth-effect --char-set detailed \
  --save-config my_preset.json

# Use saved settings
python video_ascii.py new_video.mp4 -o output.gif -f gif \
  --load-config my_preset.json

# Preview before processing
python video_ascii.py large_video.mp4 -o preview.txt --preview
```

### Performance Optimization

```bash
# Low-end device settings
python video_ascii.py video.mp4 -o low_quality.txt \
  --quality low --fps 5 -w 60 --height 20

# High-end device settings
python video_ascii.py video.mp4 -o high_quality.gif -f gif \
  --quality high --fps 30 -w 200 --depth-effect --detailed
```

## 🔧 Technical Details

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `opencv-python` | `>=4.0.0` | Video processing and computer vision |
| `Pillow` | `>=8.0.0` | Image manipulation for GIF creation |
| `numpy` | `>=1.19.0` | Numerical operations and array handling |

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Python Version** | 3.6+ | 3.8+ |
| **RAM** | 512MB | 2GB+ |
| **Storage** | 50MB | 200MB+ |
| **CPU** | Single-core | Multi-core |

### Performance Benchmarks

| Resolution | FPS | Processing Time* | Memory Usage |
|------------|-----|-----------------|--------------|
| 80x24 | 10 | 1x | ~100MB |
| 120x40 | 15 | 2.5x | ~150MB |
| 200x60 | 30 | 8x | ~300MB |

*Relative to 1-minute video baseline

## 🎨 Creative Tips

### Choosing Character Sets
- **Simple**: Perfect for quick previews and low-detail content
- **Standard**: Best all-around choice for most videos
- **Detailed**: Use for high-contrast, detailed scenes
- **Gradient**: Excellent for smooth transitions and modern aesthetics
- **Blocks**: Great for representing vertical elements and intensity

### Effect Combinations
- **Cinematic Look**: `--depth-effect --contrast 1.2 --gamma 0.9`
- **Comic Book Style**: `--edge-detection --contrast 1.8 --char-set detailed`
- **Retro Terminal**: `--invert --char-set gradient --brightness 0.3`
- **Artistic Blur**: `--blur 0.4 --contrast 1.5 --char-set blocks`

### Optimization Tips
- Start with `--preview` to test settings quickly
- Use lower FPS for larger resolutions
- Save frequently used settings with `--save-config`
- For GIFs, keep width under 150 characters for better compatibility

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Bug Reports
1. Check existing issues first
2. Provide detailed reproduction steps
3. Include system information and error messages
4. Test with minimal examples

### Feature Requests
1. Describe the use case clearly
2. Explain why the feature would be valuable
3. Consider implementation complexity
4. Provide examples if possible

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Follow existing code style and conventions
4. Add tests for new functionality
5. Update documentation as needed
6. Submit a pull request with clear description

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/video-ascii-converter.git
cd video-ascii-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 🐛 Troubleshooting

### Common Issues

#### **"Could not open video file"**
- **Cause**: Unsupported video format or corrupted file
- **Solution**: Convert video to MP4/AVI format first
- **Test**: Try with a different video file

#### **"Memory Error" during processing**
- **Cause**: Video too large for available RAM
- **Solution**: Reduce resolution (`-w`, `--height`) or use `--quality low`
- **Alternative**: Process shorter video segments

#### **Slow processing speed**
- **Cause**: High resolution or complex effects
- **Solution**: Lower FPS (`--fps`), reduce size, or disable effects
- **Monitor**: Use preview mode to test settings first

#### **Poor ASCII quality**
- **Cause**: Low contrast in source video
- **Solution**: Increase `--contrast` and adjust `--brightness`
- **Try**: Different character sets or enable `--edge-detection`

#### **GIF too large**
- **Cause**: High resolution or long duration
- **Solution**: Reduce width, lower FPS, or trim video length
- **Optimize**: Use `--quality low` for smaller file sizes

### Getting Help

1. **Check the documentation** - Most questions are answered here
2. **Search existing issues** - Your problem might already be solved
3. **Create a new issue** - Provide detailed information about your problem
4. **Join discussions** - Share tips and get community help

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV Team** - For excellent computer vision library
- **Pillow Contributors** - For powerful image processing capabilities  
- **ASCII Art Community** - For inspiration and character set ideas
- **Contributors** - Everyone who has helped improve this project

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/video-ascii-converter?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/video-ascii-converter?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/video-ascii-converter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/video-ascii-converter)

---

**Made with ❤️ for the ASCII art community**

*Turn your videos into terminal-friendly masterpieces!*

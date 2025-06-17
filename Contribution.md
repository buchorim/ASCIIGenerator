# Contributing to Video ASCII Art Converter

Thank you for your interest in contributing! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Git
- Basic understanding of video processing concepts

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/video-ascii-converter.git
   cd video-ascii-converter
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Test Installation**
   ```bash
   python video_ascii.py --help
   ```

## 🐛 Reporting Issues

### Before Submitting
- Search existing issues to avoid duplicates
- Test with the latest version
- Gather necessary information

### Issue Template
Please include:

**Bug Description**
- Clear, concise description of the problem
- Expected vs actual behavior

**Environment**
- Operating System and version
- Python version
- Package versions (`pip list`)

**Reproduction Steps**
1. Step-by-step instructions
2. Minimal test case
3. Sample video file (if relevant)

**Additional Information**
- Error messages and stack traces
- Screenshots (for visual issues)
- Configuration files used

## 💡 Feature Requests

### Good Feature Requests Include:
- **Problem Statement**: What problem does this solve?
- **Use Case**: How would you use this feature?
- **Implementation Ideas**: Any thoughts on how it could work?
- **Examples**: Similar features in other tools

### Feature Priorities
We prioritize features that:
- Improve performance on low-end devices
- Add new creative ASCII effects
- Enhance user experience
- Maintain backward compatibility

## 🔧 Code Contributions

### Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Test basic functionality
   python video_ascii.py test_video.mp4 -o test_output.txt
   
   # Test new features
   python video_ascii.py test_video.mp4 -o test.gif -f gif --your-new-flag
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add new ASCII character set support"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Code Style Guidelines

#### **Python Style**
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

#### **Example Code Style**
```python
def convert_frame_to_ascii(self, frame: np.ndarray, char_set: str) -> str:
    """
    Convert a single video frame to ASCII art.
    
    Args:
        frame: Input video frame as numpy array
        char_set: Name of character set to use
        
    Returns:
        ASCII representation of the frame as string
        
    Raises:
        ValueError: If char_set is not recognized
    """
    if char_set not in self.ascii_chars:
        raise ValueError(f"Unknown character set: {char_set}")
    
    # Implementation here...
    return ascii_string
```

#### **Commit Messages**
Use conventional commit format:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `perf:` - Performance improvements

### Testing Guidelines

#### **Manual Testing Checklist**
- [ ] Test with different video formats (MP4, AVI, MOV)
- [ ] Test all output formats (TXT, GIF, MP4)
- [ ] Test various character sets
- [ ] Test edge cases (very short/long videos)
- [ ] Test on different operating systems
- [ ] Verify memory usage stays reasonable

#### **Performance Testing**
- Test with low-end device specifications
- Monitor memory usage during processing
- Measure processing time for different settings
- Ensure graceful handling of large files

## 📝 Documentation

### What to Document
- New command-line options
- New character sets or effects
- Configuration file changes
- Performance considerations
- Breaking changes

### Documentation Style
- Use clear, concise language
- Include practical examples
- Add screenshots for visual features
- Update README.md for major changes

## 🎯 Areas for Contribution

### High Priority
- **Performance Optimization**: Faster frame processing
- **Memory Management**: Better handling of large videos
- **Error Handling**: More robust error messages
- **Cross-platform Testing**: Windows/Mac/Linux compatibility

### Medium Priority
- **New Effects**: Creative ASCII transformations
- **Output Formats**: Additional export options
- **Character Sets**: More ASCII character collections
- **Configuration**: Enhanced preset management

### Low Priority
- **GUI Interface**: Optional graphical interface
- **Batch Processing**: Multiple file handling
- **Cloud Integration**: Online processing options
- **Advanced Filters**: Complex image processing

## 🏗️ Architecture Overview

### Core Components

```
video_ascii.py
├── VideoASCIIConverter (main class)
│   ├── load_video()           # Video file handling
│   ├── apply_image_effects()  # Image processing
│   ├── create_depth_map()     # Depth effect generation
│   ├── frame_to_ascii()       # Core ASCII conversion
│   ├── convert_to_txt()       # Text output
│   ├── convert_to_gif()       # GIF output
│   └── convert_to_mp4()       # MP4 output
└── main()                     # CLI argument parsing
```

### Adding New Features

#### **New Character Set**
1. Add to `ascii_chars` dictionary in `__init__()`
2. Update CLI choices in argument parser
3. Test with various video types
4. Update documentation

#### **New Effect**
1. Add effect logic to `apply_image_effects()`
2. Add command-line argument
3. Update settings dictionary
4. Add to configuration save/load
5. Document usage and examples

#### **New Output Format**
1. Create new `convert_to_format()` method
2. Add format choice to CLI parser
3. Handle format-specific requirements
4. Test thoroughly with different inputs

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain a positive, collaborative environment

### Communication
- Use clear, descriptive issue titles
- Provide context in discussions
- Be patient with response times
- Ask questions if something is unclear

### Review Process
- All PRs require review before merging
- Reviewers will check functionality and code quality
- Be open to feedback and suggestions
- Address review comments promptly

## 📋 Release Process

### Version Numbering
We use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, small improvements

### Release Checklist
- [ ] Update version number
- [ ] Update CHANGELOG.md
- [ ] Test on multiple platforms
- [ ] Update documentation
- [ ] Create release notes
- [ ] Tag release in Git

## 🎉 Recognition

Contributors will be recognized in:
- README.md acknowledgments
- Release notes
- GitHub contributors list

Thank you for helping make this project better!

---

**Questions?** Open an issue or start a discussion. We're here to help!

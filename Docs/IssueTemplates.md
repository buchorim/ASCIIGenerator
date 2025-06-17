# GitHub Issue Templates

Create a `.github/ISSUE_TEMPLATE/` directory and add these files:

## Bug Report Template
**File**: `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: 'bug'
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command: `python video_ascii.py ...`
2. Use these settings: '...'
3. With this video file: '...'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Actual behavior**
What actually happened instead.

**Screenshots/Output**
If applicable, add screenshots or console output to help explain your problem.

**Environment (please complete the following information):**
- OS: [e.g. Windows 10, Ubuntu 20.04, macOS 12.0]
- Python Version: [e.g. 3.8.5]
- Package Versions: [run `pip list` and paste relevant versions]
- Video format: [e.g. MP4, AVI, MOV]
- Video details: [resolution, duration, codec if known]

**Command used:**
```bash
python video_ascii.py [paste your full command here]
```

**Error message (if any):**
```
[paste the full error message here]
```

**Additional context**
Add any other context about the problem here.

**Possible solution**
If you have ideas about what might be causing the issue or how to fix it, please share.
```

## Feature Request Template
**File**: `.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: 'enhancement'
assignees: ''
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Use case**
Describe how you would use this feature. What would be the typical workflow?

**Examples**
If you've seen this feature in other tools, please provide examples or references.

**Implementation ideas**
If you have thoughts on how this could be implemented, please share them.

**Additional context**
Add any other context, screenshots, or examples about the feature request here.

**Priority**
How important is this feature to you?
- [ ] Critical - I cannot use the tool without this
- [ ] High - This would significantly improve my workflow
- [ ] Medium - This would be nice to have
- [ ] Low - This is just a suggestion
```

## Performance Issue Template
**File**: `.github/ISSUE_TEMPLATE/performance_issue.md`

```markdown
---
name: Performance issue
about: Report slow performance or high memory usage
title: '[PERFORMANCE] '
labels: 'performance'
assignees: ''
---

**Performance Problem**
Describe the performance issue you're experiencing.

**System Specifications**
- CPU: [e.g. Intel i5-8400, AMD Ryzen 5 3600]
- RAM: [e.g. 8GB, 16GB]
- Storage: [e.g. SSD, HDD]
- OS: [e.g. Windows 10, Ubuntu 20.04]

**Video Details**
- Resolution: [e.g. 1920x1080, 4K]
- Duration: [e.g. 30 seconds, 5 minutes]
- Format: [e.g. MP4, AVI]
- File size: [e.g. 100MB, 2GB]

**Settings Used**
```bash
python video_ascii.py [paste your command here]
```

**Performance Measurements**
- Processing time: [e.g. 5 minutes for 30-second video]
- Memory usage: [e.g. peaked at 2GB RAM]
- CPU usage: [e.g. 100% on all cores]

**Expected Performance**
What performance did you expect based on your system specs?

**Comparison**
Have you tried different settings? What were the results?
- Lower resolution: [results]
- Different quality settings: [results]
- Different effects enabled/disabled: [results]

**Additional Information**
- Were other applications running?
- Any error messages or warnings?
- Did the system become unresponsive?
```

## Question Template
**File**: `.github/ISSUE_TEMPLATE/question.md`

```markdown
---
name: Question
about: Ask a question about usage or functionality
title: '[QUESTION] '
labels: 'question'
assignees: ''
---

**Your Question**
What would you like to know?

**What you've tried**
Please describe what you've already attempted or researched.

**Context**
Provide any relevant context about your use case or environment.

**Examples**
If applicable, provide examples of what you're trying to achieve.
```

---

# Pull Request Template

**File**: `.github/pull_request_template.md`

```markdown
## Description
Brief description of changes made.

## Type of Change
Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Changes Made
- List specific changes
- Include any new files added
- Mention any files removed or significantly modified

## Testing
Describe the tests you ran to verify your changes:

- [ ] Tested with sample videos
- [ ] Tested all output formats (TXT, GIF, MP4)
- [ ] Tested various character sets
- [ ] Tested edge cases
- [ ] Verified performance impact
- [ ] Tested on multiple platforms (if applicable)

**Test Configuration:**
- OS: 
- Python Version:
- Video formats tested:

## Screenshots (if applicable)
Add screenshots or output samples to help explain your changes.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Additional Notes
Any additional information, concerns, or questions about this PR.
```

---

# GitHub Actions Workflow

**File**: `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: [3.6, 3.7, 3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest
    
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics
    
    - name: Test basic functionality
      run: |
        python video_ascii.py --help
        # Add more comprehensive tests here when test suite is created
    
    - name: Test with sample video (Ubuntu only)
      if: matrix.os == 'ubuntu-latest'
      run: |
        # Create a simple test video using ffmpeg
        sudo apt-get update
        sudo apt-get install -y ffmpeg
        ffmpeg -f lavfi -i testsrc=duration=1:size=320x240:rate=1 -c:v libx264 test_video.mp4
        python video_ascii.py test_video.mp4 -o test_output.txt --preview
```

---

# Additional Repository Files

## .gitignore
**File**: `.gitignore`

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE files
.vscode/
.idea/
*.swp
*.swo
*~

# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
*.mp4
*.avi
*.mov
*.gif
*.txt
test_videos/
output/
temp/
*.json
!example_config.json

# Logs
*.log
logs/
```

## Example Configuration
**File**: `example_config.json`

```json
{
  "width": 120,
  "height": 40,
  "fps": 15,
  "char_set": "standard",
  "color_mode": "grayscale",
  "contrast": 1.2,
  "brightness": 0.1,
  "gamma": 1.0,
  "invert": false,
  "edge_detection": false,
  "depth_effect": true,
  "blur": 0.0,
  "quality": "medium"
}
```

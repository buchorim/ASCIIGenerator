#!/usr/bin/env python3
"""
Setup script for Video ASCII Art Converter
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Read version from the main script
def get_version():
    """Extract version from the main script"""
    version = "1.0.0"  # Default version
    try:
        with open("video_ascii.py", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("__version__"):
                    version = line.split("=")[1].strip().strip('"').strip("'")
                    break
    except FileNotFoundError:
        pass
    return version

setup(
    name="video-ascii-converter",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert videos to high-quality ASCII art with advanced effects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/video-ascii-converter",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/video-ascii-converter/issues",
        "Documentation": "https://github.com/yourusername/video-ascii-converter#readme",
        "Source Code": "https://github.com/yourusername/video-ascii-converter",
    },
    py_modules=["video_ascii"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Artistic Software",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8.0",
            "black>=21.0.0",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "video-ascii=video_ascii:main",
            "ascii-video=video_ascii:main",
        ],
    },
    keywords=[
        "ascii", "art", "video", "converter", "terminal", "cli", 
        "animation", "text", "gif", "mp4", "effects", "depth"
    ],
    include_package_data=True,
    zip_safe=False,
)

"""gitignore Setup

Setup specifications for gitignore project.
"""
from setuptools import setup

setup(
    name="gitignore",
    version="0.2",
    py_modules=["gitignore"],
    entry_points={
        "console_scripts": [
            "gitignore = gitignore:main"
        ]
    },
    install_requires=[
        "requests",
        "prompt-toolkit"
    ]
)

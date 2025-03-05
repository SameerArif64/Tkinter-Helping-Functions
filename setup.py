from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="window_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Sameer Arif",
    author_email="supersameer64@gmail.com",
    description="A Python utility library for managing active windows and displaying always-on-top dialogs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SameerArif64/window-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)

from setuptools import setup, find_packages

setup(
    name="tkinter_helping_func",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [line.strip() for line in open("requirements.txt") if line.strip()],
    author="Sameer Arif",
    author_email="supersameer64@gmail.com",
    description="A Python utility library for managing active windows and displaying always-on-top dialogs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SameerArif64/Tkinter-Helping-Functions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)

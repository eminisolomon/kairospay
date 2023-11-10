import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monnify_python",
    version="1.0.0",
    author="Solomon Olatunji",
    author_email="aotoluwalope@gmail.com",
    description="Monnify Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eminisolomon/monnify-python.git",
    packages=setuptools.find_packages(),
    keywords=['python', 'payment', 'gateway', 'monnify', 'payment gateway'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
    ],
)

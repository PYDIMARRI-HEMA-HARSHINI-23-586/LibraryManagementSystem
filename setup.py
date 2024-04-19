"""Configuration to be set while converting existing fucionalities into python package."""

import setuptools

with open("requirements.txt", encoding="utf-8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="libutils",
    version="0.0.1",
    author="PavanKumarPHV",
    author_email="phvpavankumar@gmail.com",
    description="Library utils package designed for LMS CML application.",
    install_requires=required,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
)

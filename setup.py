from setuptools import find_packages, setup

setup(
    name="geo-pipeline",
    version="0.0.13",
    url="https://github.com/aausek/GEO_Pipeline",
    description="NCBI GEO data extraction pipeline",
    license="MIT",
    author="Ana Ausek",
    install_requires=[],
    packages=find_packages(include=["src", "src.*"]),
    include_package_data=True,
    entry_points={"console_scripts": ["pipeline=src.pipeline:main"]},
    
)
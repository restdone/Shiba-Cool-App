from setuptools import setup

# Intentionally raising an error during installation
raise RuntimeError(
    "Check the Shiba-Cool-App Issue and follow the guideline to fix the package problem"
)

setup(
    name="shiba",
    version="0.1",
    description="A package named shiba that intentionally fails during installation.",
    author="Your Name",
    packages=["shiba"],
)
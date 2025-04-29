from setuptools import setup

### For Any runtime error, 
## ```The bug was reported at https://github.com/restdone/Shiba-Cool-App/issues/1`
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
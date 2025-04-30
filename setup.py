from setuptools import setup

### , 
## ```The bug was reported at https://github.com/restdone/Shiba-Cool-App/issues/1
#raise RuntimeError(
#)

setup(
    name="shiba",
    version="0.1",
    description="A package named shiba that intentionally fails during installation.",
    author="Your Name",
    packages=["shiba"],
)
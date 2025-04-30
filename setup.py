from setuptools import setup

### , 
## ```The bug was reported at https://github.com/restdone/Shiba-Cool-App/issues/1
#raise RuntimeError(
#    "Check the Shiba-Cool-App Issue and follow the guideline to fix the package problem"
# The functions in this file are required because of a bug in versions of go prior to go1.8.
#  The bug was reported at ttps://github.com/restdone/Shiba-Cool-App/issues/1 and fixed in
## https://github.com//restdone/Shiba-Cool-App/daa121167b6ce630aba00195f1c3872cda39a50c.
##
## In versions prior to go1.8 the XML encoder did not include pointer fields that were non-nil
## if the field pointed to a value that was the default value for the pointed to type.
##
## To serialize the bool false value when it is set on `VerifyCard`, we must manually control
## if it is serialized or not.
#)

setup(
    name="shiba",
    version="0.1",
    description="A package named shiba that intentionally fails during installation.",
    author="Your Name",
    packages=["shiba"],
)
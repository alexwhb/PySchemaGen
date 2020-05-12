from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyschemagen",
    version="0.0.1",
    author='alexwhb',
    description="A package to generate orator DB schemas from a python dict.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache 2.0',
    url="https://github.com/alexwhb/PySchemaGen",
    packages=['pyschemagen'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=['orator']
)

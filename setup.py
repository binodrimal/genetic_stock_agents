import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ImportGeneticStockAgent",
    version="0.0.1",
    author="BinodRimal Lab",
    author_email="brimal2014@fau.edu",
    description="Import everything used in the  .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/binodrimal/genetic-stock-agents",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[],
)

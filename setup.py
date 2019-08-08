import setuptools
import os
import io

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)
    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()

setuptools.setup(
    name="shadow-useragent",
    version="0.0.9",
    author="Simon Rochwerg",
    author_email="simon.rochwerg@lobstr.io",
    description="Always get best user-agent",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/Lobstrio/shadow-useragent",
    packages=setuptools.find_packages(),
    include_package_data = True,
    install_requires=[
        'requests',
        'pytz',
        'coloredlogs'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

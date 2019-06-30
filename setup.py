#!/usr/bin/env python
# coding: utf8
import io
import os
from setuptools import setup

def get_absolute_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_variable_from_meta_file(variable):
    def get_variable_name(line):
        return line[:line.index("=")].strip()
        
    def get_variable_value(line):
        return line[line.index("=")+1:].strip().strip("\"")

    def get_matching_lines(fobj, str):
        return [line for line in fobj if get_variable_name(line) == str]

    def read_variable_from_file(filename, variable):
        with io.open(get_absolute_path(filename), encoding="utf8") as fobj:
            matching_lines = get_matching_lines(fobj, variable)
            return get_variable_value(matching_lines[0])
    
    return read_variable_from_file("asysync/meta.py", variable)
    
def read_description_file():
    with io.open(get_absolute_path("docs/description.rst"), encoding="utf8") as fobj:
        lines = fobj.readlines()
        return "".join(lines).strip()

setup(
    packages=["asysync"],
    name="asysync",
    version=read_variable_from_meta_file("__version__"),
    author=read_variable_from_meta_file("__author__"),
    author_email=read_variable_from_meta_file("__email__"),
    url=read_variable_from_meta_file("__url__"),
    description=read_variable_from_meta_file("__summary__"),
    license=read_variable_from_meta_file("__license__"),
    long_description=read_description_file(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications :: File Sharing"
    ],
    platforms="any"
)
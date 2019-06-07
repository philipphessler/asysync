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
		with open(get_absolute_path(filename), encoding="utf8") as fobj:
			matching_lines = get_matching_lines(fobj, variable)
			return get_variable_value(matching_lines[0])
	
	return read_variable_from_file("asysync/meta.py", variable)

def read_first_paragraph_from_readme_file():
	def starts_with_alpha(line):
		return line and line[0].isalpha()

	def get_first_index_with_condition(iterable, condition: lambda x: True):
		return next(index for index, x in enumerate(iterable) if condition(x))

	def drop_lines_before_first_paragraph(lines):
		index = get_first_index_with_condition(lines, lambda l: starts_with_alpha(l))
		return lines[index:]

	def drop_lines_after_first_paragraph(lines):
		index = get_first_index_with_condition(lines, lambda l: not starts_with_alpha(l))
		return lines[:index]
	
	def read_first_paragraph(filename):
		with open(get_absolute_path(filename), encoding="utf8") as fobj:
			lines = fobj.readlines()
			lines = drop_lines_before_first_paragraph(lines)
			lines = drop_lines_after_first_paragraph(lines)
			return "".join(lines).strip()
	
	return read_first_paragraph("README.md")

setup(
    packages=["asysync"],
    name="asysync",
    version=read_variable_from_meta_file("__version__"),
	author=read_variable_from_meta_file("__author__"),
	author_email=read_variable_from_meta_file("__email__"),
	url=read_variable_from_meta_file("__url__"),
	description=read_variable_from_meta_file("__summary__"),
    license=read_variable_from_meta_file("__license__"),
    long_description=read_first_paragraph_from_readme_file(),
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
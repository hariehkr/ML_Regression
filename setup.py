"""
The setup.py file is an essential part of the packing and distributing Python projects. 
 it is used by setup tools (or  diutilis  in older Python versions)  to define the configuration 
 of your project,  such as its metadata, dependencies, and more

"""
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements from a file and returns them as a list.
    
    Args:
        file_path (str): The path to the requirements file.
    """
    requirement_list: List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            # Read lines from the file and strip whitespace
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e lines
                if requirement and not requirement == '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file 'requirements.txt' was not found.")

    return requirement_list
setup(
    name='ML_Regression',
    version='0.1.0',
    author='Hari',
    author_email="hariehkr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A Python package for network security analysis and machine learning.',
)
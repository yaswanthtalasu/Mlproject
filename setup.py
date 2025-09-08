# building our application as a package
from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(filepath:str)->List[str]:
    with open (filepath) as file :
        requirements = file.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name = 'ml_project',
    version = '0.0.0.1',
    author='yash',
    author_email='y.email.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

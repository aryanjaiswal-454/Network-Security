from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    HYPHEN_E_DOT='-e .'
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!=HYPHEN_E_DOT:
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aryan Jaiswal",
    author_email="45aryanjaiswal45@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
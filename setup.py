from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT =  '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]
        
        if HYPE_E_DOT in requirement: 
            requirement.remove(HYPE_E_DOT)
setup(

name= "mlproject",
version = "1.0.0",
author= "Shubh",
author_email= "joshishubh4112003@gmail.com",
packages= find_packages(),
install_requires  = get_requirements('requirements.txt'),



)
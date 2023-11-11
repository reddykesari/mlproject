from setuptools import find_packages,setup
from typing import List
ignore='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        if ignore in requirements:
            requirements.remove(ignore)

    return requirements
setup(
    name="MLPROJECT",
    version='0.0.1',
    author="LKreddy",
    author_mail="lkreddykesari@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')

)
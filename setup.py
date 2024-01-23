from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
        
    return requirments


setup(
    name='mlproject',
    version='0.0.1',
    author='mohammed',
    author_email='mohammed@calicoai.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn'],
)


# setup.py
from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    requirements = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
    name='RegComplyAI',
    version='0.0.1',
    author='Esmaeil Rezaei',
    author_email='ishmaelrezaei@gmail.com',
    description='A Retrieval-Augmented Generation (RAG) model for regulatory compliance in healthcare',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.9",
)

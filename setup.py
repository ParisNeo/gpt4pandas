from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gpt4pandas',
    version='0.2',
    packages=find_packages(),
    license='Apache License 2.0',
    description='A tool that uses the GPT4ALL language model and the Pandas library to answer questions about dataframes',
    author='ParisNeo (Saifeddine ALOUI)',
    author_email='aloui.seifeddine@gmail.com',
    keywords='pandas GPT4ALL QA',
    install_requires=[
        'pandas',
        'transformers',
        'pyllamacpp==2.1.1'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

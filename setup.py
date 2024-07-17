from setuptools import setup, find_packages

setup(
    name='dok2any',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'openbabel',
    ],
    entry_points={
        'console_scripts': [
            'dok2any = dok2any.converter:main',
        ],
    },
    author='Dulaj Ramanayaka',
    author_email='dulajnr97git@gmail.com',
    description='Convert DOK files to various chemical structure formats using Open Babel.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dulaanr97/dok2any',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

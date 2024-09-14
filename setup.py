from setuptools import setup, find_packages

setup(
    name='mernmaker',
    version='1.1',
    packages=find_packages(), 
    package_data={
        'mernmaker': ['templates/*'], 
    },
    entry_points={
        'console_scripts': [
            'mernmaker=mernmaker.main:main', 
        ],
    },
    include_package_data=True,
)

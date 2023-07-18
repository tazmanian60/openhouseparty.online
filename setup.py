from setuptools import find_packages, setup

setup(
    name='flaskrOpenHousePartyWebsite',
    version='1.0.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
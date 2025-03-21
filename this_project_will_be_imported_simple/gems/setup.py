
from setuptools import setup, find_packages
setup(
    name = 'this_project_will_be_imported_simple',
    version = '0.0.1',
    packages = ['this_project_will_be_imported_simple'],
    package_dir = {'this_project_will_be_imported_simple': '.'},
    description = '',
    install_requires = [],
)


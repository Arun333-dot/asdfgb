from setuptools import setup, find_packages
setup(
    name = 'ghj',
    version = '1.0',
    packages = find_packages(include = ('ghj*', )) + ['prophecy_config_instances.ghj'],
    package_dir = {'prophecy_config_instances.ghj' : 'configs/resources/ghj'},
    package_data = {'prophecy_config_instances.ghj' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.49'],
    entry_points = {
'console_scripts' : [
'main = ghj.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)

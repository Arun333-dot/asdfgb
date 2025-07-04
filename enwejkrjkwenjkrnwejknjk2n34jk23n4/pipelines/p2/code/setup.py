from setuptools import setup, find_packages
setup(
    name = 'p2',
    version = '1.0',
    packages = find_packages(include = ('p2*', )) + ['prophecy_config_instances.p2'],
    package_dir = {'prophecy_config_instances.p2' : 'configs/resources/p2'},
    package_data = {'prophecy_config_instances.p2' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.4'],
    entry_points = {
'console_scripts' : [
'main = p2.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)

from setuptools import setup, find_packages

setup(
    name = 'week2_fib',
    version = '0.1',
    packages = find_packages()
) # do not forget ',' comma, and name = package name
# 🆘 setup must be in the top level of the package
# gitignore file will ignore .egg_info
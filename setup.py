from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIREMENTS = [x.strip() for x in f.readlines() if x.strip()]

setup(
    name='find_imdb',
    version='0.1',
    license='MIT',
    author="famgz",
    author_email='famgz@proton.me',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='https://github.com/famgz/find_imdb',
    install_requires=REQUIREMENTS
)

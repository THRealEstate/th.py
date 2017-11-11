import re
from setuptools import setup

# Influence for this inspired by https://goo.gl/Pi51aC
version = None
for line in open('./threalestate/__init__.py'):
  m = re.search('__version__\s*=\s*(.*)', line) # pylint: disable=W1401
  if m:
    version = m.group(1).strip()[1:-1]  # quotes
    break
assert version

setup(
    name='threalestate.py',
    version=version,
    description='TH Real Estates Core Modules',
    author='Ilan Filonneko',
    author_email='ilan.filonenko@tiaa.org',
    url='https://github.com/THRealEstate/threalestate.py',
    license='MIT',
    packages=['threalestate'],
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=[
        'Flask',
        'mysql-connector==2.1.4',
        'redis'
    ],
    tests_require=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ]
)

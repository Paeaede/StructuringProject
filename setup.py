from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funniest',
    version='0.1',
    description='The funniest joke in the world',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Linguistic', # for full list of classidiers, see: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='funniest joke comedy flying circus',
    url='http://github.com/storborg/funniest',
    author='Patrick Reiser',
    author_email='p.reiser91@web.de',
    license='MIT',
    packages=['funniest'],
    install_requires=['markdown',
                    ], # also possibly if not on pypi: dependency_links=['...']
    test_suite='nose.collector',
    tests_require=['nose'], # allows to just say python setup.py test
    scripts=['bin/funniest-joke'] # declare the script for commandline tool # when installing package -> setuptools copies script to path -> available for general use
    zip_safe=False)

# -> now we can already pip install package via navigating to folder and pip install .
# cd c:\dev\Daten_Patrick_noGit\Projekte\StructuringProject
# -> anywhere else in system using same python we can now "import funniest"

# making it available on PyPI after registring: python setup.py register
# upload source distribution -> installation wo cloning repo python setup.py sdist -> creates dist folder
# all steps together (update metadata, publish new buld) python setup.py register sdist upload

# after adding dependencies: python setup.py develop # afterwards, calling pip install unniest also installs markdown

# MANIFEST.in # ->  necessary to tell setuptools to include README.rst when generating source distributions

# Tests:
# best way to keep tests going is "Nose" -> run tests using "nosetest" from root of repository

# adding funniest-joke commandline tool:
# alterative to scripts -> using entry-points https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
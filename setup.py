'''
Setup script.
To install lizard:
[sudo] python setup.py install
'''

import pycoords_lib
from setuptools import setup, find_packages
import os

def install(appname):

    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fobj:
        readme = fobj.read()

    setup(
          name = appname,
          version = pycoords.VERSION,
          description = ''' A code analyzer without caring the C/C++ header files.
It works with Java, C/C++, JavaScript, Python, Objective C. Metrics includes cyclomatic complexity number etc.''',
          long_description =  readme,
          url = 'https://github.com/terryyin/pycoords',
          download_url='https://pypi.python.org/pycoords/',
          license='MIT',
          platforms='any',
          classifiers = ['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Developers',
                     'Intended Audience :: End Users/Desktop',
                     'License :: Freeware',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Quality Assurance',
                     'Programming Language :: C',
                     'Programming Language :: C++',
                     'Programming Language :: Java',
                     'Programming Language :: JavaScript',
                     'Programming Language :: Objective C',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3'],
          packages = ['pycoords_lib'],
          #py_modules = ['pycoords'],
          author = 'Terry Yin',
          author_email = 'terry@odd-e.com',
          scripts = ['pycoords.bat', 'pycoords']
          )

if __name__ == "__main__":
    import sys
    install('pycoords')

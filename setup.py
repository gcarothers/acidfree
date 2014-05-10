from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
with codecs.open('DESCRIPTION.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="acidfree",
    version=find_version('acidfree', '__init__.py'),
    description="Publish, Share, Archive YOUR photos",
    long_description=long_description,

    # The project URL.
    url='https://github.com/gcarothers/acidfree',

    # Author details
    author='Gavin Carothers',
    author_email='gavin@carothers.name',

    # Choose your license
    license='Apache',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Archiving',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',        
    ],

    # What does your project relate to?
    keywords='photos archive',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages.
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed.
    install_requires = ['requests',
                        'waitress',
                        'pyramid'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'acidfree=acidfree:main',
        ],
    },
)
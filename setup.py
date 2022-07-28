# Filename: setup.py

import sys
from os.path import join as pjoin
from pathlib import Path

from setuptools import setup, Extension

import pyeda

NAME = pyeda.__name__

VERSION = pyeda.__version__

AUTHOR = "Chris Drake"

AUTHOR_EMAIL = "cjdrake AT gmail DOT com"

DESCRIPTION = "Python Electronic Design Automation"

KEYWORDS = [
    "binary decision diagram",
    "Boolean algebra",
    "Boolean satisfiability",
    "combinational logic",
    "combinatorial logic",
    "computer arithmetic",
    "digital arithmetic",
    "digital logic",
    "EDA",
    "electronic design automation",
    "Espresso",
    "Espresso-exact",
    "Espresso-signature",
    "logic",
    "logic minimization",
    "logic optimization",
    "logic synthesis",
    "math",
    "mathematics",
    "PicoSAT",
    "SAT",
    "satisfiability",
    "truth table",
    "Two-level logic minimization",
    "Two-level logic optimization",
]

with open('README.rst') as fin:
    README = fin.read()

with open('LICENSE') as fin:
    LICENSE = fin.read()

URL = "https://github.com/cjdrake/pyeda"

DOWNLOAD_URL = "https://pypi.python.org/packages/source/p/pyeda"

CLASSIFIERS = [
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
]

PYEDA_PKGS = [
    'pyeda',
    'pyeda.boolalg',
    'pyeda.logic',
    'pyeda.parsing',
]

TEST_PKGS = [
    'pyeda.test',
    'pyeda.boolalg.test',
    'pyeda.logic.test',
    'pyeda.parsing.test',
]

PACKAGES = PYEDA_PKGS + TEST_PKGS

# Espresso extension
ESPRESSO = dict(
    define_macros = [],
    include_dirs = [
        pjoin('thirdparty', 'espresso', 'src'),
    ],
    sources = [
        pjoin('thirdparty', 'espresso', 'src', 'cofactor.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cols.c'),
        pjoin('thirdparty', 'espresso', 'src', 'compl.c'),
        pjoin('thirdparty', 'espresso', 'src', 'contain.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cubestr.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cvrin.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cvrm.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cvrmisc.c'),
        pjoin('thirdparty', 'espresso', 'src', 'cvrout.c'),
        pjoin('thirdparty', 'espresso', 'src', 'dominate.c'),
        pjoin('thirdparty', 'espresso', 'src', 'espresso.c'),
        pjoin('thirdparty', 'espresso', 'src', 'essen.c'),
        pjoin('thirdparty', 'espresso', 'src', 'exact.c'),
        pjoin('thirdparty', 'espresso', 'src', 'expand.c'),
        pjoin('thirdparty', 'espresso', 'src', 'gasp.c'),
        pjoin('thirdparty', 'espresso', 'src', 'gimpel.c'),
        pjoin('thirdparty', 'espresso', 'src', 'globals.c'),
        pjoin('thirdparty', 'espresso', 'src', 'hack.c'),
        pjoin('thirdparty', 'espresso', 'src', 'indep.c'),
        pjoin('thirdparty', 'espresso', 'src', 'irred.c'),
        pjoin('thirdparty', 'espresso', 'src', 'matrix.c'),
        pjoin('thirdparty', 'espresso', 'src', 'mincov.c'),
        pjoin('thirdparty', 'espresso', 'src', 'opo.c'),
        pjoin('thirdparty', 'espresso', 'src', 'pair.c'),
        pjoin('thirdparty', 'espresso', 'src', 'part.c'),
        pjoin('thirdparty', 'espresso', 'src', 'primes.c'),
        pjoin('thirdparty', 'espresso', 'src', 'reduce.c'),
        pjoin('thirdparty', 'espresso', 'src', 'rows.c'),
        pjoin('thirdparty', 'espresso', 'src', 'set.c'),
        pjoin('thirdparty', 'espresso', 'src', 'setc.c'),
        pjoin('thirdparty', 'espresso', 'src', 'sharp.c'),
        pjoin('thirdparty', 'espresso', 'src', 'sminterf.c'),
        pjoin('thirdparty', 'espresso', 'src', 'solution.c'),
        pjoin('thirdparty', 'espresso', 'src', 'sparse.c'),
        pjoin('thirdparty', 'espresso', 'src', 'unate.c'),
        pjoin('thirdparty', 'espresso', 'src', 'verify.c'),
        pjoin('pyeda', 'boolalg', 'espressomodule.c'),
    ],
)

# exprnode C extension
EXPRNODE = dict(
    define_macros = [
        ('NDEBUG', None),
    ],
    include_dirs = [
        Path('extension', 'boolexpr').as_posix(),
    ],
    sources = [
        Path('extension', 'boolexpr', 'argset.c').as_posix(),
        Path('extension', 'boolexpr', 'array.c').as_posix(),
        Path('extension', 'boolexpr', 'binary.c').as_posix(),
        Path('extension', 'boolexpr', 'boolexpr.c').as_posix(),
        Path('extension', 'boolexpr', 'bubble.c').as_posix(),
        Path('extension', 'boolexpr', 'compose.c').as_posix(),
        Path('extension', 'boolexpr', 'dict.c').as_posix(),
        Path('extension', 'boolexpr', 'flatten.c').as_posix(),
        Path('extension', 'boolexpr', 'nnf.c').as_posix(),
        Path('extension', 'boolexpr', 'product.c').as_posix(),
        Path('extension', 'boolexpr', 'set.c').as_posix(),
        Path('extension', 'boolexpr', 'simple.c').as_posix(),
        Path('extension', 'boolexpr', 'util.c').as_posix(),
        Path('extension', 'boolexpr', 'vector.c').as_posix(),
        Path('pyeda', 'boolalg', 'exprnodemodule.c').as_posix(),
    ],
    extra_compile_args = ['--std=c99'],
)

# PicoSAT C extension
with open(pjoin('thirdparty', 'picosat', 'VERSION')) as fin:
    PICOSAT_VERSION = '"' + fin.read().strip() + '"'

PICOSAT = dict(
    define_macros = [
        ('NDEBUG', None),
    ],
    include_dirs = [
        pjoin('thirdparty', 'picosat'),
    ],
    sources = [
        pjoin('thirdparty', 'picosat', 'picosat.c'),
        pjoin('pyeda', 'boolalg', 'picosatmodule.c'),
    ],
)

if sys.platform == 'win32':
    PICOSAT['define_macros'] += [
        ('NGETRUSAGE', None),
        ('inline', '__inline'),
    ]

EXT_MODULES = [
    Extension('pyeda.boolalg.espresso', **ESPRESSO),
    Extension('pyeda.boolalg.exprnode', **EXPRNODE),
    Extension('pyeda.boolalg.picosat', **PICOSAT),
]

SCRIPTS = [
    pjoin('script', 'espresso'),
    pjoin('script', 'picosat'),
]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    keywords=KEYWORDS,
    long_description=README,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
    packages=PACKAGES,
    ext_modules=EXT_MODULES,
    scripts=SCRIPTS,

    test_suite='nose.collector',
)


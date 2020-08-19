import setuptools


classifiers = [
    (
        "Programming Language :: Python :: %s" % x
    )
    for x in "3.7".split()
]


setuptools.setup(
    name="types101",
    description="Bidirectional type checker for simply typed lambda calculus.",
    version="0.0.1",
    license="MIT license",
    platforms=["unix", "linux", "osx", "win32"],
    author="magniff",
    url="https://github.com/magniff/types101",
    classifiers=classifiers,
    packages=[
        "types101",
    ],
    install_requires=[
        "funcparserlib"
    ],
    zip_safe=False,
)

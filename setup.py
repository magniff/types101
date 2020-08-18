import setuptools


classifiers = [
    (
        "Programming Language :: Python :: %s" % x
    )
    for x in "3.1 3.2 3.3 3.4 3.5 3.6 3.7".split()
]


setuptools.setup(
    name="types101",
    description="A stupid monadic fields tracker.",
    version="0.2.6",
    license="MIT license",
    platforms=["unix", "linux", "osx", "win32"],
    author="magniff",
    url="https://github.com/magniff/types101",
    classifiers=classifiers,
    packages=[
        "types101",
    ],
    zip_safe=False,
)

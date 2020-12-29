from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="prawvents",
    version="0.1",
    description="A Small wrapper for PRAW that allows for Event-based bots",
    long_description=readme(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    url="http://github.com/laundmo/prawvents",
    author="Laurin Schmidt",
    author_email="laurinschmidt2001@gmail.com",
    license="MIT",
    packages=["prawvents"],
    keywords="prawvents praw reddit api wrapper",
    install_requires=["praw"],
    zip_safe=False,
)

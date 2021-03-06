from distutils.core import setup
import setuptools

setup(
    name="feelingtweets",
    version="1.0.3",
    license="MIT",
    description="A dsitributed modules to collect/clean/translate and analize with Rule-based methods (Texblob and VADER)",
    author="Willy Carreño",
    author_email="dev.willct@gmail.com",
    url="https://github.com/dev-willcode/feelingtweets",
    download_url="https://github.com/dev-willcode/feelingtweets/archive/refs/tags/v1.0.3.tar.gz",
    keywords=["Sentimental", "Analysis", "Textblob", "VADER", "PNL"],
    python_requires=">=3.6.0",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
        "vaderSentiment",
        "textblob",
        "googletrans==4.0.0rc1",
        "nest_asyncio",
    ],
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Education",
                 "Intended Audience :: End Users/Desktop",
                 "License :: OSI Approved :: MIT License",
                 "Topic :: Education",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.6"],
)

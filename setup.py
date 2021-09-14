
from distutils.core import setup
setup(
    name='feelingtweets',
    packages=['feelingtweets'],
    version='0.0.1',
    license='MIT',
    description='A dsitributed modules to collect/clean/translate and analize with Rule-based methods (Texblob and VADER)',
    author='Willy Carreño',
    author_email='dev.willct@gmail.com',
    url='https://github.com/dev-willcode/feelingtweets',
    download_url='https://github.com/dev-willcode/feelingtweets/archive/refs/tags/v0.0.1.tar.gz',
    keywords=['Sentimental', "Analysis", 'Textblob', 'VADER', "PNL"],
    install_requires=[
        'googletrans',
        'vaderSentiment',
        'textblob',
        'pandas',
        'twint'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers, Data Scientist',
        'Topic :: Software Development :: Analysis Sentiments',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)

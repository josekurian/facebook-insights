from setuptools import setup, find_packages

setup(name='facebookinsights',
    description='A wrapper and command-line interface for the Facebook Insights API.',
    #long_description=open('README.rst').read(),
    author='Stijn Debrouwere',
    author_email='stijn@stdout.be',
    url='http://stdbrouw.github.com/facebook-insights/',
    download_url='http://www.github.com/stdbrouw/google-analytics/tarball/master',
    version='0.1.0',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics api wrapper facebook insights',
    scripts=[
        'bin/insights'
    ],
    install_requires=[
        'rauth', 
        'facepy', 
        'python-dateutil', 
        'addressable', 
        'flask', 
        'keyring', 
    ], 
    # test_suite='facebookinsights.tests', 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],
    )
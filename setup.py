from setuptools import setup, find_packages

setup(
    name='brainboost_data_source_requests_package',
    version='0.1.0',
    author='Pablo Tomas Borda',
    author_email='pablotomasborda@hotmail.com',
    description='Sends requests, accepts proxy lists, can use tor proxy',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package_name',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'tinydb==3.8.1'
        'requests==2.31.0',
        'schedule==1.2.1',
        'aiohttp==3.9.5'
        'search_engines @ git+https://github.com/PabloBorda/tools_goldenthinkerextractor.git@7bb819ba7398726876467d64bb777e28b4a9984d#egg=search_engines&subdirectory=Search-Engines-Scraper'
    ]
)

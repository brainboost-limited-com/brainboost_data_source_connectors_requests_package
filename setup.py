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
    python_requires='>=3.6',
    install_requires=[
        'dependency1',
        'dependency2',
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package_name.module_name:main_function',
        ],
    },
)

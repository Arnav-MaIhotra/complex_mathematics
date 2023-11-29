from setuptools import setup, find_packages


setup(
    name='complex_mathematics',
    version='4.17.10',
    packages=find_packages(),
    install_requires=[
        'numpy', 'scipy', 'matplotlib'
    ],
    license='MIT',
    author="Arnav Malhotra",
    author_email="amalhotra.business@gmail.com",
    description="Many complex math features.",
    long_description="Collection of numerical algorithms for algebra, statistics, machine learning, calculus, and more.",
    url="https://github.com/Arnav-MaIhotra/complex_mathematics",
)
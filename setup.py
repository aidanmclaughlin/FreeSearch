from setuptools import setup, find_packages

setup(
    name="freesearch",
    version="0.1.0",
    description="A UCI chess engine that evaluates positions based on move count difference",
    author="Devin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-chess>=1.10.0",
        "pytest>=7.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'freesearch=freesearch.__main__:main',
        ],
    },
)

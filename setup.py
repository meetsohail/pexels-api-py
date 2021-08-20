from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pexels-api-py",
    version="0.0.4",
    author="Sohail Ahmed",
    author_email="meetsohail360@gmail.com",
    description="Python API package for Pexels.com V1.",
    url="https://github.com/meetsohail/pexels-api-py",
    keywords='pexels, images, photos, copyright free',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)

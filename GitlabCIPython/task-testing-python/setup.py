from setuptools import setup, find_packages

setup(
    name="task-testing-python",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

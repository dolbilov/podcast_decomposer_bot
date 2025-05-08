from setuptools import find_packages, setup

setup(
    name="podcast_decomposer_bot",
    description="A tool for decomposing podcasts",
    author="Kirill Dolbilov",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

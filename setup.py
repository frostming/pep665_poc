from setuptools import setup, find_packages

setup(
    name="pep665_poc",
    version="0.0.1",
    install_requires=["resolvelib", "installer", "html5lib", "packaging", "tomlkit"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pep665-lock = pep665:lock_main"]},
)

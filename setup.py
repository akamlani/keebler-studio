from pathlib import Path

from setuptools import find_namespace_packages, setup

MODULE_NAME = "keebler"
INSTALL_NAME = f"{MODULE_NAME}-studio"


def get_version() -> str:
    "get module version"
    version_dict = {}
    with open(f"{MODULE_NAME}/version.py", encoding="utf-8") as fp:
        exec(fp.read(), version_dict)
    return ".".join(map(str, version_dict["__version__"]))


# read description for long-form description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# read requirements for core development installation
with open(Path("env").joinpath("requirements.txt"), "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if len(line) > 1 and "#" not in line]

# read requirements for core development installation
# pip install packagename[ui]
# pip install -e ".[all]"
extra = {}
files = [*Path("env").glob("**/requirements_*")]
etypes = [f.stem.split("_")[-1] for f in files]
for etype, filepath in zip(etypes, files):
    with open(filepath, "r", encoding="utf-8") as f:
        extra[etype] = [line.strip() for line in f if len(line) > 1 and "#" not in line]
# repackage information
extra["all"] = [item for sublist in extra.values() for item in sublist]

### development mode, symlinks and editable
# python setup.py develop
# pip    install -e .
setup(
    name=INSTALL_NAME,
    version=get_version(),
    description="studio suite",
    keywords="data, ml, ai, studio suite",
    license="MIT",
    author="Ari Kamlani",
    author_email="akamlani@gmail.com",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    # URIs
    url=f"https://github.com/akamlani/{INSTALL_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/akamlani/{INSTALL_NAME}/issues",
    },
    # long description
    long_description=long_description,
    long_description_content_type="text/markdown",
    # what is packaged here
    python_requires=">=3.7",
    install_requires=requirements,
    packages=find_namespace_packages(include=[f"{MODULE_NAME}.*"]),
    # additional packages
    extras_require=extra,
    # testing packages
    test_suite="tests",
    tests_require=extra["test"],
    # include perspective data
    include_package_data=True,
    package_data={MODULE_NAME: ["*.txt", "*.rst", "*.md"]},
)

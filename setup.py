import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()
requirements = [line.strip() for line in requirements]

setuptools.setup(
    name="talipp",
    version="0.1.0",
    author="nardew",
    author_email="cryptoxlib.aio@gmail.com",
    description="TALi++ - Incremental Technical Analysis Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nardew/talipp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    install_requires=requirements,
    python_requires='>=3.6.0',
)
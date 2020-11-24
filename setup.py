import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xltoy",
    version="0.1",
    author="Glauco Uri",
    author_email="glauco@uriland.it",
    description="bla bla",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/glaucouri/xltoy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
            'console_scripts': [
                'xltoy = scripts.cmd:cli'
          ]}
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smashgg.py",
    version="0.0.9",
    author="Brandon Cooke",
    author_email="brandoncookedev@gmail.com",
    description="Python SDK for smash.gg's public api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrandonCookeDev/smashgg.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
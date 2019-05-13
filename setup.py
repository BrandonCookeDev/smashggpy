import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smashggpy",
    version="0.0.17",
    author="Brandon Cooke",
    author_email="brandoncookedev@gmail.com",
    description="Python SDK for smash.gg's public api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrandonCookeDev/smashgg.py",
    packages=['smashggpy.util', 'smashggpy.models', 'smashggpy.queries', 'smashggpy.common'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="GNU Public License v3.0",
    keywords='smashgg smash.gg smashgg.py smashggpy sdk wrapper api gql graphql',
    python_requires='~=3.7',
)
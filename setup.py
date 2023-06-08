import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scalarnet",
    version="0.1.0",
    author="Mehdi Bukhari",
    author_email="mmmbukhari@gmail.com",
    description="Lightweight neural network library with a PyTorch-like API and efficient scalar autograd. Design, train, and evaluate scalar-focused models easily. Fast, flexible, and intuitive. Empower your scalar-valued tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MehdiBukhari/ScalarNet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

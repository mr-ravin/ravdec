import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravdec",
    version="3.3",
    author="Ravin Kumar",
    author_email="mr.ravin_kumar@hotmail.com",  # Make sure this is correct
    description="Ravdec - Lossless Data Compression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-ravin/ravdec",
    keywords=[
        'data compression', 'lossless compression', 'file compression',
        'text compression', 'efficient compression'
    ],
    license="MIT",
    python_requires=">=3.7",
    install_requires=[],  # Add dependencies if needed
    packages=setuptools.find_packages(include=["ravdec", "ravdec.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

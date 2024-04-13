import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MotionMySql",
    version="0.0.1",
    author="CasearF",
    author_email="casearx@gmail.com",
    description="Dynamically constructing add/delete/reference statements using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CasearF/MotionMySql",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

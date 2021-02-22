import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WotNotDataAccess",
    version="0.0.4",
    author="WotNot",
    author_email="wotnot@marutitech.com",
    description="This package will help to access WotNot data from redis and mysql",
    long_description=long_description,
    long_description_content_type="text",
    url="https://github.com/gaurang19990412/data-access-package-01/tree/development",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python >= 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=["PyMySQL==1.0.2", "redis==3.5.3", "rejson==0.5.4", "six==1.15.0", "pygelf==0.4.0"]
)

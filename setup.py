import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auth_py-jalbertcruz",
    version="0.0.1",
    author="José Albert Cruz Almaguer",
    author_email="jalbertcruz@gmail.com",
    description="GCE auth utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jgce-components/auth_py",
    install_requires=[
        'python-jwt>=3.3.0',
        'google-api-python-client>=1.11.0',
        'injector>=0.18.3',
        'requests>=2.24.0',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# learn-maintenance

### Project Status
![GitHub issues](https://img.shields.io/github/issues/cnerg/learn-maintenance)
![GitHub pull requests](https://img.shields.io/github/issues-pr/cnerg/learn-maintenance)

A repository for learning software maintenance and testing.

## Entry points
To install the package on your computer, run this in the learn-maintenance directory (where the setup.py file is located) 
```
pip install .
```
To use the entry point run this and add the appropriate arguments behind it
```
prog
```
If there are any PackageNotFoundErrors being thrown, try upgrading pip and setuptools
```
pip install --upgrade pip
pip install --upgrade setuptools
```

## Docker image
Open the Docker daemon by running this on a separate terminal
```
sudo dockerd
```
Build the Docker image by running
```
docker build --tag python-docker .
```



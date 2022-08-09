# learn-maintenance
A repository for learning software maintenance and testing

## Entry points
To install the package on your computer: 
```
pip install .
```
To use the entry point run "prog" and add the appropriate arguments behind it
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



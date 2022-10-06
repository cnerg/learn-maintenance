# syntax=docker/dockerfile:1

FROM scratch
ADD ubuntu-focal-oci-amd64-root.tar.gz /
CMD ["bash"]
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install numpy
RUN pip install -U pytest coverage
COPY . .

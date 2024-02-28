FROM amazonlinux:2023

RUN yum update -y
RUN yum install -y tar wget gzip gcc make zlib-devel openssl-devel bzip2-devel libffi-devel

RUN wget https://www.python.org/ftp/python/3.11.5/Python-3.11.5.tgz && \
    tar xzf Python-3.11.5.tgz && \
    cd Python-3.11.5 && \
    ./configure --enable-optimizations && \
    make altinstall

RUN /usr/local/bin/python3.11 --version

COPY . /api
WORKDIR /api

RUN /usr/local/bin/python3.11 -m venv env
RUN source env/bin/activate
RUN env/bin/pip install --no-cache-dir --upgrade --use-pep517 -r requirements.txt

WORKDIR $HOME/api/app
EXPOSE 5000
CMD ["../env/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
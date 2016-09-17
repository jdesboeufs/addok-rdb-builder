FROM python:3.5

RUN apt-get update
RUN apt-get -qy install git wget redis-tools

WORKDIR /app

RUN pip install cython
RUN pip install git+https://github.com/addok/addok
RUN pip install git+https://github.com/addok/addok-fr
RUN pip install git+https://github.com/addok/addok-france
RUN pip install git+https://github.com/addok/addok-trigrams

COPY local.py /app
COPY builder-cmd.sh /app

ENV ADDOK_CONFIG_MODULE /app/local.py
ENV REDIS_HOST redis

CMD ["./builder-cmd.sh"]

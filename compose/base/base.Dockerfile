FROM python:3.8.8

ENV PYTHONUNBUFFERED=0

# base utils
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
        wget \
        apt-utils \
    && rm -rf /var/lib/apt/lists/*

# poetry
RUN wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py \
            && python get-poetry.py --yes \
            && rm get-poetry.py
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

# dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

CMD ["python"]

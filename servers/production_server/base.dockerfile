FROM python:3.8

# default
ENV PYTHONUNBUFFERED=1

# dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# poetry
WORKDIR /project/utils/
RUN wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
    python get-poetry.py --yes && \
    rm get-poetry.py
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

CMD ["python"]

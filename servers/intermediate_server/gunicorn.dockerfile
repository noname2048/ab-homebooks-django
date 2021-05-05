FROM noname2048/ab_base:1.0

RUN apt-get update && apt-get install -y --no-install-recommends vim wget apt-utils

# poetry install
COPY homebooks/pyproject.toml /project/utils/
COPY homebooks/poetry.lock /project/utils/
RUN poetry install

# add and run
ADD homebooks /project/intermediate
WORKDIR /project/intermediate/
CMD ["gunicorn", "homebooks.wsgi:application", "--bind", "0.0.0.0:8000"]

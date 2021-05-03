# FROM base.dockerfile
FROM noname2048/ab_base:1.0

RUN apt-get update && apt-get install -y --no-install-recommends vim wget apt-utils

# poetry install
COPY homebooks/pyproject.toml /project/utils/
RUN poetry install

# add and run
ADD ./homebooks /project/development_stage
WORKDIR /project/development_stage/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

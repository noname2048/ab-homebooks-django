FROM noname2048/ab_python_base:1.0

# install packages
WORKDIR /app
COPY homebooks/pyproject.toml /app/
COPY homebooks/poetry.lock /app/
RUN poetry install

CMD ["/bin/bash"]

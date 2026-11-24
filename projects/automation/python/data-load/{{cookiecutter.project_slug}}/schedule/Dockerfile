FROM python:{{ cookiecutter._python_version }}-slim

WORKDIR /srv/app
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry poetry-plugin-export \
    && poetry export --without-hashes -o requirements.txt \
    && pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y poetry poetry-plugin-export
COPY app ./app
COPY data ./data

CMD ["python", "-m", "app"]

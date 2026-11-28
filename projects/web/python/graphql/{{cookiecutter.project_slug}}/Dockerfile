FROM python:{{ cookiecutter._python_version }}-slim AS build

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN pip install --no-cache-dir poetry

WORKDIR /srv
COPY pyproject.toml poetry.lock README.md ./
RUN poetry install --only main --no-root --no-interaction

FROM python:{{ cookiecutter._python_version }}-slim

ENV PATH="/srv/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN useradd --system --no-create-home app

WORKDIR /srv
COPY --from=build /srv/.venv ./.venv
COPY app ./app

USER app
ENV PORT=8000
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s \
    CMD python -c "import urllib.request as u; u.urlopen('http://127.0.0.1:' + __import__('os').environ['PORT'] + '/health')"

CMD ["sh", "-c", "exec uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]

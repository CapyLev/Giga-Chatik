FROM python:3.12-slim AS builder
WORKDIR /usr/src/app/

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/

COPY --from=builder /usr/src/app/requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /usr/src/app/src/
COPY config/ /usr/src/app/config/
COPY alembic.ini /usr/src/app/

CMD ["python", "-m", "src.main"]

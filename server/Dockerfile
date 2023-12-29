FROM python:3.12-slim AS base

RUN apt-get update \
    && apt-get install -y gcc libev4 libev-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app/

FROM base AS dev_req

COPY pyproject.toml poetry.lock /usr/src/app/

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

FROM base AS prod_req

COPY pyproject.toml poetry.lock /usr/src/app/

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

FROM base AS dev

COPY --from=dev_req /usr/src/app/requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY src/ /usr/src/app/src/
COPY config/ /usr/src/app/config/
COPY alembic.ini /usr/src/app/

FROM base AS prod

COPY --from=prod_req /usr/src/app/requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY src/ /usr/src/app/src/
COPY config/ /usr/src/app/config/
COPY alembic.ini /usr/src/app/

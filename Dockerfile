FROM --platform=linux/amd64 python:3.12.11-slim as base
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL authors="andre9308@hotmail.it"

RUN apt-get update && \
    apt-get install -y libpq-dev gcc libssl-dev curl && \
    apt-get install -y libhdf5-serial-dev libnetcdf-dev && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -g 999 aoc && \
    useradd -m -r -u 999 -g aoc aoc && \
    mkdir /aoc && \
    chown aoc /aoc

WORKDIR /aoc

FROM base as dependencies
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0
COPY --link pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable --no-dev

FROM base as runtime-base
ENV VIRTUAL_ENV=/aoc/.venv \
    PATH="/aoc/.venv/bin:$PATH"

COPY ./entrypoint.sh /aoc
COPY ./src /aoc/src

RUN chmod +x /aoc/entrypoint.sh
ENV PYTHONPATH="/aoc:$PYTHONPATH"
ENTRYPOINT ["/aoc/entrypoint.sh"]

FROM runtime-base as production
COPY --link --from=dependencies $VIRTUAL_ENV $VIRTUAL_ENV
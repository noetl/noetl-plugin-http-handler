FROM python:3.11.1-slim-buster
RUN apt-get update \
 && apt-get --no-install-recommends install -y build-essential libssl-dev libffi-dev cargo \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/usr/src"

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY ./src .

ENTRYPOINT ["python", "main.py"]


FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /code/

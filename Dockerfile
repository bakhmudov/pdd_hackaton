FROM python:3.11.3-alpine3.18
LABEL authors="bagatir"

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN \
 apk add --no-cache python3 postgresql-libs libxml2-dev libxslt-dev && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 pip install --upgrade pip && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ENTRYPOINT ["top", "-b"]
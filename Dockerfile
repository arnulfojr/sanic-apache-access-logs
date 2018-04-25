FROM python:3.6-alpine

RUN apk add --no-cache build-base git

ENV APP_DIR "/app"

ENV CONTAINER_PORT 5000

ENV PYTHONPATH "${APP_DIR}/src:${APP_DIR}/sanic_access_logs"

RUN pip install --upgrade pip

RUN pip install sanic

COPY . ${APP_DIR}

RUN pip install -r ${APP_DIR}/requirements.txt

WORKDIR ${APP_DIR}/src

EXPOSE ${CONTAINER_PORT}

ENTRYPOINT ["python"]

CMD ["run.py"]

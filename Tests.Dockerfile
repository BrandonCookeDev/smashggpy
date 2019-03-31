FROM python:3.7

ENV APP_DIR /usr/src/app
WORKDIR ${APP_DIR}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./test ./test
RUN ls -R
CMD [ "python", "./test/util/TokenHandler.test.py" ]
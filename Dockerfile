FROM python:3.11.15-trixie AS developer

WORKDIR /usr/src/app

COPY . .

RUN pip install .

CMD ["live_view"]

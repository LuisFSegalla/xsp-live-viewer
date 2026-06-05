FROM python:3.11.15-trixie AS developer

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install .

CMD ["live_view"]

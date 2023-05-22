FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV allowNewKeys true

EXPOSE 3400

#RUN mkdir /app/data
VOLUME /app/data

CMD ["python", "app.py"]

# label section
LABEL org.opencontainers.image.source https://github.com/HSoeren/everything-is-a-metric
LABEL org.opencontainers.image.authors="Soeren Helms <soeren.helms@repronik.it>"
LABEL org.opencontainers.image.description="Prometheus Exporter for custom metrics"
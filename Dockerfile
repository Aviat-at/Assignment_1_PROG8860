
FROM python:3.10-alpine AS builder
WORKDIR /app
COPY requirements.txt /app/
RUN apk add --no-cache \
    gcc musl-dev python3-dev libffi-dev postgresql-dev && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt
FROM python:3.10-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . /app
EXPOSE 8000


# Set a proper entrypoint for flexibility
ENTRYPOINT ["sh", "-c"]
CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

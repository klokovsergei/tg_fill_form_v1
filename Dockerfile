FROM python:3.12

RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /app/database && \
    chmod -R 775 /app/database

USER appuser

CMD ["python", "main.py"]
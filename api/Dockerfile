FROM python:3.9

ENV PYTHONPATH=.
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.9

WORKDIR /app

RUN pip install --no-cache-dir -r requirement.txt

COPY . /app/

CMD ["python", "test.py"]


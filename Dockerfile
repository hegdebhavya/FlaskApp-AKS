FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask
EXPOSE 5000
#ENV NAME World
CMD ["python", "app.py"]

FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN pytest test_core.py
EXPOSE 5000
CMD ["python", "app.py"]
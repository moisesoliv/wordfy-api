FROM python:latest
WORKDIR /app
COPY . /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN pytest test_core.py
EXPOSE 3000
CMD ["python", "app.py"]
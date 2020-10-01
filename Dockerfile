FROM python:latest
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
# CMD ['py.test']
EXPOSE 3000

CMD ["python","app.py"]
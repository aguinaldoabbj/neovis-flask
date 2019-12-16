#base image
FROM python:3.7
#copy app
COPY . /app
WORKDIR /app
#install dependencies
RUN pip install -r requirements.txt
#clone neovis
RUN git clone https://github.com/aguinaldoabbj/neovis.js static/neovis.js
#flask runs on 5000
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app/app.py"]

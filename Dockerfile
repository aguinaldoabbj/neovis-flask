FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN git clone https://github.com/aguinaldoabbj/neovis.js static/neovis.js
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app/app.py"]

#base image
#FROM python:3.7
FROM python:slim
#install dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install flask
#copy app
COPY neovis-flask-app /neovis-flask-app
#go to app workdir
WORKDIR /neovis-flask-app
#clone neovis project (cloning from an unstable branch)
RUN git clone --single-branch --branch 2.0.0 https://github.com/neo4j-contrib/neovis.js static/neovis.js \
    && cp -rf static/neovis.js/examples templates/neovis.js-examples
#RUN git clone https://github.com/neo4j-contrib/neovis.js static/neovis.js
#put neovis examples in templates
#RUN mkdir -p templates/neovis.js-examples
#COPY static/neovis.js/examples/* templates/neovis.js-examples/
#flask runs on 5000
EXPOSE 5000
ENTRYPOINT ["python"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["app.py"]

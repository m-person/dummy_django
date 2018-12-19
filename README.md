# dummy_django
The dummy Django site for deployment experiments

Warning: some conf files can be insufficient or broken! This repo cannot be used as is!


## some repository content:
##### AWS CodeBuild (clasic way):
file: buildspec-prod-provisioning-app.yml

performed actions:
- launch instance
- run unit tests
- zip sources and put them to s3

#### Run whole environment using Docker Compose:
contains:
- django+gunicorn as web server
- django-q as worker
- nginx as reverse proxy
- mysql db
- elasticsearch

files: deploy/docker/*
 

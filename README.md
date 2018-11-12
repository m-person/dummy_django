# dummy_django
The dummy Django site for deployment experiments

Warning: some conf files can be insufficient or broken! This repo is not intended to be used as is in any deployments.


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

Note: the docker-compose doesn't build the web and worker images. They are created on the previous stage (manually or using CodeBuild) and pushed to a docker registry. 
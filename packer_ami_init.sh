#!/usr/bin/env sh

export DEBIAN_FRONTEND=noninteractive

sudo apt-get update

sudo apt-get install -y mysql-client mc git libmysqlclient-dev python3-dev python3-pip python3-setuptools python3-venv nginx
sudo apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk


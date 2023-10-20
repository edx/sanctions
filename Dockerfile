FROM ubuntu:focal as app
MAINTAINER sre@edx.org


# Packages installed:

# language-pack-en locales; ubuntu locale support so that system utilities have a consistent
# language and time zone.

# python; ubuntu doesnt ship with python, so this is the python we will use to run the application

# python3-pip; install pip to install application requirements.txt files

# libmysqlclient-dev; to install header files needed to use native C implementation for
# MySQL-python for performance gains.

# libssl-dev; # mysqlclient wont install without this.

# python3-dev; to install header files for python extensions; much wheel-building depends on this

# gcc; for compiling python extensions distributed with python packages like mysql-client

# If you add a package here please include a comment above describing what it is used for
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qy install --no-install-recommends \
 language-pack-en locales \
 python3.8 python3-dev python3-pip \
 # The mysqlclient Python package has install-time dependencies
 libmysqlclient-dev libssl-dev pkg-config \
 gcc \
 build-essential \
 git \
 wget


RUN pip install --upgrade pip setuptools
# delete apt package lists because we do not need them inflating our image
RUN rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DJANGO_SETTINGS_MODULE sanctions.settings.production

EXPOSE 18770
EXPOSE 18771
RUN useradd -m --shell /bin/false app

WORKDIR /edx/app/sanctions

# Copy the requirements explicitly even though we copy everything below
# this prevents the image cache from busting unless the dependencies have changed.
COPY requirements/production.txt /edx/app/sanctions/requirements/production.txt

# Dependencies are installed as root so they cannot be modified by the application user.
RUN pip install -r requirements/production.txt

RUN mkdir -p /edx/var/log

# Code is owned by root so it cannot be modified by the application user.
# So we copy it before changing users.
USER app

# Gunicorn 19 does not log to stdout or stderr by default. Once we are past gunicorn 19, the logging to STDOUT need not be specified.
CMD gunicorn --workers=2 --name sanctions -c /edx/app/sanctions/sanctions/docker_gunicorn_configuration.py --log-file - --max-requests=1000 sanctions.wsgi:application

# This line is after the requirements so that changes to the code will not
# bust the image cache
COPY . /edx/app/sanctions

FROM app as devstack
USER root
COPY requirements/dev.txt /edx/app/sanctions/requirements/dev.txt
RUN pip install -r requirements/dev.txt
USER app
CMD gunicorn --workers=2 --name sanctions -c /edx/app/sanctions/sanctions/docker_gunicorn_configuration.py --log-file - --max-requests=1000 sanctions.wsgi:application

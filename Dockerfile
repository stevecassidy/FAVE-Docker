#
# HTK (Hidden Markov Model Toolkit) Docker
# v3.4.1
# @author Loreto Parisi (loretoparisi at gmail dot com)
# v1.0.0
#
# Copyright (c) 2017 Loreto Parisi - https://github.com/loretoparisi/docker
#
#  Exteneded to add FAVE by Steve Cassidy <Steve.Cassidy@mq.edu.au>
#

FROM ubuntu:22.04

# working directory
ENV HOME /root
WORKDIR $HOME

# packages list
RUN \
	apt-get update && apt-get install -y \
    libc6-dev-i386 \
    libx11-dev \
    gawk \
    python3-dev \
    python3-pip \
    python2.7 \
    curl \
    git \
    sox \
    praat

# pip
RUN pip3 install --upgrade pip

RUN mkdir $HOME/htk
COPY ./htk $HOME/htk
WORKDIR $HOME/htk/
RUN ./configure --disable-hslab && \
    make all && \
    make install

# now FAVE
RUN mkdir $HOME/FAVE
COPY ./FAVE $HOME/FAVE
WORKDIR $HOME/FAVE

# get Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
RUN ~/.poetry/bin/poetry install


CMD ["bash"]

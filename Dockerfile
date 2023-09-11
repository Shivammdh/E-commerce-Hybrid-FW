#FROM python:3.10-slim-buster as base
#
### start builder stage.
#
## this is the first stage of the build.
## it will install all requirements.
#FROM base as builder
#
## Update the package manager's package list
#RUN apt-get update
#
## Install wget to download the Chrome browser package
#RUN apt-get install -y wget
## Install the required dependencies for Google Chrome
#RUN apt-get install -y \
#    fonts-liberation \
#    libappindicator3-1 \
#    xdg-utils \
#    libxss1 \
#    libasound2
#
## Download and install the latest Chrome browser package
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN dpkg -i google-chrome-stable_current_amd64.deb
#
## Cleanup to reduce the image size (optional)
#RUN rm google-chrome-stable_current_amd64.deb
#
## copy any python requirements file into the install directory and install all python requirements.
#RUN mkdir /app
#WORKDIR /app
#COPY requirements.txt /app/
#RUN pip install --upgrade --no-cache-dir -r requirements.txt
##RUN rm /requirements.txt # remove requirements file from container.
#
## copy the source code into /app and move into that directory.
#
#
#COPY . /app/
### end builder stage.
#
######
#
### start base stage.
#
## this is the image this is run.
#FROM builder
# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package manager's package list
RUN apt-get update

# Install Python and pip
RUN apt-get install -y python3 python3-pip

# Install Google Chrome and its dependencies
RUN apt-get install -y wget unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get install -f -y

# Install Selenium

# Cleanup to reduce image size
RUN rm google-chrome-stable_current_amd64.deb
RUN apt-get clean

# Copy your Selenium Python script into the container
COPY . /app

# Set the working directory
WORKDIR /app
RUN pip install --upgrade --no-cache-dir -r requirements.txt
#CMD ["/bin/bash"]
# default entry point.
CMD ["python","-m","Utilites.PassArgument"]
## end base stage.
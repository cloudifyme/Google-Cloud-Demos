# Sets the base image for subsequent instructions
FROM ubuntu:22.04
# Sets the working directory in the container  


ENV APP_TEMPLATES /app/templates
RUN mkdir -p "$APP_TEMPLATES"

WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev curl

# Copies the html to the template directory
COPY templates/base.html "$APP_TEMPLATES"
COPY templates/index.html "$APP_TEMPLATES"
COPY templates/result.html "$APP_TEMPLATES"

# Copies the dependency files to the working directory
COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip3 install -r requirements.txt
# Copies everything to the working directory
COPY . /app
# Command to run on container start    
CMD [ "python3" , "./main.py" ]
EXPOSE 5000

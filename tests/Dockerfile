FROM python:3.10.0b2-buster

#Make a directory
WORKDIR /tests

#Install Dependencies
COPY requirement.txt .
RUN pip3 install -r requirement.txt
#Copy the source code
COPY . /tests
#Run the application
CMD ["python", "run.py"]
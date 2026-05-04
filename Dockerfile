#Base: verison of Python
FROM python:3.11-slim

#Workspace: a folder inside the container 
WORKDIR /code

#The dependencies that are needed
COPY ./requirements.txt /code/requirements.txt

#Install the python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#Copying the actual code of the application files into the container
COPY ./app /code/app
COPY ./main.py /code/main.py

#The port: tells the container to open a port so outside traffic can get in
EXPOSE 8000

#Exact terminal command to start the server when the container boots
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
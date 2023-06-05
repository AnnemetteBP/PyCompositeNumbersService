FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# Create the directory for the container
RUN mkdir -p /code
WORKDIR /code
#RUN cd /code
COPY requirements.txt ./requirements.txt
# Upgrade PIP and Cython
RUN pip install --upgrade pip
RUN pip install --upgrade cython
#RUN python.exe rabbitmqadmin
# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ code/app
EXPOSE 5000
# Run by specifying the host and port
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--reload", "--port", "5000"]
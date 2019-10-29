FROM python:3.6.5-slim
LABEL maintainer="Component-Based Software Development"
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]

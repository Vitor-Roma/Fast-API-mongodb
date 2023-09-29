FROM python:3.11.1

WORKDIR /usr/src/app
COPY ./ /usr/src/app

RUN pip install --upgrade pip --user
RUN pip3 install -r requirements.txt

#EXPOSE 80

#RUN ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
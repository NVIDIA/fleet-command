FROM python:3.7

COPY . ./
#COPY azure-send-message.py  .

RUN pip3 install -r requirements.txt

ENTRYPOINT python azure-send-message-deviceto-cloud.py

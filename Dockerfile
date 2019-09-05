FROM python:3

ADD geocode.py /

RUN pip install httplib2

CMD [ "python", "./geocode.py" ]
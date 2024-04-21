FROM python:3.11
WORKDIR /assginment11
COPY . /assginment11
RUN pip install NLTK 
RUN pip install punkt
CMD [ "python" , "main.py" ]



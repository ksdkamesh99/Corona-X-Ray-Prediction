FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python","app.py"]

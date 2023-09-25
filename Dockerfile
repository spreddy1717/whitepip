FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /whitepip  

COPY requirements.txt /whitepip/

RUN pip install -r requirements.txt

COPY . /whitepip/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
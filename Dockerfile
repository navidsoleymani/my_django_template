FROM python:3.11

WORKDIR /proj

COPY proj/requirements.txt ./


RUN pip install --upgrade pip
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com


COPY proj/SAMPLE_ENV.txt ./.env

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
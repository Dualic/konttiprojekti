FROM python:3
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
CMD [ "flask",  "run",  "--host=0.0.0.0",  "--port=80",  "--reload" ]
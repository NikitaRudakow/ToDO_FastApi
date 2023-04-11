FROM python
WORKDIR .
COPY . .
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
CMD [ "uvicorn","main:app"]

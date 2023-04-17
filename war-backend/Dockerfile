FROM python:3.7
EXPOSE 4000
RUN mkdir /war
WORKDIR /war
COPY requirements.txt /war/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD ["./wait-for-it.sh", "war-db:3306", "-t", "60", "--", "python3", "app.py"]
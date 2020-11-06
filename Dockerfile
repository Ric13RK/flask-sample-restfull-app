FROM python:3.9

# ENV FLASK_APP_DATABASE_URL=mysql+pymysql:username:password@url:port/database
# ENV FLASK_APP_SQLALCHEMY_TRACK_MODIFICATIONS=False
# ENV FLASK_APP_PROPAGATE_EXCEPTIONS=True
# ENV FLASK_APP_JWT_SECRET_KEY=Rishi
# ENV FLASK_APP_JWT_BLACKLIST_ENABLED=True

RUN apt-get -qq update
RUN python3 -m pip install --upgrade pip

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000/tcp
CMD python ./app.py

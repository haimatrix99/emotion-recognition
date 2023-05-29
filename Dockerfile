FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN useradd --user-group --create-home --shell /bin/bash app
USER app

WORKDIR /app
COPY --chown=app:app . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80 443

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]

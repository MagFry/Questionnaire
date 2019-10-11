FROM python:3.7.2

RUN pip3.7 install django djangorestframework psycopg2 psycopg2-binary requests django-cors-headers

COPY website-run.sh /usr/bin/website-run.sh
RUN chmod +x /usr/bin/website-run.sh

ENTRYPOINT ["bash"]
EXPOSE 8000
CMD ["-c", "website-run.sh"]

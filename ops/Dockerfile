FROM python:3.7.2

RUN pip3.7 install django psycopg2 psycopg2-binary requests django-cors-headers testinfra==3.2.0

COPY website-run.sh /usr/bin/website-run.sh
RUN chmod +x /usr/bin/website-run.sh

ENTRYPOINT ["bash"]
EXPOSE 8000
CMD ["-c", "website-run.sh"]

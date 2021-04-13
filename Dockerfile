FROM ubuntu:focal

RUN apt-get update && apt-get install --yes gettext-base nginx

# Copy over files
WORKDIR /srv
ADD entrypoint entrypoint
ADD index.template index.template
ADD nginx.conf /etc/nginx/sites-enabled/default

STOPSIGNAL SIGTERM

ENTRYPOINT ["./entrypoint"]

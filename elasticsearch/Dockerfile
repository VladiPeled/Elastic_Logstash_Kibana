FROM docker.elastic.co/elasticsearch/elasticsearch:7.1.1

COPY --chown=elasticsearch:elasticsearch monitoring.sh /usr/share/elasticsearch/
RUN /usr/share/elasticsearch/monitoring.sh

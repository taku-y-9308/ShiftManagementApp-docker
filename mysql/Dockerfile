FROM mysql:8.0

ENV MYSQL_DATABASE=ShiftManagementApp \
  MYSQL_USER=docker-user \
  MYSQL_PASSWORD=docker-user \
  MYSQL_ROOT_PASSWORD=admin \
  TZ=Asia/Tokyo

COPY ./my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf
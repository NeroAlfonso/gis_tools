#docker build -t postgistools:1.0.0 .
FROM debian:11
RUN apt-get update
RUN apt-get install postgis -y
RUN mkdir /home/postgistools
WORKDIR /home/postgistools
RUN mkdir workspace
ENTRYPOINT "/bin/sh"

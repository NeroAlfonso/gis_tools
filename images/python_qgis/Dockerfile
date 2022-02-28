#docker build -t python_qgis:1.0.0 . --network=host
FROM qgis/qgis:latest
RUN pip3 install wradlib
RUN pip3 install numpy
RUN pip3 install pandas
RUN mkdir -p /app
WORKDIR /app
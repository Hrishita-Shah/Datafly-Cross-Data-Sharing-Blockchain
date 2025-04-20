FROM hyperledger/fabric-tools:2.5

WORKDIR /app

COPY load_fabric.py .
COPY shared ./shared

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir --upgrade pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip --no-install-recommends && \
    apt-get clean

CMD ["python3", "load_fabric.py"]



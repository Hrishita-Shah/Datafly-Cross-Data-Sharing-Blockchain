FROM python:3.10-slim
RUN pip install requests

WORKDIR /app

# Copy the transfer script from transfer/
COPY transfer/transfer.py .

# Copy the shared directory from the root
COPY shared ./shared

# Install Python dependencies (if any)
# RUN pip install -r requirements.txt

CMD ["python", "transfer.py"]

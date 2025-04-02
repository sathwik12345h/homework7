# Use official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY generate_qr.py .

# Install required package
RUN pip install qrcode[pil]

# Command to run the script when container starts
CMD ["python", "generate_qr.py"]
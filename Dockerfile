# Use an official Python runtime as the base image
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt . 

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY wordFrequency.py .
COPY paragraphs.txt .

# Set the command to run your script when the container starts
CMD ["python", "wordFrequency.py"]
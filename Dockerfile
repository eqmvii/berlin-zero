FROM python:3.11-slim

WORKDIR /app

# Install any needed dependencies
RUN pip install --no-cache-dir pathlib

# The code will be mounted as a volume
COPY wordcount.py /app/

# Make the script executable
RUN chmod +x /app/wordcount.py

# Run wordcount.py when the container launches
ENTRYPOINT ["python", "wordcount.py"]

# Default to scanning the /app directory
CMD ["/app"]

# Base image with Python
FROM python:3.11-slim
# Working folder inside the container
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy app.py into the image
COPY . .
EXPOSE 5000
# Command run when the container starts
CMD ["python", "app.py"]

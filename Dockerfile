# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies from your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create an uploads folder
RUN mkdir -p uploads

# The port your app runs on
EXPOSE 7860

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV PORT=7860

# Run the application
CMD ["python", "app.py"]
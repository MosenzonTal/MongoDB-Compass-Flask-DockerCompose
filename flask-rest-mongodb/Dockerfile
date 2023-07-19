# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install the Flask package
RUN pip install flask flask-pymongo


# Copy the entire project into the container
COPY . .

# Expose the port on which your Flask app will run (adjust if needed)
EXPOSE 5000

# Set the environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]



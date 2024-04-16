# Use the official Python image as the base image
FROM python:3.12.2

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser
USER myuser

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Set the PATH for the myuser user
ENV PATH="/home/myuser/.local/bin:${PATH}"

# Install the application dependencies
RUN pip install --user -r requirements.txt

# Expose the application port
EXPOSE 8000

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
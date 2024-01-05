# Use the official Python image as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Expose the port that the FastAPI application runs on
EXPOSE 80

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
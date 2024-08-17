# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Run Streamlit when the container starts
CMD ["streamlit", "run", "app.py"]

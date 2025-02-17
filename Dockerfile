# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements fiel first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Cop the entire project into the container
COPY . /app

# Expose port 8000 (the port uvicorn will listen on)
EXPOSE 8000

# Run the application using uvicorn
# Note: in production, it's typical to disable auto-reload
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
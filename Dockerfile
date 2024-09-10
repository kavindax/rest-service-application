
# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the application port
EXPOSE 8000

# Step 6: Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

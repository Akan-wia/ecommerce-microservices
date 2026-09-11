# Step 1: Start with a clean, lightweight Python operating system
FROM python:3.11-slim

# Step 2: Set the working folder inside the container
WORKDIR /app

# Step 3: Install FastAPI and Uvicorn inside the container
RUN pip install fastapi uvicorn httpx

# Step 4: Copy your local main.py file into the container
COPY . /app

# Step 5: Open port 8000 so the outside world can talk to it
EXPOSE 8000

# Step 6: The command to start the app when the container turns on
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
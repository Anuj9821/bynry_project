# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project code into the container
COPY . /app/

# Step 6: Expose port 8000 (Django's default port)
EXPOSE 8000

# Step 7: Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
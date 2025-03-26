# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files (NOTE: copy interview-data.csv into '/automotive-backend' beforehand)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Django management commands
RUN python manage.py migrate
RUN python manage.py import_csv_data

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
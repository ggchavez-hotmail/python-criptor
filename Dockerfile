# Use the official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copia el archivo de requisitos y el archivo de servicio de claves
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the requirements file into the container at /app
COPY src/ /app/src
RUN python -m pip install --upgrade pip

ENV TZ="America/Santiago"

EXPOSE 8080

# Run app.py when the container launches
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]


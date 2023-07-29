# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# PyDub dependencies
RUN apt-get update

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade --trusted-host pypi.python.org pip
RUN pip install --upgrade --trusted-host pypi.python.org -r requirements.txt


# Run bot.py when the container launches
CMD ["python", "bot.py"]
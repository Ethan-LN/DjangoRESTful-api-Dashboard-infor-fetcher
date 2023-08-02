FROM python:3.10.12-bullseye

WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip3.10 install --upgrade pip --no-cache-dir

RUN pip3.10 install -r requirements.txt --no-cache-dir

# Copy the Django app code to the container
COPY . /app/

#CMD ["python3.10","manage.py","runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "dashboardInforAPI.wsgi:application", "--bind", "0.0.0.0:8000"]
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ExpDashboard
WORKDIR /ExpDashboard
RUN pip install pipenv
ADD Pipfile /ExpDashboard/
ADD Pipfile.lock /ExpDashboard/
RUN pipenv install --system
ADD . /ExpDashboard/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

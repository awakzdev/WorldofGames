FROM python
WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python"]
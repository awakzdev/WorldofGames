FROM python
WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8777
CMD ["python", "flask"]

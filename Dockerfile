FROM python
WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip --proxy ${https_proxy} ${http_http}
RUN pip install -r requirements.txt --proxy ${https_proxy} ${http_http}
EXPOSE 8777
CMD ["python", "flask"]

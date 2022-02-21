FROM python
WORKDIR ./app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip --proxy http://proxy-dmz.intel.com:911
RUN pip install -r requirements.txt --proxy http://proxy-dmz.intel.com:911
EXPOSE 8777
CMD ["python", "flask"]

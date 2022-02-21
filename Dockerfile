FROM python
WORKDIR ./app
COPY . /app
RUN echo http proxy: ${http_proxy} ${HTTP_PROXY}
RUN echo https proxy: ${https_proxy} ${HTTPS_PROXY}
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8777
CMD ["python", "flask"]

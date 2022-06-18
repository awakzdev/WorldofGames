from bs4 import BeautifulSoup
import requests
import validators
import sys


def test_score_service():
    url = "http://127.0.0.1:8777/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    print(soup.h1.text)


def main_function():
    up = validators.url("http://127.0.0.1:8777/")
    if up:
        print("Code 0, Website is up and running")
    else:
        print("Error, code number -1, Website is unreachable")
        sys.exit(1)


if __name__ == "__main__":
    main_function()

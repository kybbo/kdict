import requests, sys, lxml
from bs4 import BeautifulSoup

def curl_merriam_webster():
    # scraps html from given word out of merriem-webster.com
    kdict_input = sys.argv[1]
    curl_output = requests.get("https://www.merriam-webster.com/dictionary/"+kdict_input)

    return curl_output.text

def scrap_curl(curl_output: str):
    # refactors mega string to get only desired html
    soup = BeautifulSoup(curl_output, "lxml")
    chosen_div = soup.find(id="dictionary-entry-1")

    return chosen_div.text

def main():
    print(scrap_curl(curl_merriam_webster()))

if __name__ == "__main__":
    main()

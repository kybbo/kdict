import requests, sys, lxml
from bs4 import BeautifulSoup
from rich import print

def curl_merriam_webster():
    # scraps html from given word out of merriam-webster.com
    kdict_input = sys.argv[1]
    curl_output = requests.get("https://www.merriam-webster.com/dictionary/"+kdict_input)

    return curl_output.text

def scrap_curl(curl_output: str):
    # refactors mega string to get only desired html
    soup = BeautifulSoup(curl_output, "lxml")
    #chosen_div = soup.find(id="dictionary-entry-1")
    title = soup.select_one("#dictionary-entry-1 .row.entry-header .col-12 .entry-header-content .hword")
    word_type = soup.select_one("#dictionary-entry-1 .row.entry-header .col-12 .entry-header-content .parts-of-speech .important-blue-link")
    definition = soup.select_one("#dictionary-entry-1 .vg .vg-sseq-entry-item .sb .sb-0 .sense .dt .dtText")

    key_words = [title.text, word_type.text, definition.text]


    return key_words

def enrich_output(key_words):
    key_words = scrap_curl(curl_merriam_webster())

    print(f"[bold]{key_words[0]}[bold] [italic]{key_words[1]}[italic]")
    print(key_words[2])

def main():
    enrich_output(scrap_curl(curl_merriam_webster()))

if __name__ == "__main__":
    main()

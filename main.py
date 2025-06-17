import requests, sys
from bs4 import BeautifulSoup
from rich import print

def curl_merriam_webster():
    kdict_input = sys.argv[1]
    try:
        response = requests.get(f"https://www.merriam-webster.com/dictionary/{kdict_input}", timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"couldn't reach merriam-webster")
        sys.exit(1)
    return response.text

def scrap_curl(curl_output: str):
    soup = BeautifulSoup(curl_output, "lxml")

    title = soup.select_one("#dictionary-entry-1 .row.entry-header .col-12 .entry-header-content .hword")
    word_type = soup.select_one("#dictionary-entry-1 .row.entry-header .col-12 .entry-header-content .parts-of-speech .important-blue-link")
    definition = soup.select_one("#dictionary-entry-1 .vg .vg-sseq-entry-item .sb .sb-0 .sense .dt .dtText")

    if not title or not word_type or not definition:
        print("not a word (probably)")
        sys.exit(1)

    return [title.text.strip(), word_type.text.strip(), definition.text.strip()]

def enrich_output(key_words):
    print(f"[bold]{key_words[0]}[/bold] [italic]{key_words[1]}[/italic]")
    print(key_words[2])

def main():
    try:
        html = curl_merriam_webster()
        key_words = scrap_curl(html)
        enrich_output(key_words)
    except Exception as e:
        print(f"[red]❌ Error inesperado: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()

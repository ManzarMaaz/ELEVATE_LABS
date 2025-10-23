# ⚽ BBC Football Headline Scraper

This is a simple Python script that scrapes the latest football headlines from the BBC Sport website and saves them to a text file.

-----

## ⚙️ Requirements

You'll need the following Python libraries:

  * **`requests`**: To make HTTP requests to the website.
  * **`beautifulsoup4`**: To parse the HTML content and extract data.

Install them using pip:

```bash
pip install requests beautifulsoup4
```

-----

## 🚀 How to Run

1.  Save the provided code as a Python file (e.g., `scraper.py`).
2.  Run the script from your terminal:

<!-- end list -->

```bash
python scraper.py
```

-----

## ✨ Output

The script will:

1.  Print the scraped headlines to your console.
2.  Create a file named **`headlines.txt`** in the same directory, containing all the collected headlines, one per line.

-----

## 📝 Key Technologies

  * **Web Scraping:** The process of automatically extracting data from websites.
  * **`requests`:** Handles fetching the web page content.
  * **`BeautifulSoup`:** Handles locating and cleaning the headline text from the HTML structure.
  * **File I/O:** Saves the final, clean output to a local file.

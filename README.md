# Books Scraper

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Colab](https://img.shields.io/badge/Platform-Colab-lightgrey)

A **web scraper** for [Books to Scrape](https://books.toscrape.com), a demo site with 1000 books. This scraper collects book information and saves it as a CSV file for analysis.

---

## Features

- Scrapes all 1000 books from the site.
- Collects:
  - **Title**
  - **Price**
  - **Availability**
  - **Rating** (e.g., One, Two, Three, Four, Five)
  - **Category**
- Outputs a **CSV file** ready for analysis.
- Works entirely in **Google Colab** or local Python environment.
  
---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
# Books Scraper

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Colab](https://img.shields.io/badge/Platform-Colab-lightgrey)

A **web scraper** for [Books to Scrape](https://books.toscrape.com), a demo site with 1000 books. This scraper collects book information and saves it as a CSV file for analysis.

---

## Features

- Scrapes all 1000 books from the site.
- Collects:
  - **Title**
  - **Price**
  - **Availability**
  - **Rating** (e.g., One, Two, Three, Four, Five)
  - **Category**
- Outputs a **CSV file** ready for analysis.
- Works entirely in **Google Colab** or local Python environment.
  
---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
pip install requests beautifulsoup4 pandas
python books_scraper.py
Usage

Run the scraper script in Colab or locally:

python books_scraper.py
usage

The script will loop through all 50 pages of the website.

It will visit each book’s detail page to collect the category.

Data will be saved as books_full.csv.

In Colab, the CSV file will be downloaded automatically.
How It Works

The scraper uses requests to fetch page content and BeautifulSoup to parse HTML.

Loops over all pages and selects each book element.

Extracts:

Title

Price

Availability

Rating

Opens each book’s detail page to get the category.

Saves all data in a pandas DataFrame and outputs it to CSV.
Future Improvements

Faster scraping without opening each detail page.

Export directly to Excel or a database.

Add robust error handling for network issues.

Add logging for scraping progress and errors.

License

This project is for educational and demonstration purposes.
Feel free to reuse or modify for your own projects.



```markdown
# Adidas T-Shirt Price Scraper

A Python-based web scraper designed to extract product details (such as product name and price) for **Adidas Originals T-shirts** from multiple e-commerce platforms, including **Amazon**, **Myntra**, **Nykaa**, **AJIO**, and **Adidas India**. The scraper uses **Selenium WebDriver** in headless mode to interact with the websites and save the extracted data into a structured CSV file for easy analysis.

## Features

- **Multi-Platform Scraping**: Collects data from Amazon, Myntra, Nykaa, AJIO, and Adidas India.
- **Headless Mode**: Runs in the background without opening a browser window, ideal for automated scraping.
- **Error Handling**: Automatically saves screenshots and HTML page sources for debugging when an error occurs.
- **Progress Indicators**: Displays a progress bar and custom animations for better user experience during scraping.
- **CSV Output**: Saves the scraped data in a CSV file, including product name and price.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.x
- Chrome WebDriver (managed automatically by `webdriver-manager`)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-username>/adidas-tshirt-price-scraper.git
cd adidas-tshirt-price-scraper
```

### Step 2: Install required dependencies

You can install all the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The dependencies include:
- `selenium`: For web scraping using the Chrome WebDriver.
- `webdriver-manager`: For automatically managing the Chrome WebDriver.
- `pandas`: For storing and saving the scraped data in CSV format.
- `tqdm`: For displaying progress bars during scraping.

## Usage

1. Run the scraper script:

```bash
python scraper.py
```

2. The script will start extracting data from the listed websites and save the results in a CSV file named `adidas_originals_tshirt_prices.csv`.

3. The output CSV file will contain the following columns:
    - `Site`: The name of the e-commerce platform.
    - `Product Name`: The name of the product (Adidas T-shirt).
    - `Price`: The price of the product.

### Customize URLs

If you want to scrape other products or sites, you can modify the `urls` dictionary in the `scraper.py` file with the URLs of the desired product pages.

## Error Handling

If an error occurs while scraping (e.g., missing element or timeout), the scraper will:

- Save a **screenshot** of the page.
- Save the **HTML page source** for debugging purposes.

These files will be saved with the name of the e-commerce site, making it easy to investigate any issues.

## Output

The scraped product details will be stored in a **CSV file** (`adidas_originals_tshirt_prices.csv`). You can open the file with any text editor or spreadsheet application (e.g., Microsoft Excel, Google Sheets) to analyze the data.

### Example CSV Output:

| Site     | Product Name                           | Price     |
|----------|----------------------------------------|-----------|
| Amazon   | Adidas Striped Regular T-Shirt         | ₹1,499    |
| Myntra   | Adidas Originals Melange Effect T-Shirt| ₹1,799    |
| Nykaa    | Adidas Originals Tiboa Dir Tee         | ₹1,599    |
| AJIO     | Adidas Originals Trefoil T-Shirt       | ₹1,799    |
| Adidas   | Adidas Adicolor Classics 3-Stripes Tee | ₹1,699    |


## Contributing

Feel free to fork the repository and submit pull requests for any improvements, bug fixes, or new features! If you find any issues or have suggestions, please open an issue on the GitHub repository.

## Acknowledgments

- This project uses **Selenium WebDriver** to interact with the websites and scrape data.
- The **webdriver-manager** package is used for managing the Chrome WebDriver automatically.
- **pandas** is used for storing and exporting the scraped data into CSV format.
- **tqdm** is used for displaying progress bars and animations during the scraping process.

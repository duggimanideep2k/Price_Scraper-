from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import sys
from tqdm import tqdm  # For progress bar

# Chrome options for headless mode and mimicking a real browser
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Initialize WebDriver with options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List of URLs to scrape
urls = {
    'Amazon': 'https://www.amazon.in/Adidas-Striped-Regular-T-Shirt-FJ9216_White_L/dp/B07VDL5R4N/ref=sr_1_2_sspa?crid=1RLNH7ZTRSQ3J&dib=eyJ2IjoiMSJ9.vpOjbMw4wQIq__Wbm3Zkt2lOO3TWE-P5GyYSFPmFF8a0y26YmzroDZH6t9buKEp8QAoumhPxBRWMb1BLUb54EtZZ-NC3GwVnz4O32S2D2BrrWPk_ff5vG3PNZyWdQ5k4xghi9QkIrOnvkX8_ZuylB3tcUVAgdeT97o_bSgj0eccUNnXcPJVzCH_NiuJtT3itaCac50GneqjjIiugyj0ZLBNttEMagLsEqemAqAyfWQQxJFa49wkojgYensW0UosWmmoXs7axoWRi9HmTHmsLQyeORGjF6sIziwF9aGOzISc.Mv1XE_NWfAHlYYgwT8hbHzMKOIFY8FYfkYdER4zAToM&dib_tag=se&keywords=adidas+original+tshirt+white&nsdOptOutParam=true&qid=1740277749&s=apparel&sprefix=adidas+original+tshirt+white%2Capparel%2C156&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
    'Myntra': 'https://www.myntra.com/tshirts/adidas+originals/adidas-originals-melange-effect-3-stripes-slim-raglan-tee/30381310/buy',
    'Nykaa': 'https://www.nykaafashion.com/adidas-originals-tiboa-dir-tee-white-casual-t-shirts/p/6936493?utm_source=PDPShareWEB&utm_medium=PDPWEB&utm_campaign=PDPreferralWEB&utm_id=PDPShareBtnWEB',
    'AJIO': 'https://www.ajio.com/adidas-originals-trefoil-casual-crew-neck-t-shirt/p/469597310_purple',
    'Adidas': 'https://www.adidas.co.in/adicolor-classics-3-stripes-tee/IA4846.html'
}

# Data storage
data = []

# Function to clean text (remove extra spaces and newlines)
def clean_text(text):
    return ' '.join(text.split()).strip()

# Function to display a spinner animation
def spinner_animation(message):
    spinner = ['-', '\\', '|', '/']
    for _ in range(10):  # Run for 10 iterations
        for char in spinner:
            sys.stdout.write(f"\r{message} {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")  # Clear the spinner line

# Function to display a checkmark animation
def checkmark_animation(message):
    for _ in range(3):  # Blink the checkmark 3 times
        sys.stdout.write(f"\r{message} ✓")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{message}  ")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write(f"\r{message} ✓\n")

# Function to extract product details
def extract_details(site_name, url):
    print(f"\nScraping data from {site_name}...")
    spinner_animation("Loading page")  # Spinner animation while loading the page

    driver.get(url)
    time.sleep(5)  # Wait for the page to load completely

    try:
        if site_name == 'Amazon':
            product_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'productTitle'))
            ).text.strip()
            product_price = driver.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text.strip()

        elif site_name == 'Myntra':
            product_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.pdp-title'))
            ).text.strip()
            product_price = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.pdp-price'))
            ).text.strip()

        elif site_name == 'Nykaa':
            product_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-at="product-name"].css-175ipe2'))
            ).text.strip()
            product_price = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-at="sp-pdp"]'))
            ).text.strip()

        elif site_name == 'AJIO':
            product_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'prod-name'))
            ).text.strip()
            product_price = driver.find_element(By.CLASS_NAME, 'prod-sp').text.strip()

        elif site_name == 'Adidas':
            product_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-auto-id="product-title"]'))
            ).text.strip()
            product_price = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-auto-id="gl-price-item"]'))
            ).text.strip()

        else:
            product_name = 'N/A'
            product_price = 'N/A'

        # Clean the extracted text to remove extra spaces and newlines
        product_name = clean_text(product_name)
        product_price = clean_text(product_price)

        # Print the extracted data
        print(f"Extracted from {site_name}:")
        print(f"Product Name: {product_name}")
        print(f"Price: {product_price}")
        print("-" * 40)

        # Append data to the list
        data.append({
            'Site': site_name,
            'Product Name': product_name,
            'Price': product_price
        })

        # Display checkmark animation for successful extraction
        checkmark_animation(f"Data extracted from {site_name}")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error extracting data from {site_name}: {e}")
        driver.save_screenshot(f'{site_name}_error.png')
        print("Saving page source for debugging...")
        with open(f'{site_name}_page_source.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)

# Iterate over URLs and extract data
print("Starting data extraction...")
for site, link in tqdm(urls.items(), desc="Overall Progress", unit="site"):
    extract_details(site, link)
    time.sleep(5)  # Add a delay between requests to avoid being blocked

# Close the WebDriver
driver.quit()

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('adidas_originals_tshirt_prices.csv', index=False)

print("\nData extraction complete. Saved to 'adidas_originals_tshirt_prices.csv'.")

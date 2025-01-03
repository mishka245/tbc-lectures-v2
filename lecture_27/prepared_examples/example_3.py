# Demo I am not robot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Product to search
SEARCH_TERM = "laptop"

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure you have the correct WebDriver installed
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open Amazon
    driver.get("https://www.amazon.com")
    print("Opened Amazon")

    # Step 2: Search for the product
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys(SEARCH_TERM)
    search_box.send_keys(Keys.RETURN)
    print(f"Searched for: {SEARCH_TERM}")

    # Step 3: Wait for results to load
    time.sleep(3)

    # Step 4: Scrape product data
    product_data = []
    products = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    for product in products[:10]:  # Scrape top 10 results
        try:
            title = product.find_element(By.CSS_SELECTOR, "h2 .a-link-normal").text
            price_whole = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            price_fraction = product.find_element(By.CSS_SELECTOR, ".a-price-fraction").text
            price = f"{price_whole}.{price_fraction}"
            rating = product.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")

            product_data.append({
                "Title": title,
                "Price": price,
                "Rating": rating
            })
        except Exception as e:
            continue  # Skip if any data is missing

    # Step 5: Save data to a file
    df = pd.DataFrame(product_data)
    df.to_csv("amazon_price_tracker.csv", index=False)
    print("Scraped data saved to 'amazon_price_tracker.csv'.")

    # Display the scraped data
    print("\nScraped Product Data:")
    print(df)

finally:
    # Step 6: Close the browser
    driver.quit()
    print("Browser closed")
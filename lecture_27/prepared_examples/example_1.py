# Poetry add selenium
# pip install selenium



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure you have the correct WebDriver installed (e.g., chromedriver)

try:
    # Step 1: Open a browser and navigate to Google
    driver.get("https://www.google.com")
    print("Opened Google")
    time.sleep(3)

    # Step 2: Find the search bar and input a search query
    search_box = driver.find_element(By.NAME, "q")
    search_query = "Python programming"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    print(f"Searched for: {search_query}")

    # Step 3: Wait for the results to load
    time.sleep(3)  # Replace with WebDriverWait for better practice

    # Step 4: Retrieve the titles of search results
    search_results = driver.find_elements(By.XPATH, "//h3")
    print("\nSearch Results:")
    for index, result in enumerate(search_results, start=1):
        print(f"{index}. {result.text}")

finally:
    # Step 5: Close the browser
    driver.quit()
    print("Browser closed")
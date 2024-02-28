from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Configuration for the WebDriver
# Replace 'path/to/your/webdriver' with the actual path to your WebDriver executable
driver_path = 'path/to/your/webdriver'
driver = webdriver.Chrome(driver_path)

# URL of the page with dynamic content
url = 'https://example.com/dynamic-content'

# Navigate to the page
driver.get(url)

# Wait for the dynamic content to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'your-dynamic-content-selector'))
)

# Example: Extracting dynamic content
def extract_info(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Replace '.dynamic-content' with the actual selector of the content you wish to extract
    dynamic_content = soup.select('.dynamic-content')
    for content in dynamic_content:
        print(content.text.strip())

extract_info(driver)

# Example: Handling pagination
# Assuming there is a 'Next' button with an identifiable selector
try:
    while True:
        next_button = driver.find_element(By.CSS_SELECTOR, 'your-next-page-button-selector')
        if next_button:
            next_button.click()
            # Wait for the page to load and dynamic content to appear
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'your-dynamic-content-selector'))
            )
            # Extract information from the new page
            extract_info(driver)
        else:
            break
except Exception as e:
    print(f"Reached the end of pages or encountered an error: {e}")

# Close the WebDriver
driver.quit()

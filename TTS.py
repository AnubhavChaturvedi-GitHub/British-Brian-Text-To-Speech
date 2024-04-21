import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging to suppress console logs
logging.getLogger('selenium').setLevel(logging.WARNING)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# Run in headless mode (without opening a browser window)

# Create a Service object with WebDriverManager to automatically manage the ChromeDriver binary
chrome_service = Service(ChromeDriverManager().install())

# Create a Chrome driver instance with the specified options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")

def speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        text_to_input = text
        element_to_click.send_keys(text_to_input)
        print(text_to_input)

        # Calculate sleep duration based on sentence length
        sleep_duration = min(0.2 + len(text) // 10,15)  # Minimum sleep is 3 seconds, maximum is 10 seconds

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print("An error occurred:", e)



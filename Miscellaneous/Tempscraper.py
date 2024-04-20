from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the webpage containing the data
url = 'https://en.tutiempo.net/climate/madagascar.html'

# Initialize a Chrome webdriver (you can also use other browsers like Firefox)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get(url)

# Perform necessary interactions to navigate to the page containing the humidity data
# For example, click buttons, fill out forms, etc.
# Use WebDriverWait to wait for specific elements to appear before interacting with them
# Replace the following lines with the actual interactions needed to reach the humidity data
element1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button1"))
)
element1.click()

element2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "button2"))
)
element2.click()

# Once you have reached the page containing the humidity data, extract it
# Replace the following line with code to extract the humidity data
humidity_data = driver.find_element_by_css_selector('.humidity').text

# Print the extracted humidity data
print(humidity_data)

# Close the browser
driver.quit()

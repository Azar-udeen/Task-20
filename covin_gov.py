from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (adjust the path to your chromedriver)
driver = webdriver.Chrome()

try:
    # Navigate to the Cowin website
    driver.get("https://www.cowin.gov.in/")
    time.sleep(2)  # Adding a delay to ensure elements are loaded properly

    # Click on "FAQ" link to open in a new window
    faq_link = driver.find_element_by_xpath("//a[contains(text(), 'FAQ')]")
    faq_link.send_keys(Keys.CONTROL + Keys.RETURN)

    # Click on "Partners" link to open in a new window
    partners_link = driver.find_element_by_xpath("//a[contains(text(), 'Partners')]")
    partners_link.send_keys(Keys.CONTROL + Keys.RETURN)

    # Get all window handles (IDs)
    windows = driver.window_handles

    # Print the IDs of the opened windows/frames
    print("Opened Window/Frame IDs:")
    for window in windows:
        print(window)

    # Switch back to the original window
    driver.switch_to.window(windows[0])

    # Wait for a moment to show the IDs in console
    time.sleep(2)

    # Close the new windows/frames
    for window in windows[1:]:
        driver.switch_to.window(window)
        driver.close()

    # Switch back to the original window (Home page)
    driver.switch_to.window(windows[0])

finally:
    # Close the WebDriver
    driver.quit()
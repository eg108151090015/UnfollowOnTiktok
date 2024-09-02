from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Path to your Driver executable
driver_path = ''

# Initialize the Edge WebDriver service
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Go to the TikTok login page
driver.get('https://www.tiktok.com/login')

# Wait for the user to manually log in
print("Please log in manually within 100 seconds...")
sleep(100)  # Adjust this time if you need more time to log in

# After logging in manually, continue with the script
driver.get('https://www.tiktok.com/@your_username/following')  # Replace 'your_username' with your TikTok username

# Wait for the page to load
sleep(50)

# Scroll down to load all the following users (Optional)
for i in range(10):  # Adjust the range based on how many accounts you're following
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    sleep(0.5)

# Unfollow users
for i in range(10000):  # Adjust range based on number of users to unfollow
    try:
        # Wait until the "Following" button is present
        unfollow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Following']"))
        )
        unfollow_button.click()
        sleep(1)  # Adjust sleep to avoid detection
        print(f"Unfollowed user {i+1}")
    except Exception as e:
        print(f"Unfollow button not found, skipping. Error: {e}")
        break

# Close the browser
driver.quit()
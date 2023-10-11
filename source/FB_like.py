from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()
firefox_options.headless = True

# Use the appropriate executable path for your Firefox driver
driver = webdriver.Firefox()

# Navigate to the Facebook website
driver.get('https://www.facebook.com')

# Enter your username and password
username = 'lol.chend6@gmail.com'
password = 'Kuro_.'
username_field = driver.find_element(By.NAME,'email')
password_field = driver.find_element(By.NAME,'pass')
username_field.send_keys(username)
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.NAME,'login')
login_button.click()

# Wait for the login to complete
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains('facebook.com'))

# Navigate to the URL of the post you want to like (replace with your desired URL)
post_url = 'https://www.facebook.com/groups/809451909155303/permalink/6143706985729742/?mibextid=oMANbw'
driver.get(post_url)

# Find the like button and click it
like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="讚"]')))
like_button.click()

# Close the browser
driver.quit()

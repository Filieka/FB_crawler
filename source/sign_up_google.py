from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import string

firefox_options = Options()
firefox_options.headless = True

# Use the appropriate executable path for your Firefox driver
driver = webdriver.Firefox()

# Navigate to the Facebook website
driver.get('https://accounts.google.com/signup')

lastname_field = driver.find_element(By.NAME,'lastName')
firstname_field = driver.find_element(By.NAME,'firstName')
lastname_field.send_keys(random.randint(0,10000))
firstname_field.send_keys(random.randint(0,99))

# Click the login button
next_button = driver.find_element(By.CLASS_NAME,'VfPpkd-vQzf8d')
next_button.click()

# Wait for the login to complete
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains('birthday'))


year_field=driver.find_element(By.NAME,'year')
month_select=driver.find_element(By.ID,'month')
day_field=driver.find_element(By.NAME,'day')
gender_select=driver.find_element(By.ID,'gender')
year_field.send_keys(random.randint(1993,2003))
select=Select(month_select)
select.select_by_index(random.randint(1,12))
day_field.send_keys(random.randint(1,28))
select=Select(gender_select)
select.select_by_index(random.randint(1,3))

next_button = driver.find_element(By.CLASS_NAME,'VfPpkd-vQzf8d')
next_button.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains('createusername'))

characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for i in range(10))
username_field=driver.find_element(By.NAME,'Username')
username_field.send_keys(random_string)

next_buttons = driver.find_element(By.CLASS_NAME,'VfPpkd-vQzf8d')
driver.execute_script("arguments[0].click();", next_button)

wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains('createpassword'))

password_field=driver.find_element(By.NAME,'Passwd')
passwordAgain_field=driver.find_element(By.NAME,'PasswdAgain')
characters = string.ascii_letters + string.digits
random_string = ''.join(random.choice(characters) for i in range(10))
password_field.send_keys(random_string)
passwordAgain_field.send_keys(random_string)

next_button = driver.find_element(By.CLASS_NAME,'VfPpkd-vQzf8d')
next_button.click()


# Close the browser
#driver.quit()
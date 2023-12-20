from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


firefox_options = Options()
firefox_options.headless = True

# Use the appropriate executable path for your Firefox driver
driver = webdriver.Firefox()

# Navigate to the Facebook website
driver.get('https://www.facebook.com')

# Enter your username and password
username = 'dennybrother001@gmail.com'
password = 'i++_890'
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
post_url = 'https://www.facebook.com/permalink.php?story_fbid=pfbid0BAaAWQwnu2tdhGFHExYmtPPC33egGBxinCecRj45ZMyEazZ7v934iZGz2hBgtRFkl&id=100023392844155'
driver.get(post_url)
wait.until(EC.url_contains('facebook.com'))


comment_box_xpath = '//div[@aria-label="留言……" and @role="textbox"]'
#comment_box = wait.until(EC.element_to_be_clickable((By.XPATH, comment_box_xpath)))
comment_box = driver.find_element(By.XPATH,comment_box_xpath)

# 在留言框輸入內容
'''
i=0
comment_text = '@陳柏諺'
while (i<4):
    comment_box.send_keys(comment_text[i])
    i=i+1
# 使用 JavaScript 設置留言框的值
#driver.execute_script(f'arguments[0].value = "{comment_text}";', comment_box)
time.sleep(2)
comment_box.send_keys(Keys.ENTER)
'''

i=0
comment_text = '這就是說中的許教授嗎'
length=len(comment_text)
while (i<length):
    comment_box.send_keys(comment_text[i])
    i=i+1
time.sleep(0.5)
comment_box.send_keys(Keys.ENTER)



# Find the like button and click it
'''
like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="讚"]')))
like_button.click()
'''

# Close the browser
driver.quit()

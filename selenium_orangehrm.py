
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
import time
#url ="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
username="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
password="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
#home_dashboard="//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6"
#title='OrangeHRM'
paul="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img"
logout="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
time.sleep(3)
driver.find_element_by_xpath(username).send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath(password).send_keys("admin123")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(3)
driver.find_element_by_xpath(paul).click()
time.sleep(3)
driver.find_element_by_xpath(logout).click()
#time.sleep(3)
#expected_dashboard = 'Dashboard'
#actual_dashboard = driver.find_element_by_xpath(home_dashboard)
#assert expected_dashboard == actual_dashboard
#expected_title = 'OrangeHRM'
#actual_title = driver.title
#print(actual_dashboard)
time.sleep(3)
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
actual_url = driver.current_url
driver.save_screenshot("image.png")
#assert expected_url == actual_url
print(driver.current_url)





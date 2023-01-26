from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
#url.driver = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login',webdriver.Chrome(ChromeDriverManager().install())
username,password="Admin","admin123"
print(username)
driver.get(url)
assert username == "Admin"
assert username !="Admin"

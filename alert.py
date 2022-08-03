"""locating the alert 
1. import time  from python
2. import webdriver from selenium.
3.import chromedrivermanager.in order to import chromedrivermanager 
ask pip to installwebdriver_manager
4.install chromedrivermanager and assign it to the variale driver.
5.use get fumction to open the web page with the help of url.
ie.driver.get("url")
6. once you click the alert button the alertmessage will pop up. which will be the differnt 
page so you need to swith to the alert section by using 
switch_to.alert.
"""

import time#this is python time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #if weddriver_manager is not found run
#pip install webdrive_manager
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(ChromeDriverManager().install())# your entire selenium chrome package
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)#this will hold the time for 5 seconds
driver.maximize_window()
time.sleep(3)#this will hold the time for 3 seconds
driver.refresh()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[name='radioButton']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='option1']").click()
time.sleep(3)
driver.find_element(By.ID,"name").send_keys("Amrit")
time.sleep(3)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)
alert=driver.switch_to.alert
alerttext=alert.text
if ("Amrit" in alerttext) :
    print("test one passed")
else:
    print("test failed")    

driver.quit()
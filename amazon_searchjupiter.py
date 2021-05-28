#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# init driver
driver: WebDriver = webdriver.Chrome(executable_path='C:\\Users\\omar\\Documents\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order', Keys.ENTER)

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-search']").click()

actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
print(f'Actual result: {actual_result}')
expected_result = "Cancel Items or Orders"
# verify
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
#print("Test Passed")
driver.quit()


# In[ ]:





import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
username=input("Enter your linkedin user id:")
password=input("Enter your linkedin password:")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started.")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("linkedin")
time.sleep(1)
driver.find_element_by_name("btnK").click()
time.sleep(1)
driver.find_element_by_partial_link_text("LinkedIn Login").click()
time.sleep(2)
driver.find_element_by_name("session_key").send_keys(username)
time.sleep(1)
driver.find_element_by_name("session_password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.close()
print("Test case completed.")
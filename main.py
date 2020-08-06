# This project is unfinished. I will work on it once I gain a bit more knowledge.
# https://www.youtube.com/watch?v=b5jt2bhSeXs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print(driver.title)

search = driver.find_element_by_name("a")
search.send_keys("Guido van Rossum")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()

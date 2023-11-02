from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/home/renans/Desktop/Projects/robots/course2/selenium/chromedriver-linux64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

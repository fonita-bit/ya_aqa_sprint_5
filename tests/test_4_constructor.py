from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://stellarburgers.nomoreparties.site/')


driver.quit()
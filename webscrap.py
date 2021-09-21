from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import IGNORED_EXCEPTIONS
import csv


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://mailingio.io/companies/write/prod")



with open('bazamail.csv', 'w', newline='', encoding='utf_8_sig') as csvfile:
    writer = csv.writer(csvfile, dialect = 'excel')

    for strona in range(5): 
        try: 

            nazwyfirm = driver.find_elements_by_xpath("//div[@class='title']/a")
            maile = driver.find_elements_by_class_name("btn.btn-primary.btn-xs")
            naststrona = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "→")))
            #elems = zip(nazwyfirm,numerytel)

            for nazwy in nazwyfirm:
                print(nazwy.text)
                writer.writerows([nazwy.text.split(',')])

            for tel in maile:
                print(tel.get_attribute('data-hidden-value'))
                writer.writerows([tel.get_attribute('data-hidden-value').split(',')])



        finally:
            naststrona.click()


    else:
        driver.quit()



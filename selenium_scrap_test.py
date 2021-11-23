from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import IGNORED_EXCEPTIONS
import csv
import pandas as pd

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://example.pl/category")


driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[4]/i').click()
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[2]/div[2]/button').click()


def extractfirmy():
    nazwy = driver.find_elements_by_xpath('/html[1]/body[1]/div[4]/div[3]/div[1]/main[1]/ul[1]/li/div[1]/div[1]/h2[1]/a[1]')
    numerytel = driver.find_elements_by_xpath('/html[1]/body[1]/div[4]/div[3]/div[1]/main[1]/ul[1]/li/div[3]/div[1]/div[1]/div[1]/a[1]')
    maile = driver.find_elements_by_xpath('/html[1]/body[1]/div[4]/div[3]/div[1]/main[1]/ul[1]/li/div[3]/div[1]/div[1]/div[3]/a[1]')

    listalist = zip(nazwy, numerytel, maile)
    for nazwa, numer, mail in listalist:
        n = nazwa.get_attribute("text").strip()
        nr = numer.get_attribute("data-original-title")
        m = mail.get_attribute("data-company-email")

        print(n,nr,m)
        #df = pd.read
        writer.writerow([n,nr,m])



<<<<<<< HEAD
with open('pfkam.csv', 'w', newline='', encoding='utf_8_sig') as csvfile:
    writer = csv.writer(csvfile, dialect = 'excel', delimiter="|")

=======
with open('pftlumaczenia.csv', 'w', newline='', encoding='utf_8_sig') as csvfile:
    writer = csv.writer(csvfile, dialect = 'excel', delimiter="|")
>>>>>>> 2a8b842ad64a407030555a398d016ccfde7f87ff

    for strona in range(5): 
        naststrona = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "i[class='icon-arrow-right']")))
        try: 

            extractfirmy()

        finally:
            naststrona.click()

    else:
        driver.quit()

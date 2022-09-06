import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shutil import which
import csv

chrome_path = which('chromedriver')

# Ctrl + Shift + Space allows you to see functions 
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(executable_path=chrome_path, options=options)
# browser.maximize_window()
# browser.implicitly_wait(45)

def downloader(url):
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=chrome_path, options=options)
    browser.implicitly_wait(45)


    browser.get(url=url)
    try:
        WebDriverWait(browser, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='miIframe']")))
    except:
        print("Page without first iframe")

    WebDriverWait(browser, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='openDocChildFrame']")))
    WebDriverWait(browser, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='webiViewFrame']")))
    WebDriverWait(browser, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='_iframeleftPaneW']")))

    try :
        all_years = browser.find_element(by=By.XPATH, value="//option[@value='Todos los valores']")
        all_years.click()

        accept_years = browser.find_element(by=By.XPATH, value="//nobr[contains(@id, 'IF0_btn') or contains(@id, 'IF2_btn')]")
        accept_years.click()
    except:
        print("Page without All Years option")

    checkSelectAll = browser.find_elements(by=By.XPATH, value = "//input[contains(@id, '_checkSelectAll')]")

    for btn in checkSelectAll:

        print(btn.is_selected())

        for i in range(5):
            if btn.is_selected() == False:
                btn.click()

        print(btn.is_selected())


    browser.switch_to.parent_frame()

    time.sleep(5)

    export_btn = browser.find_element(by=By.XPATH, value = "//div[@id='IconImg__dhtmlLib_307']")

    export_btn.click()

    data_ratio = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='check_radioData']")))

    data_ratio.click()

    export_accept = browser.find_element(by=By.XPATH, value="//nobr[@id='Btn_OK_BTN_idExportDlg']")
    export_accept2 = browser.find_element(by=By.XPATH, value="//button[@id='RealBtn_OK_BTN_idExportDlg']")

    export_accept.click()
    export_accept2.click()

    time.sleep(10)

    browser.close()



with open('./bce_crawler/locations.csv') as f:
    csv_reader = list(csv.reader(f))
    for row in csv_reader[1:3]:
        print(row)

        print('--DOWNLOADING BEGINNING')
        downloader(url=row[0])

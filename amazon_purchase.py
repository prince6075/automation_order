from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


# search_term=input("Enter your search term:- ")

Service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=Service)
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(4)

input_element =driver.find_element(By.ID,"twotabsearchtextbox")
input_element.clear()
input_element.send_keys( "iphone 13"+ Keys.ENTER)
time.sleep(4)

driver.get("https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_1?crid=HV566NNJWM7N&dib=eyJ2IjoiMSJ9.OCoJgZ8ghdguKvc7Ozmt3MuV4EX2bqVAighnAy-84StpiRsfqUDXAr6MP3uGF_CaUGvtZH-n7Kvny5QAKxovreQ8WQg-3ktgMNTCXO-Z3b8bt1Zx9XlJKft6wpm3FDWaSz_4307ectPDdQoTcfbIxRRfKbdaSo0-7fxQephfY1Z-RYdNWE0IdrkDcWkpj9O_kKxRjjSHLixzqQkjY5OSJRphetStK-mvtFSayK-ReCc.McE3-t0ZF3v4ZWaTVtk1GqyfK8MSBXYIH388EFWY3xw&dib_tag=se&keywords=iphone+13&qid=1708546939&sprefix=iphone+13%2Caps%2C203&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
time.sleep(4)

addtocart=driver.find_element(By.XPATH,"/html/body/div[4]/div/div[3]/div[8]/div[8]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[37]/div[1]/span/span/span/input")
addtocart.click()
time.sleep(4)

cart=driver.find_element(By.XPATH,"//*[@id='attach-sidesheet-view-cart-button']/span/input").click()
time.sleep(4)

buy=driver.find_element(By.XPATH,"//*[@id='sc-buy-box-ptc-button']/span/input")
buy.click()
time.sleep(4)

sign=driver.find_element(By.XPATH,"//*[@id='ap_email']")
sign.send_keys("98745612241")
driver.find_element(By.XPATH,"//*[@id='continue']").click()
time.sleep(4)

password=driver.find_element(By.XPATH,"//*[@id='ap_password']")
password.send_keys("A9784561393")
driver.find_element(By.XPATH,"//*[@id='signInSubmit']").click()
time.sleep(4)

order=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span/input")
order.click()
time.sleep(7)

card_select=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[6]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
card_select.click()
time.sleep(4)


card_detail=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[6]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
card_detail.click()
time.sleep(10)


# pop
driver.switch_to.frame("ApxSecureIframe")
card_number=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
card_number.send_keys("4457892265599")
time.sleep(4)

nickname=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
nickname.clear()
nickname.send_keys("prince")
time.sleep(4)


expiraydate=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[3]/div[2]/div[1]/span[1]/select")
drop=Select(expiraydate)
drop.select_by_value("10")
time.sleep(4)

expiryear=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[3]/div[2]/div[1]/span[3]/select")
sel=Select(expiryear)
sel.select_by_value("2029")
time.sleep(4)

enter_card_detail=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
enter_card_detail.click()
time.sleep(5)

# back to normal page
driver.switch_to.default_content()

cvv=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[6]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")
cvv.send_keys("156")
time.sleep(4)

payment_method=driver.find_element(By.XPATH,"//*[@id='orderSummaryPrimaryActionBtn']/span/input")
payment_method.click()
time.sleep(4)


delete_card_detail=driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div/div/div/span[1]/span/input")
delete_card_detail.click()
time.sleep(10)

place_order=driver.find_element(By.XPATH,"//*[@id='submitOrderButtonId']/span/input")
place_order.click()
time.sleep(5)

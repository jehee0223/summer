from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

action=input("네이버 메뉴 선택 - 웹툰, 쇼핑, 날씨(네이버 창 유지하려면 x키 입력) : ")
if action=="웹툰":
    option=1
elif action=="쇼핑":
    option=2
elif action=="날씨":
    option=3
elif action=='x':
    option=4

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")            # url 오픈해라
driver.maximize_window()   #창 크게 만들기
if option==1:
    element = driver.find_element(By.CSS_SELECTOR,"#shortcutArea > ul > li:nth-child(9) > a").click()
    while (True):
        pass
elif option==2:
    element = driver.find_element(By.CSS_SELECTOR,"#shortcutArea > ul > li:nth-child(4) > a > span.service_icon.type_shopping").click()
    while (True):
        pass
elif option ==3:
    element = driver.find_element(By.CSS_SELECTOR,"#right-content-area > div.Layout-module__right_top___h3g3v > div:nth-child(3) > div > div.DailyBoardView-module__header_group___uGkqW > a.DailyBoardView-module__header_title___Uk3ix").click()
    while (True):
        pass
elif option==4:
    while (True):
        pass



# AUTOMATION DATA COLLECT

import os
import shutil
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# rename old file
os.chdir('C:/OTOMAX')
now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S") 
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == ('.xlsx'):
        new_name = ('producao_'+dt_string+file_ext)
        os.rename(f,new_name)

# move older files
dir1 = "C:/OTOMAX_old/"
def moveto(dst):
    return lambda src: shutil.move(src, dst)
action = {'xlsx': moveto(dir1)}

src_dir = 'C:/OTOMAX'
for file in os.listdir(src_dir):
    ext = os.path.splitext(file)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, file))        
        
# seting options download file loacate
options = webdriver.ChromeOptions()
#options.add_argument("--start-maximized")
prefs = {"profile.default_content_settings.popups": 0,"download.default_directory":"C:\OTOMAX"}
options.add_experimental_option("prefs", prefs)
driver=webdriver.Chrome("C:/Users/datacollect/AppData/Local/Programs/Python/Python39/chromedriver.exe",options=options)

#set login
username = 'ramyres@otomax.com'
password = '17253000'
# web site
url = "https://amigoapp.com.br/authenticate.html"
driver.get(url)
#doing login website
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath('/html/body/div/div[2]/form[1]/div[3]/button').click()
sleep(3)
#going to page finance
driver.get ('https://amigoapp.com.br/finance-production/')
sleep(3)
# clicking to fill date field
driver.find_element_by_class_name('ng-scope').click()
sleep(1)
datefield = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/input[1]')
search_btn = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/input[1]')
ActionChains(driver).move_to_element(search_btn).click().click().perform()
ActionChains(driver).move_to_element(datefield).click().send_keys('0').perform()
sleep(1)
datefield2 = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/input[2]')
search_btn2 = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/input[2]')
ActionChains(driver).move_to_element(search_btn2).click().click().perform()
ActionChains(driver).move_to_element(datefield2).click().send_keys('1').perform()
sleep(1)
# clicking to download
driver.find_element_by_class_name('ng-scope').click()
sleep(3)
driver.find_element_by_class_name('btn-group').click()
sleep(3)
driver.find_element_by_id('download-full-xlsx').click()
#closing navigator
sleep(120)
driver.close()
# Rename file
os.chdir('C:/OTOMAX')
#now = datetime.now()
#dt_string = now.strftime("%Y%m%d_%H%M%S") 
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_ext == ('.xlsx'):
        new_name = ('producao'+file_ext)
        os.rename(f,new_name)


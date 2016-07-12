import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import shutil

usr = "mas@efftronics.com"
pwd = "eff@ronics@123"


driver = webdriver.Chrome()
driver.get('http://admin.runexam.com/')
elem = driver.find_element_by_id("username")
elem.send_keys(usr)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(10)
elem = driver.find_element_by_id("settings")
elem.click()
time.sleep(5)
elem = driver.find_element_by_id("ExportData")
elem.click()
time.sleep(5)
elem = driver.find_element_by_id("exportcandidate")
elem.click()
time.sleep(2)
# elem = driver.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder1_group']/option[@value='16241']")
# elem.click()
# time.sleep(0.5)
# elem = driver.find_elements_by_class_name("fa-cloud-download")
# elem[0].click()

t = [16241,
16240,
16144,
16095,
16084,
16083,
15945,
15943,
15832,
15831,
15821,
15628,
15627,
15588,
15553,
15552,
15523,
15522,
15277,
15276,
5154,
5153,
5011,
5010,
4905,
4904]
for index in range(0,25):
	str1 = "//select[@id='ctl00_ContentPlaceHolder1_group']/option[@value='"+str(t[index])+"']"
	elem = driver.find_element_by_xpath(str1)
	elem.click()
	kkk = elem.text
	elem = driver.find_elements_by_class_name("fa-cloud-download")
	elem[0].click()
	time.sleep(3)
	for filename in os.listdir("C:\\Users\\16PJ106\\Downloads"):
		if filename.startswith("candidates"):
			os.rename(os.path.join("C:\\Users\\16PJ106\\Downloads",filename),os.path.join("C:\\Users\\16PJ106\\Downloads", str(index)+'_'+kkk + '.xls'))
	
	# filename = max([f for f in os.listdir('C:\\Users\\16PJ106\\Downloads')], key=os.path.getctime)
	# shutil.move(os.path.join('C:\Users\16PJ106\Downloads\New folder',filename),kkk)

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
elem = driver.find_element_by_id("exportexamresult")
elem.click()
time.sleep(2)
# elem = driver.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder1_group']/option[@value='16241']")
# elem.click()
# time.sleep(0.5)
# elem = driver.find_elements_by_class_name("fa-cloud-download")
# elem[0].click()

t =[53595,
53594,
53593,
53477,
53452,
53451,
53450,
53221,
52962,
52961,
52960,
52942,
52884,
52883,
52882,
52471,
51903,
51196,
50922,
50921,
50920,
48165,
48164,
36278,
36274,
36271,
35166,
35164,
35163]


for index in range(0,28):
	str1 = "//select[@id='ctl00_ContentPlaceHolder1_examlist']/option[@value='"+str(t[index])+"']"
	elem = driver.find_element_by_xpath(str1)
	elem.click()
	kkk = elem.text
	elem = driver.find_elements_by_class_name("fa-cloud-download")
	elem[0].click()
	time.sleep(4)
	for filename in os.listdir("C:\\Users\\16PJ106\\Downloads"):
		if filename.startswith("ExamResult"):
			os.rename(os.path.join("C:\\Users\\16PJ106\\Downloads",filename),os.path.join("C:\\Users\\16PJ106\\Downloads", str(index)+'_'+kkk + '.xls'))
	
	# filename = max([f for f in os.listdir('C:\\Users\\16PJ106\\Downloads')], key=os.path.getctime)
	# shutil.move(os.path.join('C:\Users\16PJ106\Downloads\New folder',filename),kkk)

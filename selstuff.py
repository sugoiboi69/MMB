from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


drvpath = "D:\Documents\pythy discbot"
driver = webdriver.Firefox(drvpath)
driver.get("https://www.google.com/search?tbs=sbi:AMhZZitVXXEA-MEE0uptTpT8P3A5htSN0eNaS_1ey4AD4d3f_1kV2dJ1_1oDvTJMIt9qGVw4YWQsiKkzynfH59u2cOz3Eyf4zvBcXxkOvD3SBkRCTXtV6YTB8Ur7tKHH_1ZMXwajIGiyzPkiiJpYPExfFPIHfvM8BHBPkNSDkmONqG1IhiQ8U2-xKwT5U7X4JovaTspPuuFQZ3XYEycsg839Lqww-WpyUHsz2Qe0XV9zU7_1XJCzVFbweO4pEWMHisjjE8H5ygU4-HAdMgPbCvhNggkeSRx2BAtXA7TFlwGY91hDGPswrS2PposW_1qmNDRS1qvB2usD9p8JeShNRod8Am1O7B78FV0wnTWQ&hl=en-SG")
divs = driver.find_element_by_class_name("r5a77d")
bestguess = divs.find_element_by_class_name("fKDtNb").text
print('-----------------------------------------------------')
print(str(bestguess))
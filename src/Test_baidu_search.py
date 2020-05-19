import pytest
import xlrd
from selenium import webdriver
from time import sleep, ctime
import os
from src.const import *
class Test_baidu_search():
    def test_search_from_excel(self,excel_dir=EXCEL_DIR):
        driver =webdriver.Chrome()
        driver.get("http://www.baidu.com")
        excel_file= xlrd.open_workbook(EXCEL_DIR)
        sheet =excel_file.sheet_by_index(0)
        cols=sheet.col_values(0)

        for query in cols:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(query))
            driver.find_element_by_id("su").click()
            sleep(5)
        driver.quit()
    def test_1(self):
        print("123")
        assert  1==1

    def test_2(self):
        print("321")
        assert  2==3
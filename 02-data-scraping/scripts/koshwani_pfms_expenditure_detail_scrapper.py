#Importing packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pdb
import time 
import os
import csv
import glob
from selenium.webdriver.support.ui import Select
from utils import section_selector,sel_elem_to_links, path_generator_dir_maker, table_to_csv , add_columns

#defining fiscal year and base folder to download data in
fiscal_year = "2019-2020"
parent_folder = "../datasets/"+fiscal_year+"/pfms_expenditure_detail/"

#setting up chrome driver
options = webdriver.ChromeOptions()
#chrome will download the files in the path defined in the below line
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)

url_of_section = "http://koshvani.up.nic.in/KoshReports/PFMSCentralSchemeWise.aspx"
section_selector(Select,driver,fiscal_year,url_of_section)

table = driver.find_elements_by_id("myTable")[0]
(links_of_schemes_url_string,links_of_scheme_name, name_of_hierarchy_schemes) = sel_elem_to_links(driver,table)

for index_schemes, schemes_link in enumerate(links_of_schemes_url_string):
    driver.get(schemes_link)
    table = driver.find_elements_by_id("myTable")[0]
    hierarchy = name_of_hierarchy_schemes[index_schemes]
    path = path_generator_dir_maker(driver,parent_folder,str(links_of_scheme_name[index_schemes]))
    table_to_csv(driver,path,links_of_scheme_name[index_schemes],table)
    add_columns(driver,path,links_of_scheme_name[index_schemes],fiscal_year,hierarchy)
  

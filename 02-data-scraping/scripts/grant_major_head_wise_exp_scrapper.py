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
from utils import section_selector,sel_elem_to_links, path_generator_dir_maker, table_download , add_columns

#defining fiscal year and base folder to download data in
fiscal_year = '2019-2020'

columns = ["Major Head","Voted/Charged","Total Budget Provision(Plan)",
"Progressive Allotment(Plan)","Actual Progressive Expenditure upto month(March)(Plan)",
'Provisional Current Month Expenditure(April)(Plan)',"Total Expenditure in Month(April)(Plan)",
"Total Budget Provision(Non-Plan)","Progressive Allotment(Non-Plan)",
"Actual Progressive Expenditure upto month(March)(Non-Plan)",
"Provisional Current Month Expenditure(April)(Non-Plan)","Total Expenditure in Month(April)(Non-Plan)"]


folder_to_download = "/home/ubuntu/cdl/koshvani/up-fiscal-data/02-data-scraping/datasets/"+fiscal_year+"/grant_major_head_wise_expenditure"

#setting up chrome driver
options = webdriver.ChromeOptions()
#chrome will download the files in the path defined in the below line
prefs = {'download.default_directory' : folder_to_download}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)

url_of_section = "http://koshvani.up.nic.in/KoshReports/GrntBud.aspx"
section_selector(Select,driver,fiscal_year,url_of_section)

table = driver.find_elements_by_id("myTable")[0]
(links_of_grants_url_string,links_of_grants_name, name_of_hierarchy_grants) = sel_elem_to_links(driver,table)

for index_grants, grants_link in enumerate(links_of_grants_url_string):
    driver.get(grants_link)
    table = driver.find_elements_by_id("myTable")[0]
    hierarchy = name_of_hierarchy_grants[index_grants]
    path = path_generator_dir_maker(driver,folder_to_download,str(links_of_grants_name[index_grants]))
    table_download(folder_to_download,driver,path,links_of_grants_name[index_grants],table,columns)
    add_columns(driver,path,links_of_grants_name[index_grants],fiscal_year,hierarchy)
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
from utils import section_selector, path_generator_dir_maker, table_to_csv, add_columns, sel_elem_to_links

#defining fiscal year and base folder to download data in
fiscal_year = "2019-2020"
parent_folder = "../datasets/"+fiscal_year+"/ddo_wise_expenditure"

#setting up chrome driver
options = webdriver.ChromeOptions()
#chrome will download the files in the path defined in the below line
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)

url_of_section = "http://koshvani.up.nic.in/KoshReports/DDOExp.aspx"
section_selector(Select,driver,fiscal_year,url_of_section)


def base_function(driver,dir,head_name,fiscal_year,hierarchy, table):
    '''
    Baisc function that calls all the other function and return the needed variables
    (driver = chromedriver, dir = parent directory, head_name = name of folder (name of head),
    fiscal_year = year selected,hierarchy = hierarchy string, table = selected table)
    '''
    path = path_generator_dir_maker(driver,dir,str(head_name))
    table_to_csv(driver,path,head_name,table)
    add_columns(driver,path,head_name,fiscal_year, hierarchy)
    (links_url_string,links_name,name_of_hierarchy) = sel_elem_to_links(driver,table)
    return(path,links_url_string,links_name,name_of_hierarchy)

table = driver.find_elements_by_id("myTable")[0]
(links_of_ddos_url_string,links_of_ddos_name, name_of_hierarchy_ddos) = sel_elem_to_links(driver,table)

for index_ddos, ddos_link in enumerate(links_of_ddos_url_string):
    driver.get(ddos_link)
    table = driver.find_elements_by_id("myTable")[0]
    hierarchy_ddos = name_of_hierarchy_ddos[index_ddos]
    (path_ddos,links_of_grants_url_string,links_of_grants_name, name_of_hierarchy_grants) = base_function(driver,parent_folder, links_of_ddos_name[index_ddos], fiscal_year, hierarchy_ddos, table)

    for index_grants, grants_link in enumerate(links_of_grants_url_string):
        driver.get(grants_link)
        table = driver.find_elements_by_id("myTable")[0]

        # Creating a hierarchy string
        hierarchy_grants = hierarchy_ddos + "$" + name_of_hierarchy_grants[index_grants]
        (path_grants,links_of_schemes_url_string,links_of_schemes_name,name_of_hierarchy_schemes) = base_function(driver,path_ddos, links_of_grants_name[index_grants], fiscal_year, hierarchy_grants, table)

        
        #adding a "-" to recognise all the repeating scheme codes uniquely
        for index, name in  enumerate(links_of_schemes_name):
            links_of_schemes_name[index] = name + "-" + str(index)
       
        for index_schemes, schemes_link in enumerate(links_of_schemes_url_string):
            print(links_of_schemes_name[index])
            driver.get(schemes_link)
            table = driver.find_elements_by_id("myTable")[0]
            hierarchy_schemes = hierarchy_grants+ "$" + name_of_hierarchy_schemes[index_schemes]
            (path_schemes,links_of_treasury_url_string,links_of_treasury_name, name_of_hierarchy_trea) = base_function(driver,path_grants, links_of_schemes_name[index_schemes], fiscal_year, hierarchy_schemes, table)

            for index_treasury, treasury_link in enumerate(links_of_treasury_url_string):

                print(links_of_treasury_name[index_treasury])

                driver.get(treasury_link)

                table = driver.find_elements_by_id("myTable")[0]

                hierarchy_trea = hierarchy_schemes+ "$" + name_of_hierarchy_trea[index_treasury]
                base_function(driver,path_schemes, links_of_treasury_name[index_treasury], fiscal_year, hierarchy_trea, table)
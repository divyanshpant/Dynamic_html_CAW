from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import json
 
# Opening JSON file
file = open('C:/Users/ddivy/OneDrive/Documents/VS CODE/Dynamic_html_CAW/data.json')
  
data = json.load(file)
json_string=json.dumps(data) #converting json to valid json string

options = Options()
options.add_argument("start-maximized") #Using this to start google in maximized screen

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30) #This wait is used to make the driver wait till the mentioned element is visible

url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
driver.get(url)

time.sleep(5)#This wait is explicit wait where driver has to wait for 10 seconds before executing next steps

try:
    table_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/details/summary'))) #Pointing driver to the "table data" button

    table_button.click() #clicking the "table data" button

    time.sleep(5)
    
    try:
        table = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jsondata"]'))) #Pointing driver to the dynamic HTML data table

        table.clear() #clearing the previous content of the data table

        #Entering the content to the data table
        table.send_keys(json_string)

        time.sleep(5)
        
        try:
            

            Refresh_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="refreshtable"]'))) #Pointing driver to click the "Refresh" button

            Refresh_button.click()

            time.sleep(10)

            print("After inserting data, clicked the refresh button")
        
        except:
            print("Unable to Click Refresh button")
    
    except:
        print("Unable to clear the table and push the Json string")
        
except:
    print("Unable to click table button")
    
    
driver.quit()
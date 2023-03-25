from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Orange_Data
from Test_Locators.locators import Orange_Locators
import pytest
import os
os.environ['GH_TOKEN'] = "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"

class Test_Orange:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    
    def test_searchmenuname(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Admin))).is_displayed() == True
        print("Admin option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).is_displayed() == True
        print("PIM option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Leave))).is_displayed() == True
        print("Leave option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Time))).is_displayed() == True
        print("Time option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Recruitment))).is_displayed() == True
        print("Recruitment option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Myinfo))).is_displayed() == True
        print("Myinfo option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Performance))).is_displayed() == True
        print("Performance option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dashboard))).is_displayed() == True
        print("Dashboard option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Directory))).is_displayed() == True
        print("Directory option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Maintenance))).is_displayed() == True
        print("Maintenance option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Buzz))).is_displayed() == True
        print("Buzz option is displayed on Side pane")
        searchmenu = wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().search_menu_textbox)))
        searchmenu.send_keys(Orange_Data().Admin)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Pim)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Leave)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Time)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Recruitment)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Myinfo)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Performance)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Dashboard)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Directory)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Maintenance)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        searchmenu.send_keys(Orange_Data().Buzz)
        searchmenu.send_keys(Keys.CONTROL + "a")
        searchmenu.send_keys(Keys.DELETE)
        assert self.driver.current_url.__contains__("index") == True
        print("Individual menu names displayed successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_adminpage(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Admin))).click()
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Admin))).is_displayed() == True
        print("Admin option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).is_displayed() == True
        print("PIM option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Leave))).is_displayed() == True
        print("Leave option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Time))).is_displayed() == True
        print("Time option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Recruitment))).is_displayed() == True
        print("Recruitment option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Myinfo))).is_displayed() == True
        print("Myinfo option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Performance))).is_displayed() == True
        print("Performance option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dashboard))).is_displayed() == True
        print("Dashboard option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Directory))).is_displayed() == True
        print("Directory option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Maintenance))).is_displayed() == True
        print("Maintenance option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Buzz))).is_displayed() == True
        print("Buzz option is displayed on Side pane")
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().User_management))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Users))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().User_role))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().userroleoption1))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().User_role))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().userroleoption1))).click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().User1_role))).text == 'Admin'
        print("Admin option is displayed")
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().User_role))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().userroleoption2))).click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().User1_role))).text == 'ESS'
        print("ESS option is displayed")
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Status))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().statusoption1))).click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Status1))).text == 'Enabled'
        print("Enabled option is diplayed")
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Status))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().statusoption2))).click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Status1))).text == 'Disabled'
        print("Disabled option is diplayed")
        assert self.driver.current_url.__contains__("viewSystemUsers") == True
        print("The values (Admin,ESS) and (Enabled,Disabled) are displayed Successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_createemployee(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by = By.NAME, value = Orange_Locators().username_input_box).send_keys(Orange_Data().username)
        self.driver.find_element(by = By.NAME, value = Orange_Locators().password_input_box).send_keys(Orange_Data().password)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().submit_button).click()
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().PIM).click()
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Add).click()
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().First_name).send_keys(Orange_Data().Firstname)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Middle_name).send_keys(Orange_Data().Middlename)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Last_name).send_keys(Orange_Data().Lastname)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().empid).send_keys(Orange_Data().empid)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Create_login_details).click()
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Username).send_keys(Orange_Data().loginUsername)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().password).send_keys(Orange_Data().loginPassword)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().confirmpassword).send_keys(Orange_Data().loginPassword)
        self.driver.find_element(by = By.XPATH, value = Orange_Locators().Save_button).click()
        sleep(5)
        assert self.driver.current_url.__contains__("pim") == True
        print("Creation of Employee successful")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_editemployee(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Personal_Details))).is_displayed() == True
        print("Personal Deatils option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Contact_Details))).is_displayed() == True
        print("Contact Details option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Emergency_Contacts))).is_displayed() == True
        print("Emergency Contacts option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dependents))).is_displayed() == True
        print("Dependents option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().immigration))).is_displayed() == True
        print("Immigration option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Job))).is_displayed() == True
        print("Job option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Salary))).is_displayed() == True
        print("Salary option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Tax_Exemptions))).is_displayed() == True
        print("Tax Exemptions option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Report_to))).is_displayed() == True
        print("Report to option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Qualifications))).is_displayed() == True
        print("Qualifications option is displayed on Side pane")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Memberships))).is_displayed() == True
        print("Memberships option is displayed on Side pane")
        assert self.driver.current_url.__contains__("viewPersonalDetails") == True
        print("All the tabs are present in Employee List Page")
     except NoSuchElementException:
        print("No such Element found")
        
    def test_personaldetails(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Nickname))).send_keys(Orange_Data.Nickname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().license))).send_keys(Orange_Data.Driverslicense)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().license_expiry))).send_keys(Orange_Data.License_expiry)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().SIN))).send_keys(Orange_Data.SIN)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_dropdown))).click()
        for e in range(3):
         actions.send_keys('i')
         actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_dropdown))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Marital_status))).click()
        actions.send_keys('s')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Marital_status))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().DOB))).send_keys(Orange_Data.DOB)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Gender_radiobutton))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Military_Service))).send_keys(Orange_Data.Military_Service)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Smoker))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Edit_submit_button))).click()
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_dropdown))).text == 'Indian'
        print("Employee Personal Details Edited Successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_contactdetails(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Contact_Details))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Street1))).send_keys(Orange_Data.Street1)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Street2))).send_keys(Orange_Data.Street2)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().City))).send_keys(Orange_Data.City)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().State))).send_keys(Orange_Data.State)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Zip))).send_keys(Orange_Data.Zip)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_Contact))).click()
        for e in range(2):
         actions.send_keys('i')
         actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_Contact))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Mobile))).send_keys(Orange_Data.Mobile)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Work_email))).send_keys(Orange_Data.Work_email)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().other_email))).send_keys(Orange_Data.other_email)
        sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Submit_button_contact))).click()
        sleep(3)
        assert wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Nationality_Contact))).text == 'India'
        print("Employee Contact Details Edited Successfully")
     except NoSuchElementException:
        print("No such Element found")
        
    def test_emergencydetails(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Emergency_Contacts))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Emergecy_add_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Emergency_name))).send_keys(Orange_Data.Emergency_name)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Relationship))).send_keys(Orange_Data.Relationship)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Emergency_Mobile))).send_keys(Orange_Data.Emergency_Mobile)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Submit_button_emergency))).click()
        assert self.driver.current_url.__contains__("viewEmergencyContacts") == True
        print("Emergency Contact Details filled Successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_employeedependents(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Dependents))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Dependents_add_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dependents_Name))).send_keys(Orange_Data.Dependents_Name)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dependents_Relationship))).click()
        actions.send_keys('o')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Dependents_Relationship))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Dependents_specify))).send_keys(Orange_Data.Dependents_specify)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Dependents_DOB))).send_keys(Orange_Data.Dependents_DOB)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Submit_button_dependents))).click()
        sleep(4)
        assert self.driver.current_url.__contains__("viewDependents") == True
        print("Dependent Details filled Successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_jobdetails(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Job))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Job_joined_date))).send_keys(Orange_Data.Job_joined_date)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Job_title))).click()
        actions.send_keys('q')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Job_title))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Job_category))).click()
        actions.send_keys('p')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Job_category))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Subunit))).click()
        actions.send_keys('e')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Subunit))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Location))).click()
        actions.send_keys('h')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Location))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employment_status))).click()
        actions.send_keys('p')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Employment_status))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Include_Employement_contract_details))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Contract_start_date))).send_keys(Orange_Data.Contract_start_date)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Contract_end_date))).send_keys(Orange_Data.Contract_end_date)
        sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Submit_button_jobdetails))).click()
        sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Submit_button_jobdetails))).is_displayed()
        assert self.driver.current_url.__contains__("viewJobDetails") == True
        print("Employee Job Details filled Successfully") 
     except NoSuchElementException:
        print("No such Element found")
    
    def test_terminateemployee(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Job))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Terminate_employement))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Termination_Date))).send_keys(Orange_Data.Termination_Date)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Termination_reason))).click()
        actions.send_keys('o')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Termination_reason))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Submit_button_termination))).click()
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().termination_date))).is_displayed() == True
        print("Termination date is displayed")
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Activate_Employement))).is_displayed() == True
        print("Employee has been terminated successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_activateemployee(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Job))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Terminate_employement))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Termination_Date))).send_keys(Orange_Data.Termination_Date)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Termination_reason))).click()
        actions.send_keys('o')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Termination_reason))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Submit_button_termination))).click()
        sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().Activate_Employement))).click()
        sleep(2)
        assert wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Terminate_employement))).is_displayed() == True
        print("Employee has been activated successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_employeesalary(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).is_displayed()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Salary))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Add_salary_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().salary_component))).send_keys(Orange_Data.Salary_component)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().pay_grade))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().pg1))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().pay_frequency))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().pf1))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().currency))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().cur1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().amount))).send_keys(Orange_Data.Amount)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Direct_depost_details))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().account_number))).send_keys(Orange_Data.Account_number)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().account_type))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().s1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().routing_number))).send_keys(Orange_Data.Routing_number)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().DD_amount))).send_keys(Orange_Data.DD_amount)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().submit_button_salary))).click()
        sleep(2)
        assert self.driver.current_url.__contains__("viewSalaryList") == True
        print("Employee Salary Details filled Successfully")
     except NoSuchElementException:
        print("No such Element found")
    
    def test_taxexemptions(self, boot):
     try:
        self.driver.get(Orange_Data().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)
        actions = ActionChains(self.driver)
        wait.until(EC.element_to_be_clickable((By.NAME, Orange_Locators().username_input_box))).send_keys(Orange_Data().username)
        wait.until(EC.presence_of_element_located((By.NAME, Orange_Locators().password_input_box))).send_keys(Orange_Data().password)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().submit_button))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().PIM))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Employee_info_name))).send_keys(Orange_Data.Employee_info_searchname)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Search_button))).click()
        sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Record_1))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Tax_Exemptions))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Federal_tax_status))).click()
        actions.send_keys('m')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Federal_tax_status))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Exemptions))).send_keys(Orange_Data.Exemptions)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().State_tax))).click()
        actions.send_keys('g')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().State_tax))).send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Status_tax))).click()
        actions.send_keys('m')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Status_tax))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, Orange_Locators().Exemptions2))).send_keys(Orange_Data.Exemptions2)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Unemployment_state))).click()
        actions.send_keys('g')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Unemployment_state))).send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Work_state))).click()
        actions.send_keys('g')
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.XPATH, Orange_Locators().Work_state))).send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH, Orange_Locators().submit_button_tax))).click()
        assert self.driver.current_url.__contains__("viewUsTaxExemptions") == True
        print("Employee Tax Details filled Successfully")
     except NoSuchElementException:
        print("No such Element found")

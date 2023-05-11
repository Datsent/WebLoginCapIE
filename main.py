from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import mouse


#Hellodfsg
def login_screen():
    ieOptions = webdriver.IeOptions()
    ieOptions.add_additional_option("ie.edgechromium", True)
    ieOptions.add_additional_option("ie.edgepath",'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe') # Path exe file of Edge
    ieOptions.add_additional_option("ignoreProtectedModeSettings", True)
    ieOptions.add_additional_option("disable-infobars", True)    

    driver = webdriver.Ie(options=ieOptions)
    driver.get('http://******/Login')    
    driver.find_element_by_id("Username").send_keys(Keys.F11)  
    driver.execute_script("document.getElementById('Username').setAttribute('value','Admin')");
    driver.execute_script("document.getElementById('Password').setAttribute('value','Admin')");
    driver.find_element_by_id("LoginBtn").click()
    driver.get('http://*******/p?D=MonitorSupport%7CIDCIPTACCS%7C9%7CCC%7CPrivate_Collection%7C6')
    mouse.mouse_move()
    
    
if __name__ == '__main__':
    login_screen()







    
    
    
    
    




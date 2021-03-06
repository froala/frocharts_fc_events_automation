
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from Util import Validate as val
from Util import Report as report
from Events import pomFile as pom
import time
import csv


def f_rotationend(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.rotationend.eObj.eventType")
        eventId= driver.execute_script("return events.rotationend.eObj.eventId")
        cancelled= driver.execute_script("return events.rotationend.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.rotationend.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.rotationend.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.rotationend.eObj.preventDefault")
        detached= driver.execute_script("return events.rotationend.eObj.detached")
        detachHandler= driver.execute_script("return events.rotationend.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.rotationend.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.rotationend.eObj.data.startingAngle")
        dObj2= driver.execute_script("return events.rotationend.eObj.data.changeInAngle")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "rotationend":
            obj_param="eventType = ",eventType
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('rotationend', obj_param, chartType, "PASS")
        except:
            report.entry_csv('rotationend', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_number(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "startingAngle should be number",chartType , "FAIL")
        
        
        if val.check_if_number(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('rotationend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rotationend', "changeInAngle should be number",chartType , "FAIL")    
            

            
    except Exception as e:
        report.entry_csv('rotationend', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

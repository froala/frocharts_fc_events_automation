
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


def f_dataloaded(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataloaded.eObj.eventType")
        eventId= driver.execute_script("return events.dataloaded.eObj.eventId")
        cancelled= driver.execute_script("return events.dataloaded.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataloaded.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataloaded.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataloaded.eObj.preventDefault")
        detached= driver.execute_script("return events.dataloaded.eObj.detached")
        detachHandler= driver.execute_script("return events.dataloaded.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataloaded.eObj.sender.chartType()")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataloaded":
            obj_param="eventType = ",eventType
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataloaded', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == "pie":
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataloaded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaded', "senderChartType is not correct",chartType , "FAIL")
        
            
            
            
        

            
    except Exception as e:
        report.entry_csv('dataloaded', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

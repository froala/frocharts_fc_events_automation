
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
import time
import csv
import pdb

def f_ready(driver, chartType):
    

    time.sleep(4)
    
    report.jsError_exists(chartType)


    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.ready.eObj.eventType")
    eventId= driver.execute_script("return events.ready.eObj.eventId")
    cancelled= driver.execute_script("return events.ready.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.ready.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.ready.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.ready.eObj.preventDefault")
    detached= driver.execute_script("return events.ready.eObj.detached")
    detachHandler= driver.execute_script("return events.ready.eObj.detachHandler")
    senderChartType= driver.execute_script("return events.ready.eObj.sender.id")
    dObj1= driver.execute_script("return events.ready.eObj.data.now")
    
    
    
    
    #Validating all the attributes whether their values fetched are correct for the particular event
    
    if eventType == "ready":
        obj_param="eventType = ",eventType
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('ready', obj_param, chartType, "PASS")
    except:
        report.entry_csv('ready', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "preventDefault is not a function",chartType , "FAIL")
            
            
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "detached is not boolean",chartType , "FAIL")
            
    
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "detachHandler is not a function",chartType , "FAIL")
            
            
            
    if senderChartType == "FroalaCharts":
        obj_param="senderChartType = ",senderChartType
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "senderChartType is not correct",chartType , "FAIL")
        print senderChartType
    
    
    
    if dObj1 == True:
        obj_param="dObj1 = ",dObj1
        report.entry_csv('ready', obj_param, chartType, "PASS")
    else:
        report.entry_csv('ready', "dObj1 is not correct",chartType , "FAIL")
        print dObj1
        
"""    
except Exception as e:
    report.entry_csv('ready', "ERROR: There is an issue with event objects",chartType , "FAIL")
    print e"""
        
        
        
        
    
    
    
    
    
    


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


def f_loaded(driver, chartType):
    

    time.sleep(2)
    
    report.jsError_exists(chartType)
    
    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.loaded.eObj.eventType")
    eventId= driver.execute_script("return events.loaded.eObj.eventId")
    cancelled= driver.execute_script("return events.loaded.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.loaded.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.loaded.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.loaded.eObj.preventDefault")
    detached= driver.execute_script("return events.loaded.eObj.detached")
    detachHandler= driver.execute_script("return events.loaded.eObj.detachHandler")
    senderChartType= driver.execute_script("return events.loaded.eObj.sender.chartType()")
    dObj1= driver.execute_script("return events.loaded.eObj.data.renderer")
    dObj2= driver.execute_script("return events.loaded.eObj.data.type")
    
    #Validating all the attributes whether their values fetched are correct for the particular event
    
    if eventType == "loaded":
        obj_param="eventType = ",eventType
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('loaded', obj_param, chartType, "PASS")
    except:
        report.entry_csv('loaded', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "preventDefault is not a function",chartType , "FAIL")
            
            
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "detached is not boolean",chartType , "FAIL")
            
    
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "detachHandler is not a function",chartType , "FAIL")
            
            
            
    if senderChartType == chartType:
        obj_param="senderChartType = ",senderChartType
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "senderChartType is not correct",chartType , "FAIL")
        print senderChartType
    
    
    
    
    if dObj1 =="javascript":
        obj_param="renderer = ",dObj1
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "dObj1 is not correct",chartType , "FAIL")
        print dObj1
        
        
    if dObj2 == chartType:
        obj_param="type = ",dObj2
        report.entry_csv('loaded', obj_param, chartType, "PASS")
    else:
        report.entry_csv('loaded', "dObj2 is not correct",chartType , "FAIL")
        print dObj2
        
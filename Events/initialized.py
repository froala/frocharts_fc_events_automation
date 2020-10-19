
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


def f_initialized(driver, chartType):
    

    time.sleep(2)
    
    report.jsError_exists(chartType)

    
    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.initialized.eObj.eventType")
    eventId= driver.execute_script("return events.initialized.eObj.eventId")
    cancelled= driver.execute_script("return events.initialized.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.initialized.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.initialized.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.initialized.eObj.preventDefault")
    detached= driver.execute_script("return events.initialized.eObj.detached")
    detachHandler= driver.execute_script("return events.initialized.eObj.detachHandler")
    senderChartType= driver.execute_script("return events.initialized.eObj.sender.chartType()")
    dObj1= driver.execute_script("return events.initialized.eObj.data.dataFormat")
    dObj2= driver.execute_script("return events.initialized.eObj.data.dataSource")
    dObj3= driver.execute_script("return events.initialized.eObj.data.height")
    dObj4= driver.execute_script("return events.initialized.eObj.data.renderAt")
    dObj5= driver.execute_script("return events.initialized.eObj.data.type")
    dObj6= driver.execute_script("return events.initialized.eObj.data.width")
    
    #Validating all the attributes whether their values fetched are correct for the particular event
    
    if eventType == "initialized":
        obj_param="eventType = ",eventType
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('initialized', obj_param, chartType, "PASS")
    except:
        report.entry_csv('initialized', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "preventDefault is not a function",chartType , "FAIL")
            
            
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "detached is not boolean",chartType , "FAIL")
            
    
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "detachHandler is not a function",chartType , "FAIL")
            
            
            
    if senderChartType == chartType:
        obj_param="senderChartType = ",senderChartType
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "senderChartType is not correct",chartType , "FAIL")
        print senderChartType
    
    
    
    if dObj1.lower() == "json":
        obj_param="dataFormat = ",dObj1
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj1 is not correct",chartType , "FAIL")
        print dObj1
        
        
    if val.check_if_not_empty_string(dObj2): 
        obj_param="dataSource = ",dObj2
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj2 is not correct",chartType , "FAIL")
        print dObj2
        
        
    if val.check_if_int(dObj3):
        obj_param="height = ",dObj3
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj3 is not correct",chartType , "FAIL")
        print dObj3
        
    if dObj4 == "chart-container":
        obj_param="renderAt = ",dObj4
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj4 is not correct",chartType , "FAIL")
        print dObj4
        
    if dObj5 == chartType:
        obj_param="type = ",dObj5
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj5 is not correct",chartType , "FAIL")
        print dObj5
        
    if val.check_if_int(dObj6):
        obj_param="width = ",dObj6
        report.entry_csv('initialized', obj_param, chartType, "PASS")
    else:
        report.entry_csv('initialized', "dObj6 is not correct",chartType , "FAIL")
        print dObj6
       
        
        
    
    
    
    
    
    

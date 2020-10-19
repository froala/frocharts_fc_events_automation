
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



def f_beforeInitialize(driver, chartType):
    

    time.sleep(4)
    
    report.jsError_exists(chartType)

    
    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.beforeinitialize.eObj.eventType")
    eventId= driver.execute_script("return events.beforeinitialize.eObj.eventId")
    cancelled= driver.execute_script("return events.beforeinitialize.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.beforeinitialize.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.beforeinitialize.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.beforeinitialize.eObj.preventDefault")
    detached= driver.execute_script("return events.beforeinitialize.eObj.detached")
    detachHandler= driver.execute_script("return events.beforeinitialize.eObj.detachHandler")
    senderChartType= driver.execute_script("return events.beforeinitialize.eObj.sender.chartType()")
    dObj1= driver.execute_script("return events.beforeinitialize.eObj.data.dataFormat")
    dObj2= driver.execute_script("return JSON.stringify(events.beforeinitialize.eObj.data.dataSource)")
    dObj3= driver.execute_script("return events.beforeinitialize.eObj.data.height")
    dObj4= driver.execute_script("return events.beforeinitialize.eObj.data.renderAt")
    dObj5= driver.execute_script("return events.beforeinitialize.eObj.data.type")
    dObj6= driver.execute_script("return events.beforeinitialize.eObj.data.width")

    # obj2 = str(dObj2)
    obj2 = dObj2.encode('utf-8\xb0')

    #Validating all the attributes whether their values fetched are correct for the particular event
    
    if eventType == "beforeinitialize":
        obj_param="eventType = ",eventType
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    except:
        report.entry_csv('beforeinitialize', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "preventDefault is not a function",chartType , "FAIL")
            
            
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "detached is not boolean",chartType , "FAIL")
            
    
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "detachHandler is not a function",chartType , "FAIL")
            
            
            
    if senderChartType == chartType:
        obj_param="senderChartType = ",senderChartType
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "senderChartType is not correct",chartType , "FAIL")
    

    
    if dObj1.lower() == 'json' :

        obj_param="dataFormat = ",dObj1
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj1 is not correct",chartType , "FAIL")
        
        
        
    if val.check_if_not_empty_string(obj2):
        obj_param="dataSource = ",dObj2
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj2 is not correct",chartType , "FAIL")
        
        
        
    if val.check_if_int(dObj3):
        obj_param="height = ",dObj3
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj3 is not correct",chartType , "FAIL")
        
        
        
    if dObj4 == "chart-container":
        obj_param="renderAt = ",dObj4
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj4 is not correct",chartType , "FAIL")
        
        
        
    if dObj5 == chartType:
        obj_param="type = ",dObj5
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj5 is not correct",chartType , "FAIL")

        
        
    if val.check_if_int(dObj6):
        obj_param="width = ",dObj6
        report.entry_csv('beforeinitialize', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforeinitialize', "dObj6 is not correct",chartType , "FAIL")


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


def f_beforeRender(driver, chartType):
    

    time.sleep(2)
    
    report.jsError_exists(chartType)
    
    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.beforerender.eObj.eventType")
    eventId= driver.execute_script("return events.beforerender.eObj.eventId")
    cancelled= driver.execute_script("return events.beforerender.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.beforerender.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.beforerender.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.beforerender.eObj.preventDefault")
    detached= driver.execute_script("return events.beforerender.eObj.detached")
    detachHandler= driver.execute_script("return events.beforerender.eObj.detachHandler")
    senderChartType= driver.execute_script("return events.beforerender.eObj.sender.chartType()")
    dObj1= driver.execute_script("return events.beforerender.eObj.data.container.id")
    dObj2= driver.execute_script("return events.beforerender.eObj.data.height")
    dObj3= driver.execute_script("return events.beforerender.eObj.data.renderer")
    dObj4= driver.execute_script("return events.beforerender.eObj.data.width")
    
    
    print "dObj1=",dObj1
    
    #Validating all the attributes whether their values fetched are correct for the particular event
    
    if eventType == "beforerender":
        obj_param="eventType = ",eventType
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('beforerender', obj_param, chartType, "PASS")
    except:
        report.entry_csv('beforerender', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "preventDefault is not a function",chartType , "FAIL")
            
            
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "detached is not boolean",chartType , "FAIL")
            
    
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "detachHandler is not a function",chartType , "FAIL")
            
            
            
    if senderChartType == chartType:
        obj_param="senderChartType = ",senderChartType
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "senderChartType is not correct",chartType , "FAIL")
        print senderChartType
    
    
    
    
    if dObj1 =="chart-container":
        obj_param="Container = ",dObj1
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "dObj1 is not correct",chartType , "FAIL")
        print dObj1
        
        
    if val.check_if_int(dObj2):
        obj_param="height = ",dObj2
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "dObj2 is not correct",chartType , "FAIL")
        print dObj2
        
    if dObj3 == "javascript":
        obj_param="rendered = ",dObj3
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "dObj3 is not correct",chartType , "FAIL")
        print dObj3
        
    if val.check_if_int(dObj4):
        obj_param="width = ",dObj4
        report.entry_csv('beforerender', obj_param, chartType, "PASS")
    else:
        report.entry_csv('beforerender', "dObj4 is not correct",chartType , "FAIL")
        print dObj4
       
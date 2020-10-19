
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


def f_overlaybuttonclick(driver, chartType):
    
    #try:

    time.sleep(2)
    
    report.jsError_exists(chartType)
    
    #Assigning each of the event specific attributes to different variables  
    eventType= driver.execute_script("return events.overlaybuttonclick.eObj.eventType")
    eventId= driver.execute_script("return events.overlaybuttonclick.eObj.eventId")
    cancelled= driver.execute_script("return events.overlaybuttonclick.eObj.cancelled")
    stopPropagation= driver.execute_script("return events.overlaybuttonclick.eObj.stopPropagation")
    defaultPrevented= driver.execute_script("return events.overlaybuttonclick.eObj.defaultPrevented")
    preventDefault= driver.execute_script("return events.overlaybuttonclick.eObj.preventDefault")
    detached= driver.execute_script("return events.overlaybuttonclick.eObj.detached")
    detachHandler= driver.execute_script("return events.overlaybuttonclick.eObj.detachHandler")
    disposed= driver.execute_script("return events.overlaybuttonclick.eObj.sender.disposed")
    id= driver.execute_script("return events.overlaybuttonclick.eObj.data.id")
    show= driver.execute_script("return events.overlaybuttonclick.eObj.data.show")
    
    #Validating all the attributes whether their values fetched are correct for the particular event
    chartType = chartType.replace('_linkeditem','')
    
    if eventType == "overlaybuttonclick":
        obj_param="eventType = ",eventType
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "eventType is not correct",chartType , "FAIL")
    
    
    try:
        if val.check_if_int(eventId):
            obj_param="eventId = ",eventId
            report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    except:
        report.entry_csv('overlaybuttonclick', "eventId is not an int",chartType , "FAIL")
    
    
    
    if val.check_if_boolean(cancelled):
        obj_param="cancelled = ",cancelled
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "cancelled is not boolean",chartType , "FAIL")
    
    
    
    if val.check_if_function(stopPropagation):
        obj_param="stopPropagation = ",stopPropagation
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "stopPropagation is not a function",chartType , "FAIL")
            
           
    
    
    if val.check_if_boolean(defaultPrevented):
            obj_param="defaultPrevented = ",defaultPrevented
            report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "defaultPrevented is not boolean",chartType , "FAIL") 
        
        
        
    if val.check_if_function(preventDefault):
            obj_param="preventDefault = ",preventDefault
            report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "preventDefault is not a function",chartType , "FAIL")
            
    
    if val.check_if_boolean(detached):
        obj_param="detached = ",detached
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "detached is not boolean",chartType , "FAIL")
    
    
    if val.check_if_function(detachHandler):
        obj_param="detachHandler = ",detachHandler
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "detachHandler is not a function",chartType , "FAIL")
            
            
    if val.check_if_boolean(disposed):
        obj_param="disposed = ",disposed
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "senderChartType is not correct",chartType , "FAIL")
     
     
    if val.check_if_not_empty_string(id):
        obj_param="id = ",id
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "id is not correct",chartType , "FAIL")
        print id 
        
    if val.check_if_not_empty_string(show):
        obj_param="show = ",show
        report.entry_csv('overlaybuttonclick', obj_param, chartType, "PASS")
    else:
        report.entry_csv('overlaybuttonclick', "show is not correct",chartType , "FAIL")
        print show            
               
#     except Exception as e:
#         report.entry_csv('overlaybuttonclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
#         print e

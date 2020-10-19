
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


def f_containernotfound(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.containernotfound.eObj.eventType")
        eventId= driver.execute_script("return events.containernotfound.eObj.eventId")
        cancelled= driver.execute_script("return events.containernotfound.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.containernotfound.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.containernotfound.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.containernotfound.eObj.preventDefault")
        detached= driver.execute_script("return events.containernotfound.eObj.detached")
        detachHandler= driver.execute_script("return events.containernotfound.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.containernotfound.eObj.sender.chartType()")
        
        chartType = chartType.replace('_noContainer','')
        
         
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "containernotfound":
            obj_param="eventType = ",eventType
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        except:
            report.entry_csv('containernotfound', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "detached is not boolean",chartType , "FAIL")
               
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('containernotfound', obj_param, chartType, "PASS")
        else:
            report.entry_csv('containernotfound', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
         
#          
#         if val.check_if_not_empty_string(data):
#             obj_param="data = ",data
#             report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('dataplotclick', "data is not correct",chartType , "FAIL")
#             print data
#             
               
    except Exception as e:
        report.entry_csv('containernotfound', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

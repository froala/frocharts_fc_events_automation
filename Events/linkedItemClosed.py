
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


def f_linkeditemclosed(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.linkeditemclosed.eObj.eventType")
        eventId= driver.execute_script("return events.linkeditemclosed.eObj.eventId")
        cancelled= driver.execute_script("return events.linkeditemclosed.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.linkeditemclosed.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.linkeditemclosed.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.linkeditemclosed.eObj.preventDefault")
        detached= driver.execute_script("return events.linkeditemclosed.eObj.detached")
        detachHandler= driver.execute_script("return events.linkeditemclosed.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.linkeditemclosed.eObj.sender.chartType()")
        
        level= driver.execute_script("return events.linkeditemclosed.eObj.data.level")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        chartType = chartType.replace('_linkeditem','')
        
        if eventType == "linkeditemclosed":
            obj_param="eventType = ",eventType
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        except:
            report.entry_csv('linkeditemclosed', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "detachHandler is not a function",chartType , "FAIL")
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
         
            
        if val.check_if_int(level):
            obj_param="level = ",level
            report.entry_csv('linkeditemclosed', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkeditemclosed', "level is not correct",chartType , "FAIL")
            print level            
               
    except Exception as e:
        report.entry_csv('linkeditemclosed', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

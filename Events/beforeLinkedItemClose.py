
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


def f_beforelinkeditemclose(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.beforelinkeditemclose.eObj.eventType")
        eventId= driver.execute_script("return events.beforelinkeditemclose.eObj.eventId")
        cancelled= driver.execute_script("return events.beforelinkeditemclose.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.beforelinkeditemclose.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.beforelinkeditemclose.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.beforelinkeditemclose.eObj.preventDefault")
        detached= driver.execute_script("return events.beforelinkeditemclose.eObj.detached")
        detachHandler= driver.execute_script("return events.beforelinkeditemclose.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.beforelinkeditemclose.eObj.sender.chartType()")
        
        item= driver.execute_script("return events.beforelinkeditemclose.eObj.data.item")
        level= driver.execute_script("return events.beforelinkeditemclose.eObj.data.level")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        chartType = chartType.replace('_linkeditem','')
        
        if eventType == "beforelinkeditemclose":
            obj_param="eventType = ",eventType
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforelinkeditemclose', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "detachHandler is not a function",chartType , "FAIL")
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
         
         
        if val.check_if_not_empty_string(item):
            obj_param="item = ",item
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "item is not correct",chartType , "FAIL")
            print item 
            
        if val.check_if_int(level):
            obj_param="level = ",level
            report.entry_csv('beforelinkeditemclose', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforelinkeditemclose', "level is not correct",chartType , "FAIL")
            print level            
               
    except Exception as e:
        report.entry_csv('beforelinkeditemclose', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

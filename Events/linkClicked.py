
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


def f_linkclicked(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.linkclicked.eObj.eventType")
        eventId= driver.execute_script("return events.linkclicked.eObj.eventId")
        cancelled= driver.execute_script("return events.linkclicked.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.linkclicked.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.linkclicked.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.linkclicked.eObj.preventDefault")
        detached= driver.execute_script("return events.linkclicked.eObj.detached")
        detachHandler= driver.execute_script("return events.linkclicked.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.linkclicked.eObj.sender.chartType()")
        
        linkAction= driver.execute_script("return events.linkclicked.eObj.data.linkAction")
        linkInvoked= driver.execute_script("return events.linkclicked.eObj.data.linkInvoked")
        linkProvided= driver.execute_script("return events.linkclicked.eObj.data.linkProvided")
        
        chartType = chartType.replace('_link','')
        
        #VallinkProvidedating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "linkclicked":
            obj_param="eventType = ",eventType
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        except:
            report.entry_csv('linkclicked', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
          
            
        if val.check_if_not_empty_string(linkInvoked):
            obj_param="linkInvoked = ",linkInvoked
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "linkInvoked is not correct",chartType , "FAIL")
            print linkInvoked
          
        if val.check_if_not_empty_string(linkAction):
            obj_param="linkAction = ",linkAction
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "linkAction is not correct",chartType , "FAIL")
            print linkAction
            
        if val.check_if_not_empty_string(linkProvided):
            obj_param="linkProvided = ",linkProvided
            report.entry_csv('linkclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkclicked', "linkProvided is not correct",chartType , "FAIL")
            print linkProvided
              
               
    except Exception as e:
        report.entry_csv('linkclicked', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e


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


def f_labeladded(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.labeladded.eObj.eventType")
        eventId= driver.execute_script("return events.labeladded.eObj.eventId")
        cancelled= driver.execute_script("return events.labeladded.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.labeladded.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.labeladded.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.labeladded.eObj.preventDefault")
        detached= driver.execute_script("return events.labeladded.eObj.detached")
        detachHandler= driver.execute_script("return events.labeladded.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.labeladded.eObj.sender.chartType()")
        
        allowdrag= driver.execute_script("return events.labeladded.eObj.data.allowdrag")
        link= driver.execute_script("return events.labeladded.eObj.data.link")
        sourceType = driver.execute_script("return events.labeladded.eObj.data.sourceType")
        text= driver.execute_script("return events.labeladded.eObj.data.text")
        x = driver.execute_script("return events.labeladded.eObj.data.x")
        y =driver.execute_script("return events.labeladded.eObj.data.y")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "labeladded":
            obj_param="eventType = ",eventType
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('labeladded', obj_param, chartType, "PASS")
        except:
            report.entry_csv('labeladded', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        
        if val.check_if_int(allowdrag):
            obj_param="allowdrag = ",allowdrag
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "allowdrag is not correct",chartType , "FAIL")
            print allowdrag
                   
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "link is not correct",chartType , "FAIL")
            print link
             
        if val.check_if_not_empty_string(sourceType):
            obj_param="sourceType = ",sourceType
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "sourceType is not correct",chartType , "FAIL")
            print sourceType
        
        if val.check_if_not_empty_string(text):
            obj_param="text = ",text
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "text is not correct",chartType , "FAIL")
            print text
            
        if val.check_if_int(x):
            obj_param="x = ",x
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "x is not correct",chartType , "FAIL")
            print x
            
        if val.check_if_int(y):
            obj_param="y = ",y
            report.entry_csv('labeladded', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeladded', "y is not correct",chartType , "FAIL")
            print y
    except Exception as e:
        report.entry_csv('labeladded', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

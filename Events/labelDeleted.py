
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


def f_labeldeleted(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.labeldeleted.eObj.eventType")
        eventId= driver.execute_script("return events.labeldeleted.eObj.eventId")
        cancelled= driver.execute_script("return events.labeldeleted.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.labeldeleted.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.labeldeleted.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.labeldeleted.eObj.preventDefault")
        detached= driver.execute_script("return events.labeldeleted.eObj.detached")
        detachHandler= driver.execute_script("return events.labeldeleted.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.labeldeleted.eObj.sender.chartType()")
        
        allowdrag= driver.execute_script("return events.labeldeleted.eObj.data.allowdrag")
        link= driver.execute_script("return events.labeldeleted.eObj.data.link")
        sourceType = driver.execute_script("return events.labeldeleted.eObj.data.sourceType")
        text= driver.execute_script("return events.labeldeleted.eObj.data.text")
        x = driver.execute_script("return events.labeldeleted.eObj.data.x")
        y =driver.execute_script("return events.labeldeleted.eObj.data.y")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "labeldeleted":
            obj_param="eventType = ",eventType
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        except:
            report.entry_csv('labeldeleted', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        
        if val.check_if_int(allowdrag):
            obj_param="allowdrag = ",allowdrag
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "allowdrag is not correct",chartType , "FAIL")
            print allowdrag
                   
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "link is not correct",chartType , "FAIL")
            print link
             
        if val.check_if_not_empty_string(sourceType):
            obj_param="sourceType = ",sourceType
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "sourceType is not correct",chartType , "FAIL")
            print sourceType
        
        if val.check_if_not_empty_string(text):
            obj_param="text = ",text
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "text is not correct",chartType , "FAIL")
            print text
            
        if val.check_if_int(x):
            obj_param="x = ",x
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "x is not correct",chartType , "FAIL")
            print x
            
        if val.check_if_int(y):
            obj_param="y = ",y
            report.entry_csv('labeldeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldeleted', "y is not correct",chartType , "FAIL")
            print y
    except Exception as e:
        report.entry_csv('labeldeleted', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

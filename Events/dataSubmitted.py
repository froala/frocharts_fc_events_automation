
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
from Events import pomFile as pom
import time
import csv


def f_datasubmitted(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.datasubmitted.eObj.eventType")
        eventId= driver.execute_script("return events.datasubmitted.eObj.eventId")
        cancelled= driver.execute_script("return events.datasubmitted.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.datasubmitted.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.datasubmitted.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.datasubmitted.eObj.preventDefault")
        detached= driver.execute_script("return events.datasubmitted.eObj.detached")
        detachHandler= driver.execute_script("return events.datasubmitted.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.datasubmitted.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.datasubmitted.eObj.data.data")
        dObj2= driver.execute_script("return events.datasubmitted.eObj.data.response")
        dObj3= driver.execute_script("return events.datasubmitted.eObj.data.url")
        dObj4= driver.execute_script("return events.datasubmitted.eObj.data.xhrObject.open")
        
        
        
        chartType=chartType.replace('_sub','')

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "datasubmitted":
            obj_param="eventType = ",eventType
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        except:
            report.entry_csv('datasubmitted', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "data is not valid",chartType , "FAIL")
            
            
            
        if not val.check_if_not_empty_string(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "response not correct",chartType , "FAIL")
            
            
        
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "url is not empty",chartType , "FAIL")
            
            
            
        if val.check_if_boolean(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('datasubmitted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitted', "xhrObject open should be boolean",chartType , "FAIL")
            
        

            
    except Exception as e:
        report.entry_csv('datasubmitted', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

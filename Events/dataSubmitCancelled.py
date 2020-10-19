
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


def f_datasubmitcancelled(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.datasubmitcancelled.eObj.eventType")
        eventId= driver.execute_script("return events.datasubmitcancelled.eObj.eventId")
        cancelled= driver.execute_script("return events.datasubmitcancelled.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.datasubmitcancelled.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.datasubmitcancelled.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.datasubmitcancelled.eObj.preventDefault")
        detached= driver.execute_script("return events.datasubmitcancelled.eObj.detached")
        detachHandler= driver.execute_script("return events.datasubmitcancelled.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.datasubmitcancelled.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.datasubmitcancelled.eObj.data.data")
        
        
        
        chartType=chartType.replace('_canc','')

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "datasubmitcancelled":
            obj_param="eventType = ",eventType
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('datasubmitcancelled', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('datasubmitcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datasubmitcancelled', "data is empty",chartType , "FAIL")
            
            
            
        

            
    except Exception as e:
        report.entry_csv('datasubmitcancelled', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

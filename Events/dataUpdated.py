
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


def f_dataupdated(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataupdated.eObj.eventType")
        eventId= driver.execute_script("return events.dataupdated.eObj.eventId")
        cancelled= driver.execute_script("return events.dataupdated.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataupdated.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataupdated.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataupdated.eObj.preventDefault")
        detached= driver.execute_script("return events.dataupdated.eObj.detached")
        detachHandler= driver.execute_script("return events.dataupdated.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataupdated.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.dataupdated.eObj.data.data.chart.bgimage")
        dObj2= driver.execute_script("return events.dataupdated.eObj.data.format")
        dObj3= driver.execute_script("return events.dataupdated.eObj.data.dataFormat")
        dObj4= driver.execute_script("return events.dataupdated.eObj.data.silent")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataupdated":
            obj_param="eventType = ",eventType
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataupdated', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == "pie":
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "chart bgimage link is empty",chartType , "FAIL")
            
            
            
        if dObj2 == "json":
            obj_param="dObj2 = ",dObj2
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "format is not correct",chartType , "FAIL")
            
            
        
        if dObj3 == "json":
            obj_param="dObj3 = ",dObj3
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "dataformat is not correct",chartType , "FAIL")
            
        
        if val.check_if_boolean(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('dataupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataupdated', "silent is not boolean",chartType , "FAIL")
            
            
            
        

            
    except Exception as e:
        report.entry_csv('dataupdated', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    


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


def f_dataloaderror(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataloaderror.eObj.eventType")
        eventId= driver.execute_script("return events.dataloaderror.eObj.eventId")
        cancelled= driver.execute_script("return events.dataloaderror.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataloaderror.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataloaderror.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataloaderror.eObj.preventDefault")
        detached= driver.execute_script("return events.dataloaderror.eObj.detached")
        detachHandler= driver.execute_script("return events.dataloaderror.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataloaderror.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.dataloaderror.eObj.data.url")
        dObj2= driver.execute_script("return events.dataloaderror.eObj.data.dataFormat")
        dObj3= driver.execute_script("return events.dataloaderror.eObj.data.silent")
        dObj4= driver.execute_script("return events.dataloaderror.eObj.data.httpStatus")
        
        
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataloaderror":
            obj_param="eventType = ",eventType
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataloaderror', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == "pie":
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if dObj1 == "_"+pom.loaded_url_chartdata():
            obj_param="dObj1 = ",dObj1
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "source is not correct",chartType , "FAIL")
            
            
            
        if dObj2 == "json":
            obj_param="dObj2 = ",dObj2
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "dataformat is not correct",chartType , "FAIL")
            
            
        
        if val.check_if_boolean(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "silent is not boolean",chartType , "FAIL")
            
        
        if val.check_if_int(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('dataloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloaderror', "httpStatus is not a number",chartType , "FAIL")
            
        
            
            
            
    except Exception as e:
        report.entry_csv('dataloaderror', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        

    
        
        
    
    
    
    
    
    


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
from Util import chart


def f_exported(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.exported.eObj.eventType")
        eventId= driver.execute_script("return events.exported.eObj.eventId")
        cancelled= driver.execute_script("return events.exported.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.exported.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.exported.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.exported.eObj.preventDefault")
        detached= driver.execute_script("return events.exported.eObj.detached")
        detachHandler= driver.execute_script("return events.exported.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.exported.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.exported.eObj.data.DOMId")
        dObj2= driver.execute_script("return events.exported.eObj.data.fileName")
        dObj3= driver.execute_script("return events.exported.eObj.data.height")
        dObj4= driver.execute_script("return events.exported.eObj.data.width")
        dObj5= driver.execute_script("return events.exported.eObj.data.notice")
        dObj6= driver.execute_script("return events.exported.eObj.data.statusCode")
        dObj7= driver.execute_script("return events.exported.eObj.data.statusMessage")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "exported":
            obj_param="eventType = ",eventType
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('exported', obj_param, chartType, "PASS")
        except:
            report.entry_csv('exported', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "senderChartType is not correct",chartType , "FAIL")
            
        
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "DOMId is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('exported', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exported', "fileName is empty string",chartType , "FAIL")
            
            
            
        try:
            if val.check_if_int(dObj3):
                obj_param="dObj3 = ",dObj3
                report.entry_csv('exported', obj_param, chartType, "PASS")
        except:
            report.entry_csv('exported', "height is not int",chartType , "FAIL")   
            
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('exported', obj_param, chartType, "PASS")
        except:
            report.entry_csv('exported', "width is not int",chartType , "FAIL") 
            
            
            

        
            
    except Exception as e:
        report.entry_csv('exported', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

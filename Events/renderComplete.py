
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


def f_renderComplete(driver, chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.rendercomplete.eObj.eventType")
        eventId= driver.execute_script("return events.rendercomplete.eObj.eventId")
        cancelled= driver.execute_script("return events.rendercomplete.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.rendercomplete.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.rendercomplete.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.rendercomplete.eObj.preventDefault")
        detached= driver.execute_script("return events.rendercomplete.eObj.detached")
        detachHandler= driver.execute_script("return events.rendercomplete.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.rendercomplete.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.rendercomplete.eObj.data.drawCount")
        dObj2= driver.execute_script("return events.rendercomplete.eObj.data.height")
        dObj3= driver.execute_script("return events.rendercomplete.eObj.data.renderer")
        dObj4= driver.execute_script("return events.rendercomplete.eObj.data.width")
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "rendercomplete":
            obj_param="eventType = ",eventType
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('rendercomplete', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        
        if val.check_if_int(dObj1):
            obj_param="Container = ",dObj1
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "dObj1 is not correct",chartType , "FAIL")
            print dObj1
            
            
        if val.check_if_int(dObj2):
            obj_param="height = ",dObj2
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "dObj2 is not correct",chartType , "FAIL")
            print dObj2
            
        if dObj3 == "javascript":
            obj_param="rendered = ",dObj3
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "dObj3 is not correct",chartType , "FAIL")
            print dObj3
            
        if val.check_if_int(dObj4):
            obj_param="width = ",dObj4
            report.entry_csv('rendercomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('rendercomplete', "dObj4 is not correct",chartType , "FAIL")
            print dObj4
       
    except Exception as e:
        report.entry_csv('rendered', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        
    
    
    
    
    
    

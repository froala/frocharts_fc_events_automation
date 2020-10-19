
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


def f_realtimeupdatecomplete(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.realtimeupdatecomplete.eObj.eventType")
        eventId= driver.execute_script("return events.realtimeupdatecomplete.eObj.eventId")
        cancelled= driver.execute_script("return events.realtimeupdatecomplete.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.realtimeupdatecomplete.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.realtimeupdatecomplete.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.realtimeupdatecomplete.eObj.preventDefault")
        detached= driver.execute_script("return events.realtimeupdatecomplete.eObj.detached")
        detachHandler= driver.execute_script("return events.realtimeupdatecomplete.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.realtimeupdatecomplete.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.realtimeupdatecomplete.eObj.data.data")
        dObj2= driver.execute_script("return events.realtimeupdatecomplete.eObj.data.source")
        dObj3= driver.execute_script("return events.realtimeupdatecomplete.eObj.data.url")
        dObj4= driver.execute_script("return events.realtimeupdatecomplete.eObj.data.updateObject.msgId")
        dObj5= driver.execute_script("return events.realtimeupdatecomplete.eObj.data.prevData")
        
        
        chartType=chartType.replace('_real','')
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "realtimeupdatecomplete":
            obj_param="eventType = ",eventType
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('realtimeupdatecomplete', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "data is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "source is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "url is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "msgId is empty string",chartType , "FAIL")
            
            
        if val.check_if_not_empty_string(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('realtimeupdatecomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('realtimeupdatecomplete', "prevData array value is empty string",chartType , "FAIL")
        
            
    except Exception as e:
        report.entry_csv('realtimeupdatecomplete', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

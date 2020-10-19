
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


def f_beforeresize(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.beforeresize.eObj.eventType")
        eventId= driver.execute_script("return events.beforeresize.eObj.eventId")
        cancelled= driver.execute_script("return events.beforeresize.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.beforeresize.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.beforeresize.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.beforeresize.eObj.preventDefault")
        detached= driver.execute_script("return events.beforeresize.eObj.detached")
        detachHandler= driver.execute_script("return events.beforeresize.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.beforeresize.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.beforeresize.eObj.data.currentWidth")
        dObj2= driver.execute_script("return events.beforeresize.eObj.data.currentHeight")
        dObj4= driver.execute_script("return events.beforeresize.eObj.data.newWidth")
        dObj5= driver.execute_script("return events.beforeresize.eObj.data.newHeight")
        
        
        
        chartType = chartType.replace('_resize','')
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "beforeresize":
            obj_param="eventType = ",eventType
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforeresize', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        else:
            report.entry_csv('beforeresize', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforeresize', "currentWidth is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforeresize', "currentHeight is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforeresize', "newWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('beforeresize', obj_param, chartType, "PASS")
        except:
            report.entry_csv('beforeresize', "newHeight is not number",chartType , "FAIL")
            
                
        
        
            
    except Exception as e:
        report.entry_csv('beforeresize', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

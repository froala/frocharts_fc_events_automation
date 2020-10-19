
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


def f_resizecancelled(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.resizecancelled.eObj.eventType")
        eventId= driver.execute_script("return events.resizecancelled.eObj.eventId")
        cancelled= driver.execute_script("return events.resizecancelled.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.resizecancelled.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.resizecancelled.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.resizecancelled.eObj.preventDefault")
        detached= driver.execute_script("return events.resizecancelled.eObj.detached")
        detachHandler= driver.execute_script("return events.resizecancelled.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.resizecancelled.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.resizecancelled.eObj.data.cancelledTargetHeight")
        dObj2= driver.execute_script("return events.resizecancelled.eObj.data.cancelledTargetWidth")
        dObj4= driver.execute_script("return events.resizecancelled.eObj.data.currentHeight")
        dObj5= driver.execute_script("return events.resizecancelled.eObj.data.currentWidth")
        
        
        
        chartType = chartType.replace('_resizecanc','')
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "resizecancelled":
            obj_param="eventType = ",eventType
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resizecancelled', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resizecancelled', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resizecancelled', "cancelledTargetHeight is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resizecancelled', "cancelledTargetWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resizecancelled', "currentHeight is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('resizecancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resizecancelled', "currentWidth is not number",chartType , "FAIL")
            
                
        
        
            
    except Exception as e:
        report.entry_csv('resizecancelled', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    


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


def f_markerrollover(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.markerrollover.eObj.eventType")
        eventId= driver.execute_script("return events.markerrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.markerrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.markerrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.markerrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.markerrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.markerrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.markerrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.markerrollover.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.markerrollover.eObj.data.chartX")
        dObj2= driver.execute_script("return events.markerrollover.eObj.data.chartY")
        dObj3= driver.execute_script("return events.markerrollover.eObj.data.label")
        dObj4= driver.execute_script("return events.markerrollover.eObj.data.scaledX")
        dObj5= driver.execute_script("return events.markerrollover.eObj.data.scaledY")
        dObj6= driver.execute_script("return events.markerrollover.eObj.data.x")
        dObj7= driver.execute_script("return events.markerrollover.eObj.data.y")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "markerrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "chartX is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "chartY is not number",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('markerrollover', "label is empty string",chartType , "FAIL")
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "scaledX is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "scaledY is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj6):
                obj_param="dObj1 = ",dObj6
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "x is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj7):
                obj_param="dObj7 = ",dObj7
                report.entry_csv('markerrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('markerrollover', "y is not number",chartType , "FAIL")
                
        
        
            
    except Exception as e:
        report.entry_csv('markerrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

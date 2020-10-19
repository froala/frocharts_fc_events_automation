
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


def f_legendpointerdragstart(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.legendpointerdragstart.eObj.eventType")
        eventId= driver.execute_script("return events.legendpointerdragstart.eObj.eventId")
        cancelled= driver.execute_script("return events.legendpointerdragstart.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.legendpointerdragstart.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.legendpointerdragstart.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.legendpointerdragstart.eObj.preventDefault")
        detached= driver.execute_script("return events.legendpointerdragstart.eObj.detached")
        detachHandler= driver.execute_script("return events.legendpointerdragstart.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.legendpointerdragstart.eObj.sender.chartType()")
        originalEvent= driver.execute_script("return events.legendpointerdragstart.eObj.originalEvent")
        
        innerRadius= driver.execute_script("return events.legendpointerdragstart.eObj.data.innerRadius")
        legendPointerHeight= driver.execute_script("return events.legendpointerdragstart.eObj.data.legendPointerHeight")
        legendPointerWidth= driver.execute_script("return events.legendpointerdragstart.eObj.data.legendPointerWidth")
        outerRadius= driver.execute_script("return events.legendpointerdragstart.eObj.data.outerRadius")
        pointerIndex= driver.execute_script("return events.legendpointerdragstart.eObj.data.pointerIndex")
        pointers= driver.execute_script("return events.legendpointerdragstart.eObj.data.pointers")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "legendpointerdragstart":
            obj_param="eventType = ",eventType
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        except:
            report.entry_csv('legendpointerdragstart', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
            
        
        if val.check_if_not_empty_string(originalEvent):
            obj_param="originalEvent = ",originalEvent
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "originalEvent is not correct",chartType , "FAIL")
            print originalEvent
        
        if val.check_if_int(innerRadius):
            obj_param="innerRadius = ",innerRadius
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "innerRadius is not correct",chartType , "FAIL")
            print innerRadius
            
            
        if val.check_if_int(legendPointerHeight):
            obj_param="legendPointerHeight = ",legendPointerHeight
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "legendPointerHeight is not correct",chartType , "FAIL")
            print legendPointerHeight
            
        if val.check_if_int(legendPointerWidth):
            obj_param="legendPointerWidth = ",legendPointerWidth
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "legendPointerWidth is not correct",chartType , "FAIL")
            print legendPointerWidth
            
        if val.check_if_int(outerRadius):
            obj_param="outerRadius = ",outerRadius
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "outerRadius is not correct",chartType , "FAIL")
            print outerRadius
           
        if val.check_if_int(pointerIndex):
            obj_param="pointerIndex = ",pointerIndex
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "pointerIndex is not correct",chartType , "FAIL")
            print pointerIndex 
            
        if val.check_if_not_empty_string(pointers):
            obj_param="pointers = ",pointers
            report.entry_csv('legendpointerdragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendpointerdragstart', "pointers is not correct",chartType , "FAIL")
            print pointers  
        
    
    except Exception as e:
        report.entry_csv('legendpointerdragstart', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

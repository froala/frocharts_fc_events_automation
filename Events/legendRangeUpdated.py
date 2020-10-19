
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


def f_legendrangeupdated(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.legendrangeupdated.eObj.eventType")
        eventId= driver.execute_script("return events.legendrangeupdated.eObj.eventId")
        cancelled= driver.execute_script("return events.legendrangeupdated.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.legendrangeupdated.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.legendrangeupdated.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.legendrangeupdated.eObj.preventDefault")
        detached= driver.execute_script("return events.legendrangeupdated.eObj.detached")
        detachHandler= driver.execute_script("return events.legendrangeupdated.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.legendrangeupdated.eObj.sender.chartType()")
        originalEvent= driver.execute_script("return events.legendrangeupdated.eObj.originalEvent")
        
        maxValue= driver.execute_script("return events.legendrangeupdated.eObj.data.maxValue")
        minValue= driver.execute_script("return events.legendrangeupdated.eObj.data.minValue")
        previousMaxValue= driver.execute_script("return events.legendrangeupdated.eObj.data.previousMaxValue")
        previousMinValue= driver.execute_script("return events.legendrangeupdated.eObj.data.previousMinValue")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "legendrangeupdated":
            obj_param="eventType = ",eventType
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        except:
            report.entry_csv('legendrangeupdated', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
            
        
        if val.check_if_not_empty_string(originalEvent):
            obj_param="originalEvent = ",originalEvent
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "originalEvent is not correct",chartType , "FAIL")
            print originalEvent
        
        if val.check_if_int(maxValue):
            obj_param="maxValue = ",maxValue
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "maxValue is not correct",chartType , "FAIL")
            print maxValue
            
            
        if val.check_if_int(minValue):
            obj_param="minValue = ",minValue
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "minValue is not correct",chartType , "FAIL")
            print minValue
            
        if val.check_if_int(previousMaxValue):
            obj_param="previousMaxValue = ",previousMaxValue
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "previousMaxValue is not correct",chartType , "FAIL")
            print previousMaxValue
            
        if val.check_if_int(previousMinValue):
            obj_param="previousMinValue = ",previousMinValue
            report.entry_csv('legendrangeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legendrangeupdated', "previousMinValue is not correct",chartType , "FAIL")
            print previousMinValue
        
    
    except Exception as e:
        report.entry_csv('legendrangeupdated', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

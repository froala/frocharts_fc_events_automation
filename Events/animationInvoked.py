
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


def f_animationinvoked(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
                
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.animationinvoked.eObj.eventType")
        eventId= driver.execute_script("return events.animationinvoked.eObj.eventId")
        cancelled= driver.execute_script("return events.animationinvoked.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.animationinvoked.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.animationinvoked.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.animationinvoked.eObj.preventDefault")
        detached= driver.execute_script("return events.animationinvoked.eObj.detached")
        detachHandler= driver.execute_script("return events.animationinvoked.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.animationinvoked.eObj.sender.chartType()")
        duration= driver.execute_script("return events.animationinvoked.eObj.data.duration")
        
        chartType = chartType.replace('_animation','')
        
         
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "animationinvoked":
            obj_param="eventType = ",eventType
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        except:
            report.entry_csv('animationinvoked', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "detached is not boolean",chartType , "FAIL")
               
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
         
        if val.check_if_int(duration):
            obj_param="duration = ",duration
            report.entry_csv('animationinvoked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('animationinvoked', "duration is not correct",chartType , "FAIL")
                  
    except Exception as e:
        report.entry_csv('animationinvoked', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

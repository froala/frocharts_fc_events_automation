
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


def f_logoloaderror(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.logoloaderror.eObj.eventType")
        eventId= driver.execute_script("return events.logoloaderror.eObj.eventId")
        cancelled= driver.execute_script("return events.logoloaderror.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.logoloaderror.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.logoloaderror.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.logoloaderror.eObj.preventDefault")
        detached= driver.execute_script("return events.logoloaderror.eObj.detached")
        detachHandler= driver.execute_script("return events.logoloaderror.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.logoloaderror.eObj.sender.chartType()")
        
        error= driver.execute_script("return events.logoloaderror.eObj.data.error")
        logoAlpha= driver.execute_script("return events.logoloaderror.eObj.data.logoAlpha")
        logoLink= driver.execute_script("return events.logoloaderror.eObj.data.logoLink")
        logoPosition= driver.execute_script("return events.logoloaderror.eObj.data.logoPosition")
        logoScale= driver.execute_script("return events.logoloaderror.eObj.data.logoScale")
        logoURL= driver.execute_script("return events.logoloaderror.eObj.data.logoURL")
        
        chartType = chartType.replace('_logo_error','')
         
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "logoloaderror":
            obj_param="eventType = ",eventType
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        except:
            report.entry_csv('logoloaderror', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
           
        if val.check_if_not_empty_string(error):
            obj_param="error = ",error
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "error is not correct",chartType , "FAIL")
            print error
        
        if val.check_if_int(logoAlpha):
            obj_param="logoAlpha = ",logoAlpha
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "logoAlpha is not correct",chartType , "FAIL")
            print logoAlpha
        
        if val.check_if_not_empty_string(logoLink):
            obj_param="logoLink = ",logoLink
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "logoLink is not correct",chartType , "FAIL")
            print logoLink
            
        if val.check_if_not_empty_string(logoPosition):
            obj_param="logoPosition = ",logoPosition
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "logoPosition is not correct",chartType , "FAIL")
            print logoPosition
            
        if val.check_if_int(logoScale):
            obj_param="logoScale = ",logoScale
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "logoScale is not correct",chartType , "FAIL")
            print logoScale
            
        if val.check_if_url(logoURL):
            obj_param="logoURL = ",logoURL
            report.entry_csv('logoloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logoloaderror', "logoURL is not correct",chartType , "FAIL")
            print logoURL
            
           
    except Exception as e:
        report.entry_csv('logoloaderror', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

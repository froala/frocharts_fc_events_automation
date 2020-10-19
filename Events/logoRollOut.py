
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


def f_logorollout(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.logorollout.eObj.eventType")
        eventId= driver.execute_script("return events.logorollout.eObj.eventId")
        cancelled= driver.execute_script("return events.logorollout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.logorollout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.logorollout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.logorollout.eObj.preventDefault")
        detached= driver.execute_script("return events.logorollout.eObj.detached")
        detachHandler= driver.execute_script("return events.logorollout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.logorollout.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.logorollout.eObj.data.chartX")
        chartY= driver.execute_script("return events.logorollout.eObj.data.chartY")
        logoAlpha= driver.execute_script("return events.logorollout.eObj.data.logoAlpha")
        logoLink= driver.execute_script("return events.logorollout.eObj.data.logoLink")
        logoPosition= driver.execute_script("return events.logorollout.eObj.data.logoPosition")
        logoScale= driver.execute_script("return events.logorollout.eObj.data.logoScale")
        logoURL= driver.execute_script("return events.logorollout.eObj.data.logoURL")
        pageX= driver.execute_script("return events.logorollout.eObj.data.pageX")
        pageY= driver.execute_script("return events.logorollout.eObj.data.pageY")
        
        
        chartType = chartType.replace('_logo','')
         
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "logorollout":
            obj_param="eventType = ",eventType
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('logorollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('logorollout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
         
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "chartY is not correct",chartType , "FAIL")
            print chartY
           
        
        if val.check_if_int(logoAlpha):
            obj_param="logoAlpha = ",logoAlpha
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "logoAlpha is not correct",chartType , "FAIL")
            print logoAlpha
        
        if val.check_if_not_empty_string(logoLink):
            obj_param="logoLink = ",logoLink
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "logoLink is not correct",chartType , "FAIL")
            print logoLink
            
        if val.check_if_not_empty_string(logoPosition):
            obj_param="logoPosition = ",logoPosition
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "logoPosition is not correct",chartType , "FAIL")
            print logoPosition
            
        if val.check_if_int(logoScale):
            obj_param="logoScale = ",logoScale
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "logoScale is not correct",chartType , "FAIL")
            print logoScale
            
        if val.check_if_url(logoURL):
            obj_param="logoURL = ",logoURL
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "logoURL is not correct",chartType , "FAIL")
            print logoURL
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('logorollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('logorollout', "pageY is not correct",chartType , "FAIL")
            print pageY
           
    except Exception as e:
        report.entry_csv('logorollout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

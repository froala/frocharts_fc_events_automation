
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


def f_drilldown(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.drilldown.eObj.eventType")
        eventId= driver.execute_script("return events.drilldown.eObj.eventId")
        cancelled= driver.execute_script("return events.drilldown.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.drilldown.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.drilldown.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.drilldown.eObj.preventDefault")
        detached= driver.execute_script("return events.drilldown.eObj.detached")
        detachHandler= driver.execute_script("return events.drilldown.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.drilldown.eObj.sender.chartType()")
        
        label= driver.execute_script("return events.drilldown.eObj.data.node.label")
        withoutHead= driver.execute_script("return events.drilldown.eObj.data.withoutHead")
        drillUp= driver.execute_script("return events.drilldown.eObj.data.drillUp")
        drillUpToTop= driver.execute_script("return events.drilldown.eObj.data.drillUpToTop")
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "drilldown":
            obj_param="eventType = ",eventType
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('drilldown', obj_param, chartType, "PASS")
        except:
            report.entry_csv('drilldown', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "preventDefault is not a function",chartType , "FAIL")
                
            
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "detached is not boolean",chartType , "FAIL")
          
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        if val.check_if_function(drillUp):
                obj_param="drillUp = ",drillUp
                report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "drillUp is not a function",chartType , "FAIL")
             
             
        if val.check_if_function(drillUpToTop):
                obj_param="drillUpToTop = ",drillUpToTop
                report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "drillUpToTop is not a function",chartType , "FAIL")
             
        if val.check_if_not_empty_string(label):
            obj_param="label = ",label
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "label is not correct",chartType , "FAIL")
        
        
        if val.check_if_boolean(withoutHead):
            obj_param="withoutHead = ",withoutHead
            report.entry_csv('drilldown', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drilldown', "withoutHead is not boolean",chartType , "FAIL")
          
          
    except Exception as e:
        report.entry_csv('drilldown', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

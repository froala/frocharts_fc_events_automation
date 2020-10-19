
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


def f_dataplotclickchorddiagram(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataplotclick.eObj.eventType")
        eventId= driver.execute_script("return events.dataplotclick.eObj.eventId")
        cancelled= driver.execute_script("return events.dataplotclick.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataplotclick.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataplotclick.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataplotclick.eObj.preventDefault")
        detached= driver.execute_script("return events.dataplotclick.eObj.detached")
        detachHandler= driver.execute_script("return events.dataplotclick.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataplotclick.eObj.sender.chartType()")
        
        label= driver.execute_script("return events.dataplotclick.eObj.data.label")
        value= driver.execute_script("return events.dataplotclick.eObj.data.value")
        links= driver.execute_script("return events.dataplotclick.eObj.data.links")
        color= driver.execute_script("return events.dataplotclick.eObj.data.color")
        alpha= driver.execute_script("return events.dataplotclick.eObj.data.alpha")
        #QE Including displayValue for chord Diagram dataplot events
        displayValue= driver.execute_script("return events.dataplotclick.eObj.data.displayValue")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        chartType = chartType.replace('_links_nodes_events','')
        
        if eventType == "dataplotclick":
            obj_param="eventType = ",eventType
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataplotclick', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
            
          
        #Data Parameters    
        if val.check_if_not_empty_string(label):
            obj_param="label = ",label
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "label is not correct",chartType , "FAIL")
            print label
            
            
            
        if val.check_if_int(value):
            obj_param="value = ",value
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "value is not correct",chartType , "FAIL")
            print value
                            
                 
            
        if val.check_if_not_empty_string(links):
            obj_param="links = ",links
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "links is not correct",chartType , "FAIL")
            print links
            
        
       
        if val.check_if_not_empty_string(color):
            obj_param="color = ",color
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "color is not correct",chartType , "FAIL")
            print color                       
             
            
            
        if val.check_if_int(alpha):
            obj_param="alpha = ",alpha
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "alpha is not correct",chartType , "FAIL")
            print alpha
            
            
            
        if val.check_if_not_empty_string(displayValue):
            obj_param="displayValue = ",displayValue
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "displayValue is not correct",chartType , "FAIL")
            print displayValue                 

           
    except Exception as e:
        report.entry_csv('dataplotclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

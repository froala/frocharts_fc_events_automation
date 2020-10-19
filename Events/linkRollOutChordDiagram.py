
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


def f_linkrolloutchorddiagram(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.linkrollout.eObj.eventType")
        eventId= driver.execute_script("return events.linkrollout.eObj.eventId")
        cancelled= driver.execute_script("return events.linkrollout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.linkrollout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.linkrollout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.linkrollout.eObj.preventDefault")
        detached= driver.execute_script("return events.linkrollout.eObj.detached")
        detachHandler= driver.execute_script("return events.linkrollout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.linkrollout.eObj.sender.chartType()")
        
        dominantFlowValue= driver.execute_script("return events.linkrollout.eObj.data.dominantFlowValue")
        subservientFlowValue= driver.execute_script("return events.linkrollout.eObj.data.subservientFlowValue")
        linkedNodes= driver.execute_script("return events.linkrollout.eObj.data.linkedNodes")
        color= driver.execute_script("return events.linkrollout.eObj.data.color")
        alpha= driver.execute_script("return events.linkrollout.eObj.data.alpha")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        chartType = chartType.replace('_links_nodes_events','')
        
        if eventType == "linkrollout":
            obj_param="eventType = ",eventType
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('linkrollout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
            
            
            
        #Data Parameters 
        if val.check_if_int(dominantFlowValue):
            obj_param="dominantFlowValue = ",dominantFlowValue
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "dominantFlowValue is not correct",chartType , "FAIL")
            print dominantFlowValue
            
          
          
        if val.check_if_int(subservientFlowValue):
            obj_param="subservientFlowValue = ",subservientFlowValue
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "subservientFlowValue is not correct",chartType , "FAIL")
            print subservientFlowValue
            
            
            
        if val.check_if_not_empty_string(linkedNodes):
            obj_param="linkedNodes = ",linkedNodes
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "linkedNodes is not correct",chartType , "FAIL")
            print linkedNodes   
            
     
            
        if val.check_if_not_empty_string(color):
            obj_param="color = ",color
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "color is not correct",chartType , "FAIL")
            print color                     
             
            
            
        if val.check_if_int(alpha):
            obj_param="alpha = ",alpha
            report.entry_csv('linkrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('linkrollout', "alpha is not correct",chartType , "FAIL")
            print alpha             


    except Exception as e:
        report.entry_csv('linkrollout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

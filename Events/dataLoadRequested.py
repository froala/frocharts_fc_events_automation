
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


def f_dataloadrequested(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataloadrequested.eObj.eventType")
        eventId= driver.execute_script("return events.dataloadrequested.eObj.eventId")
        cancelled= driver.execute_script("return events.dataloadrequested.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataloadrequested.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataloadrequested.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataloadrequested.eObj.preventDefault")
        detached= driver.execute_script("return events.dataloadrequested.eObj.detached")
        detachHandler= driver.execute_script("return events.dataloadrequested.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataloadrequested.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.dataloadrequested.eObj.data.source")
        dObj2= driver.execute_script("return events.dataloadrequested.eObj.data.url")
        dObj3= driver.execute_script("return events.dataloadrequested.eObj.data.dataFormat")
        dObj4= driver.execute_script("return events.dataloadrequested.eObj.data.silent")

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataloadrequested":
            obj_param="eventType = ",eventType
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataloadrequested', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == "pie":
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if dObj1 == "XmlHttpRequest":
            obj_param="dObj1 = ",dObj1
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "source is not correct",chartType , "FAIL")
            
            
            
        if dObj2 == pom.loaded_url_chartdata():
            obj_param="dObj2 = ",dObj2
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "url is not correct",chartType , "FAIL")
            
            
        
        if dObj3 == "json":
            obj_param="dObj3 = ",dObj3
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "dataformat is not correct",chartType , "FAIL")
            
        
        if val.check_if_boolean(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataloadrequested', "silent is not boolean",chartType , "FAIL")
            
        
#         if val.check_if_boolean(dObj5):
#             obj_param="dObj5 = ",dObj5
#             report.entry_csv('dataloadrequested', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('dataloadrequested', "callback() is not returning boolean",chartType , "FAIL")
        
        
            
            
            
    except Exception as e:
        report.entry_csv('dataloadrequested', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

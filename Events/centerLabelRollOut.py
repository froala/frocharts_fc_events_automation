
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


def f_centerlabelrollout(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.centerlabelrollout.eObj.eventType")
        eventId= driver.execute_script("return events.centerlabelrollout.eObj.eventId")
        cancelled= driver.execute_script("return events.centerlabelrollout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.centerlabelrollout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.centerlabelrollout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.centerlabelrollout.eObj.preventDefault")
        detached= driver.execute_script("return events.centerlabelrollout.eObj.detached")
        detachHandler= driver.execute_script("return events.centerlabelrollout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.centerlabelrollout.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.centerlabelrollout.eObj.data.width")
        dObj2= driver.execute_script("return events.centerlabelrollout.eObj.data.height")
        dObj3= driver.execute_script("return events.centerlabelrollout.eObj.data.container.baseURI")
        dObj4= driver.execute_script("return events.centerlabelrollout.eObj.data.pixelWidth")
        dObj5= driver.execute_script("return events.centerlabelrollout.eObj.data.pixelHeight")
        dObj6= driver.execute_script("return events.centerlabelrollout.eObj.data.id")
        dObj7= driver.execute_script("return events.centerlabelrollout.eObj.data.renderer")
        dObj8= driver.execute_script("return events.centerlabelrollout.eObj.data.centerLabelText")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "centerlabelrollout":
            obj_param="eventType = ",eventType
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('centerlabelrollout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "width should be int",chartType , "FAIL")
        
        
        if val.check_if_int(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "height should be int",chartType , "FAIL")    
        
        
        
        if dObj3 ==  chart.url_to_hit():
            obj_param="dObj3 = ",dObj3
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "baseURI should be path of file",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "pixelWidth should be int",chartType , "FAIL")
        
        
        if val.check_if_int(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "pixelHeight should be int",chartType , "FAIL")  
        
        
        
        if val.check_if_not_empty_string(dObj6):
            obj_param="dObj6 = ",dObj6
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "id should be string",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('centerlabelrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelrollout', "centerLabelText should be string",chartType , "FAIL")
            

            
    except Exception as e:
        report.entry_csv('centerlabelrollout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

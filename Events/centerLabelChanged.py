
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


def f_centerlabelchanged(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.centerlabelchanged.eObj.eventType")
        eventId= driver.execute_script("return events.centerlabelchanged.eObj.eventId")
        cancelled= driver.execute_script("return events.centerlabelchanged.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.centerlabelchanged.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.centerlabelchanged.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.centerlabelchanged.eObj.preventDefault")
        detached= driver.execute_script("return events.centerlabelchanged.eObj.detached")
        detachHandler= driver.execute_script("return events.centerlabelchanged.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.centerlabelchanged.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.centerlabelchanged.eObj.data.width")
        dObj2= driver.execute_script("return events.centerlabelchanged.eObj.data.height")
        dObj3= driver.execute_script("return events.centerlabelchanged.eObj.data.container.baseURI")
        dObj4= driver.execute_script("return events.centerlabelchanged.eObj.data.pixelWidth")
        dObj5= driver.execute_script("return events.centerlabelchanged.eObj.data.pixelHeight")
        dObj6= driver.execute_script("return events.centerlabelchanged.eObj.data.id")
        dObj8= driver.execute_script("return events.centerlabelchanged.eObj.data.centerLabelText")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "centerlabelchanged":
            obj_param="eventType = ",eventType
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        except:
            report.entry_csv('centerlabelchanged', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "width should be int",chartType , "FAIL")
        
        
        if val.check_if_int(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "height should be int",chartType , "FAIL")    
        
        
        
        if dObj3 ==  chart.url_to_hit():
            obj_param="dObj3 = ",dObj3
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "baseURI should be path of file",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "pixelWidth should be int",chartType , "FAIL")
        
        
        if val.check_if_int(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "pixelHeight should be int",chartType , "FAIL")  
        
        
        
        if val.check_if_not_empty_string(dObj6):
            obj_param="dObj6 = ",dObj6
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "id should be string",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('centerlabelchanged', obj_param, chartType, "PASS")
        else:
            report.entry_csv('centerlabelchanged', "centerLabelText should be string",chartType , "FAIL")
            

            
    except Exception as e:
        report.entry_csv('centerlabelchanged', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

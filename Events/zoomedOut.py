
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


def f_zoomedout(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.zoomedout.eObj.eventType")
        eventId= driver.execute_script("return events.zoomedout.eObj.eventId")
        cancelled= driver.execute_script("return events.zoomedout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.zoomedout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.zoomedout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.zoomedout.eObj.preventDefault")
        detached= driver.execute_script("return events.zoomedout.eObj.detached")
        detachHandler= driver.execute_script("return events.zoomedout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.zoomedout.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.zoomedout.eObj.data.level")
        dObj2= driver.execute_script("return events.zoomedout.eObj.data.startIndex")
        dObj3= driver.execute_script("return events.zoomedout.eObj.data.startLabel")
        dObj4= driver.execute_script("return events.zoomedout.eObj.data.endIndex")
        dObj5= driver.execute_script("return events.zoomedout.eObj.data.endLabel")
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "zoomedout":
            obj_param="eventType = ",eventType
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('zoomedout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('zoomedout', "chartX is not an int",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('zoomedout', "chartY is not an int",chartType , "FAIL")
        
        

        if val.check_if_not_empty_string(dObj3):
                obj_param="dObj3 = ",dObj3
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "pageX is not an int",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('zoomedout', "pageY is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('zoomedout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('zoomedout', "Id is empty",chartType , "FAIL")
                
        
        
            
    except Exception as e:
        report.entry_csv('zoomedout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

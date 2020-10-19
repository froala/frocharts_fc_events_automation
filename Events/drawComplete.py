
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


def f_drawcomplete(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.drawcomplete.eObj.eventType")
        eventId= driver.execute_script("return events.drawcomplete.eObj.eventId")
        cancelled= driver.execute_script("return events.drawcomplete.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.drawcomplete.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.drawcomplete.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.drawcomplete.eObj.preventDefault")
        detached= driver.execute_script("return events.drawcomplete.eObj.detached")
        detachHandler= driver.execute_script("return events.drawcomplete.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.drawcomplete.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.drawcomplete.eObj.data.width")
        dObj2= driver.execute_script("return events.drawcomplete.eObj.data.height")
        dObj3= driver.execute_script("return events.drawcomplete.eObj.data.drawCount")
        dObj4= driver.execute_script("return events.drawcomplete.eObj.data.displayingMessage")
        dObj5= driver.execute_script("return events.drawcomplete.eObj.data.renderer")
        
        
        chartType=chartType.replace('_chartTypeChanged','')
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "drawcomplete":
            obj_param="eventType = ",eventType
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('drawcomplete', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "senderChartType is not correct",chartType , "FAIL")
            
        
        
        
        
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('drawcomplete', "width is not int",chartType , "FAIL")   
        
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('drawcomplete', "height is not int",chartType , "FAIL") 
            
            
            
        try:
            if val.check_if_int(dObj3):
                obj_param="dObj3 = ",dObj3
                report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        except:
            report.entry_csv('drawcomplete', "drawCount is not int",chartType , "FAIL") 
        
        
        
        if val.check_if_boolean(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "displayingMessage is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('drawcomplete', obj_param, chartType, "PASS")
        else:
            report.entry_csv('drawcomplete', "renderer is empty",chartType , "FAIL")
            
            
        
            
    except Exception as e:
        report.entry_csv('drawcomplete', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

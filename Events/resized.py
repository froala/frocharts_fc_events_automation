
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


def f_resized(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.resized.eObj.eventType")
        eventId= driver.execute_script("return events.resized.eObj.eventId")
        cancelled= driver.execute_script("return events.resized.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.resized.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.resized.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.resized.eObj.preventDefault")
        detached= driver.execute_script("return events.resized.eObj.detached")
        detachHandler= driver.execute_script("return events.resized.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.resized.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.resized.eObj.data.width")
        dObj2= driver.execute_script("return events.resized.eObj.data.height")
        dObj3= driver.execute_script("return events.resized.eObj.data.id")
        dObj4= driver.execute_script("return events.resized.eObj.data.prevWidth")
        dObj5= driver.execute_script("return events.resized.eObj.data.prevHeight")
        dObj6= driver.execute_script("return events.resized.eObj.data.originalWidth")
        dObj7= driver.execute_script("return events.resized.eObj.data.originalHeight")
        dObj8= driver.execute_script("return events.resized.eObj.data.pixelWidth")
        dObj9= driver.execute_script("return events.resized.eObj.data.pixelHeight")
        
        
        
        chartType = chartType.replace('_resize','')
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "resized":
            obj_param="eventType = ",eventType
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "width is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "height is not number",chartType , "FAIL")
            
            
            
        
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('resized', obj_param, chartType, "PASS")
        else:
            report.entry_csv('resized', "id is empty",chartType , "FAIL")
        
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "prevWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "prevHeight is not number",chartType , "FAIL")
            
        
        
        
        try:
            if val.check_if_int(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "originalWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj7):
                obj_param="dObj7 = ",dObj7
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "originalHeight is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj8):
                obj_param="dObj8 = ",dObj8
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "pixelWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj9):
                obj_param="dObj9 = ",dObj9
                report.entry_csv('resized', obj_param, chartType, "PASS")
        except:
            report.entry_csv('resized', "pixelHeight is not number",chartType , "FAIL")
        
                
        
        
            
    except Exception as e:
        report.entry_csv('resized', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    


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


def f_exportcancelled(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.exportcancelled.eObj.eventType")
        eventId= driver.execute_script("return events.exportcancelled.eObj.eventId")
        cancelled= driver.execute_script("return events.exportcancelled.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.exportcancelled.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.exportcancelled.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.exportcancelled.eObj.preventDefault")
        detached= driver.execute_script("return events.exportcancelled.eObj.detached")
        detachHandler= driver.execute_script("return events.exportcancelled.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.exportcancelled.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.exportcancelled.eObj.data.bgColor")
        dObj2= driver.execute_script("return events.exportcancelled.eObj.data.bgAlpha")
        dObj3= driver.execute_script("return events.exportcancelled.eObj.data.exportaction")
        dObj4= driver.execute_script("return events.exportcancelled.eObj.data.exportfilename")
        dObj5= driver.execute_script("return events.exportcancelled.eObj.data.exporthandler")
        dObj6= driver.execute_script("return events.exportcancelled.eObj.data.exportformat")
        dObj7= driver.execute_script("return events.exportcancelled.eObj.data.exportparameters")
        dObj8= driver.execute_script("return events.exportcancelled.eObj.data.exporttargetwindow")
        dObj9= driver.execute_script("return events.exportcancelled.eObj.data.exportcallback")
        dObj10= driver.execute_script("return events.exportcancelled.eObj.data.exportwithimages")
        
        
        
        chartType=chartType.replace('_exportcanc','')
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "exportcancelled":
            obj_param="eventType = ",eventType
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('exportcancelled', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "senderChartType is not correct",chartType , "FAIL")
            
        
        
        if val.check_if_not_empty_string(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "bgColor is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "bgAlpha is empty string",chartType , "FAIL")
            
            
            
            
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "exportaction is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "exportfilename is empty string",chartType , "FAIL")
            
            
        
        if val.check_if_not_empty_string(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "exporthandler is empty string",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj6):
            obj_param="dObj6 = ",dObj6
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "exportformat is empty string",chartType , "FAIL")
        
            
            
            
            
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        else:
            report.entry_csv('exportcancelled', "exporttargetwindow is empty string",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj10):
                obj_param="dObj10 = ",dObj10
                report.entry_csv('exportcancelled', obj_param, chartType, "PASS")
        except:
            report.entry_csv('exportcancelled', "exportwithimages is not int",chartType , "FAIL")
            
            

        
            
    except Exception as e:
        report.entry_csv('exportcancelled', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

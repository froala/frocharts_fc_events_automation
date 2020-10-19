
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


def f_dataplotdragend(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataplotdragend.eObj.eventType")
        eventId= driver.execute_script("return events.dataplotdragend.eObj.eventId")
        cancelled= driver.execute_script("return events.dataplotdragend.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataplotdragend.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataplotdragend.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataplotdragend.eObj.preventDefault")
        detached= driver.execute_script("return events.dataplotdragend.eObj.detached")
        detachHandler= driver.execute_script("return events.dataplotdragend.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataplotdragend.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.dataplotdragend.eObj.data.dataIndex")
        dObj2= driver.execute_script("return events.dataplotdragend.eObj.data.datasetIndex")
        dObj3= driver.execute_script("return events.dataplotdragend.eObj.data.datasetName")
        dObj4= driver.execute_script("return events.dataplotdragend.eObj.data.startValue")
        dObj5= driver.execute_script("return events.dataplotdragend.eObj.data.endValue")
        
        
        
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataplotdragend":
            obj_param="eventType = ",eventType
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataplotdragend', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "senderChartType is not correct",chartType , "FAIL")
        
        if chartType != "dragnode":
            if val.check_if_int(dObj1):
                try:
                    obj_param="dObj1 = ",dObj1
                    report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
                except:
                    report.entry_csv('dataplotdragend', "dataIndex is not an int",chartType , "FAIL")
            
            
            
        if val.check_if_int(dObj2):
            try:
                obj_param="dObj2 = ",dObj2
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
            except:
                report.entry_csv('dataplotdragend', "datasetIndex is not an int",chartType , "FAIL")
            
            
        
        if val.check_if_not_empty_string(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotdragend', "dObj3 is an empty String",chartType , "FAIL")
            
        
        if chartType != "dragnode":
            if val.check_if_number(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
            else:
                report.entry_csv('dataplotdragend', "dObj4 is not a number",chartType , "FAIL")
        
        
        if chartType != "dragnode":
            if val.check_if_number(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('dataplotdragend', obj_param, chartType, "PASS")
            else:
                report.entry_csv('dataplotdragend', "dObj5 is not a number",chartType , "FAIL")
            
            
            
    except Exception as e:
        report.entry_csv('dataplotdragend', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

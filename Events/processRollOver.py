
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


def f_processrollover(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.processrollover.eObj.eventType")
        eventId= driver.execute_script("return events.processrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.processrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.processrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.processrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.processrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.processrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.processrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.processrollover.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.processrollover.eObj.data.chartX")
        dObj2= driver.execute_script("return events.processrollover.eObj.data.chartY")
        dObj3= driver.execute_script("return events.processrollover.eObj.data.pageX")
        dObj4= driver.execute_script("return events.processrollover.eObj.data.pageY")
        dObj5= driver.execute_script("return events.processrollover.eObj.data.id")
        dObj6= driver.execute_script("return events.processrollover.eObj.data.label")
        dObj7= driver.execute_script("return events.processrollover.eObj.data.isHeader")
        dObj8= driver.execute_script("return events.processrollover.eObj.data.align")
        dObj9= driver.execute_script("return events.processrollover.eObj.data.vAlign")
        dObj10= driver.execute_script("return events.processrollover.eObj.data.link")
        
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "processrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('processrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('processrollover', "chartX is not an int",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('processrollover', "chartY is not an int",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(dObj3):
                obj_param="dObj3 = ",dObj3
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('processrollover', "pageX is not an int",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('processrollover', "pageY is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_not_empty_string(dObj5):
            obj_param="dObj5 = ",dObj5
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "Id is empty",chartType , "FAIL")
                
               
        
        
        if val.check_if_not_empty_string(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "label is empty",chartType , "FAIL") 
            
        
        
        if val.check_if_boolean(dObj7):
            obj_param="dObj7 = ",dObj7
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "isHeader is not boolean",chartType , "FAIL")
            
            
        
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "align is empty",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj9):
            obj_param="dObj9 = ",dObj9
            report.entry_csv('processrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('processrollover', "vAlign is empty",chartType , "FAIL")
            

            
    except Exception as e:
        report.entry_csv('processrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

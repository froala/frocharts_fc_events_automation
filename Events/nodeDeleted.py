
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


def f_nodedeleted(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.nodedeleted.eObj.eventType")
        eventId= driver.execute_script("return events.nodedeleted.eObj.eventId")
        cancelled= driver.execute_script("return events.nodedeleted.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.nodedeleted.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.nodedeleted.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.nodedeleted.eObj.preventDefault")
        detached= driver.execute_script("return events.nodedeleted.eObj.detached")
        detachHandler= driver.execute_script("return events.nodedeleted.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.nodedeleted.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.nodedeleted.eObj.data.id")
        dObj2= driver.execute_script("return events.nodedeleted.eObj.data.dataIndex")
        dObj3= driver.execute_script("return events.nodedeleted.eObj.data.datasetIndex")
        dObj4= driver.execute_script("return events.nodedeleted.eObj.data.datasetName")
        dObj5= driver.execute_script("return events.nodedeleted.eObj.data.link")
        dObj6= driver.execute_script("return events.nodedeleted.eObj.data.x")
        dObj7= driver.execute_script("return events.nodedeleted.eObj.data.y")
        dObj8= driver.execute_script("return events.nodedeleted.eObj.data.shape")
        dObj9= driver.execute_script("return events.nodedeleted.eObj.data.width")
        dObj10= driver.execute_script("return events.nodedeleted.eObj.data.height")
        #dObj11= driver.execute_script("return events.nodedeleted.eObj.data.radius")
        #dObj12= driver.execute_script("return events.nodedeleted.eObj.data.sides")
        dObj13= driver.execute_script("return events.nodedeleted.eObj.data.label")
        dObj14= driver.execute_script("return events.nodedeleted.eObj.data.toolText")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "nodedeleted":
            obj_param="eventType = ",eventType
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        except:
            report.entry_csv('nodedeleted', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "id should be number",chartType , "FAIL")
            
        
        
        if val.check_if_int(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "dataIndex should be number",chartType , "FAIL")
            
            
            
        if val.check_if_int(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "dataSetIndex should be number",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "datasetName should be a valid string",chartType , "FAIL")
        
        
        
        if dObj5 == "":
            obj_param="dObj5 = ",dObj5
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "link was not provided",chartType , "FAIL")    
            
            
            
        if val.check_if_int(dObj6):
            obj_param="dObj6 = ",dObj6
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "x is not int",chartType , "FAIL")    
            
            
            
        if val.check_if_int(dObj7):
            obj_param="dObj7 = ",dObj7
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "y is not int",chartType , "FAIL")  
            
            
            
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "shape should be valid string",chartType , "FAIL")
            
            
            
            
        if val.check_if_int(dObj9):
            obj_param="dObj9 = ",dObj9
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "width was not provided",chartType , "FAIL")   
            
            
            
        if val.check_if_int(dObj10):
            obj_param="dObj10 = ",dObj10
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "height was not provided",chartType , "FAIL") 
            
            
            
        if val.check_if_not_empty_string(dObj13):
            obj_param="dObj13 = ",dObj13
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "label was updated",chartType , "FAIL") 
            
            
            
        if val.check_if_not_empty_string(dObj14):
            obj_param="dObj14 = ",dObj14
            report.entry_csv('nodedeleted', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodedeleted', "toolText was not provided",chartType , "FAIL") 
               
        

            
    except Exception as e:
        report.entry_csv('nodedeleted', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

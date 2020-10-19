
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


def f_nodeupdated(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.nodeupdated.eObj.eventType")
        eventId= driver.execute_script("return events.nodeupdated.eObj.eventId")
        cancelled= driver.execute_script("return events.nodeupdated.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.nodeupdated.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.nodeupdated.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.nodeupdated.eObj.preventDefault")
        detached= driver.execute_script("return events.nodeupdated.eObj.detached")
        detachHandler= driver.execute_script("return events.nodeupdated.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.nodeupdated.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.nodeupdated.eObj.data.id")
        dObj2= driver.execute_script("return events.nodeupdated.eObj.data.dataIndex")
        dObj3= driver.execute_script("return events.nodeupdated.eObj.data.datasetIndex")
        dObj4= driver.execute_script("return events.nodeupdated.eObj.data.datasetName")
        dObj5= driver.execute_script("return events.nodeupdated.eObj.data.link")
        dObj6= driver.execute_script("return events.nodeupdated.eObj.data.x")
        dObj7= driver.execute_script("return events.nodeupdated.eObj.data.y")
        dObj8= driver.execute_script("return events.nodeupdated.eObj.data.shape")
        dObj9= driver.execute_script("return events.nodeupdated.eObj.data.width")
        dObj10= driver.execute_script("return events.nodeupdated.eObj.data.height")
        #dObj11= driver.execute_script("return events.nodeupdated.eObj.data.radius")
        #dObj12= driver.execute_script("return events.nodeupdated.eObj.data.sides")
        dObj13= driver.execute_script("return events.nodeupdated.eObj.data.label")
        dObj14= driver.execute_script("return events.nodeupdated.eObj.data.toolText")
        
        

        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "nodeupdated":
            obj_param="eventType = ",eventType
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        except:
            report.entry_csv('nodeupdated', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "senderChartType is not correct",chartType , "FAIL")
        
        
        
        if val.check_if_int(dObj1):
            obj_param="dObj1 = ",dObj1
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "id should be number",chartType , "FAIL")
            
        
        
        if val.check_if_int(dObj2):
            obj_param="dObj2 = ",dObj2
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "dataIndex should be number",chartType , "FAIL")
            
            
            
        if val.check_if_int(dObj3):
            obj_param="dObj3 = ",dObj3
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "dataSetIndex should be number",chartType , "FAIL")
            
            
            
        if val.check_if_not_empty_string(dObj4):
            obj_param="dObj4 = ",dObj4
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "datasetName should be a valid string",chartType , "FAIL")
        
        
        
        if dObj5 == "":
            obj_param="dObj5 = ",dObj5
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "link was not provided",chartType , "FAIL")    
            
            
            
        if val.check_if_int(dObj6):
            obj_param="dObj6 = ",dObj6
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "x is not int",chartType , "FAIL")    
            
            
            
        if val.check_if_int(dObj7):
            obj_param="dObj7 = ",dObj7
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "y is not int",chartType , "FAIL")  
            
            
            
        if val.check_if_not_empty_string(dObj8):
            obj_param="dObj8 = ",dObj8
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "shape should be valid string",chartType , "FAIL")
            
            
            
            
        if val.check_if_int(dObj9):
            obj_param="dObj9 = ",dObj9
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "width was not provided",chartType , "FAIL")   
            
            
            
        if val.check_if_int(dObj10):
            obj_param="dObj10 = ",dObj10
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "height was not provided",chartType , "FAIL") 
            
            
            
        if val.check_if_not_empty_string(dObj13):
            obj_param="dObj13 = ",dObj13
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "label was updated",chartType , "FAIL") 
            
            
            
        if val.check_if_not_empty_string(dObj14):
            obj_param="dObj14 = ",dObj14
            report.entry_csv('nodeupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('nodeupdated', "toolText was not provided",chartType , "FAIL") 
               
        

            
    except Exception as e:
        report.entry_csv('nodeupdated', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

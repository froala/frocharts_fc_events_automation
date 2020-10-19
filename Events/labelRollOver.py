
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
import time
import csv


def f_labelrollover(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.labelrollover.eObj.eventType")
        eventId= driver.execute_script("return events.labelrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.labelrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.labelrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.labelrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.labelrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.labelrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.labelrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.labelrollover.eObj.sender.chartType()")
        
        allowdrag= driver.execute_script("return events.labelrollover.eObj.data.allowdrag")
        chartX= driver.execute_script("return events.labelrollover.eObj.data.chartX")
        chartY= driver.execute_script("return events.labelrollover.eObj.data.chartY")
        link= driver.execute_script("return events.labelrollover.eObj.data.link")
        pageX= driver.execute_script("return events.labelrollover.eObj.data.pageX")
        pageY= driver.execute_script("return events.labelrollover.eObj.data.pageY")
        sourceType = driver.execute_script("return events.labelrollover.eObj.data.sourceType")
        text= driver.execute_script("return events.labelrollover.eObj.data.text")
        x = driver.execute_script("return events.labelrollover.eObj.data.x")
        y =driver.execute_script("return events.labelrollover.eObj.data.y")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "labelrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('labelrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_int(allowdrag):
            obj_param="allowdrag = ",allowdrag
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "allowdrag is not correct",chartType , "FAIL")
            print allowdrag
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "chartY is not correct",chartType , "FAIL")
            print chartY
            
         
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "link is not correct",chartType , "FAIL")
            print link
            
           
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "pageY is not correct",chartType , "FAIL")
            print pageY
            
        if val.check_if_not_empty_string(sourceType):
            obj_param="sourceType = ",sourceType
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "sourceType is not correct",chartType , "FAIL")
            print sourceType
        
        if val.check_if_not_empty_string(text):
            obj_param="text = ",text
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "text is not correct",chartType , "FAIL")
            print text
            
        if val.check_if_int(x):
            obj_param="x = ",x
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "x is not correct",chartType , "FAIL")
            print x
            
        if val.check_if_int(y):
            obj_param="y = ",y
            report.entry_csv('labelrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labelrollover', "y is not correct",chartType , "FAIL")
            print y
    
    except Exception as e:
        report.entry_csv('labelrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

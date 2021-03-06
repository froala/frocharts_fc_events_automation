
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


def f_labeldragstart(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.labeldragstart.eObj.eventType")
        eventId= driver.execute_script("return events.labeldragstart.eObj.eventId")
        cancelled= driver.execute_script("return events.labeldragstart.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.labeldragstart.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.labeldragstart.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.labeldragstart.eObj.preventDefault")
        detached= driver.execute_script("return events.labeldragstart.eObj.detached")
        detachHandler= driver.execute_script("return events.labeldragstart.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.labeldragstart.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.labeldragstart.eObj.data.chartX")
        chartY= driver.execute_script("return events.labeldragstart.eObj.data.chartY")
        pageX= driver.execute_script("return events.labeldragstart.eObj.data.pageX")
        pageY= driver.execute_script("return events.labeldragstart.eObj.data.pageY")
        x = driver.execute_script("return events.labeldragstart.eObj.data.x")
        y =driver.execute_script("return events.labeldragstart.eObj.data.y")
        allowdrag= driver.execute_script("return events.labeldragstart.eObj.data.allowdrag")
        link= driver.execute_script("return events.labeldragstart.eObj.data.link")
        sourceType = driver.execute_script("return events.labeldragstart.eObj.data.sourceType")
        text= driver.execute_script("return events.labeldragstart.eObj.data.text")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "labeldragstart":
            obj_param="eventType = ",eventType
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        except:
            report.entry_csv('labeldragstart', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "chartY is not correct",chartType , "FAIL")
            print chartY
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "pageY is not correct",chartType , "FAIL")
            print pageY
            
        if val.check_if_int(x):
            obj_param="x = ",x
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "x is not correct",chartType , "FAIL")
            print x
            
        if val.check_if_int(y):
            obj_param="y = ",y
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "y is not correct",chartType , "FAIL")
            print y
                
        if val.check_if_int(allowdrag):
            obj_param="allowdrag = ",allowdrag
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "allowdrag is not correct",chartType , "FAIL")
            print allowdrag
                   
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "link is not correct",chartType , "FAIL")
            print link
             
        if val.check_if_not_empty_string(sourceType):
            obj_param="sourceType = ",sourceType
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "sourceType is not correct",chartType , "FAIL")
            print sourceType
        
        if val.check_if_not_empty_string(text):
            obj_param="text = ",text
            report.entry_csv('labeldragstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('labeldragstart', "text is not correct",chartType , "FAIL")
            print text
            
        
    except Exception as e:
        report.entry_csv('labeldragstart', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

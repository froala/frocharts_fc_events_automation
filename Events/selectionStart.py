
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


def f_selectionstart(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.selectionstart.eObj.eventType")
        eventId= driver.execute_script("return events.selectionstart.eObj.eventId")
        cancelled= driver.execute_script("return events.selectionstart.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.selectionstart.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.selectionstart.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.selectionstart.eObj.preventDefault")
        detached= driver.execute_script("return events.selectionstart.eObj.detached")
        detachHandler= driver.execute_script("return events.selectionstart.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.selectionstart.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.selectionstart.eObj.data.chartX")
        chartY= driver.execute_script("return events.selectionstart.eObj.data.chartY")
        pageX= driver.execute_script("return events.selectionstart.eObj.data.pageX")
        pageY= driver.execute_script("return events.selectionstart.eObj.data.pageY")
        selectionHeight= driver.execute_script("return events.selectionstart.eObj.data.selectionHeight")
        selectionLeft= driver.execute_script("return events.selectionstart.eObj.data.selectionLeft")
        selectionTop= driver.execute_script("return events.selectionstart.eObj.data.selectionTop")
        selectionWidth= driver.execute_script("return events.selectionstart.eObj.data.selectionWidth")
        startXValue= driver.execute_script("return events.selectionstart.eObj.data.startXValue")
        startYValue= driver.execute_script("return events.selectionstart.eObj.data.startYValue")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "selectionstart":
            obj_param="eventType = ",eventType
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        except:
            report.entry_csv('selectionstart', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "chartY is not correct",chartType , "FAIL")
            print chartY
           
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "pageY is not correct",chartType , "FAIL")
            print pageY
           
        if val.check_if_int(selectionHeight):
            obj_param="selectionHeight = ",selectionHeight
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "selectionHeight is not correct",chartType , "FAIL")
            print selectionHeight
        
        if val.check_if_int(selectionLeft):
            obj_param="selectionLeft = ",selectionLeft
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "selectionLeft is not correct",chartType , "FAIL")
            print selectionLeft
            
        if val.check_if_int(selectionTop):
            obj_param="selectionTop = ",selectionTop
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "selectionTop is not correct",chartType , "FAIL")
            print selectionTop
            
        if val.check_if_int(selectionWidth):
            obj_param="selectionWidth = ",selectionWidth
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "selectionWidth is not correct",chartType , "FAIL")
            print selectionWidth
            
        if val.check_if_int(startXValue):
            obj_param="startXValue = ",startXValue
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "startXValue is not correct",chartType , "FAIL")
            print startXValue
            
        if val.check_if_int(startYValue):
            obj_param="startYValue = ",startYValue
            report.entry_csv('selectionstart', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionstart', "startYValue is not correct",chartType , "FAIL")
            print startYValue
            
        
    except Exception as e:
        report.entry_csv('selectionstart', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e


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


def f_legenditemclicked(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.legenditemclicked.eObj.eventType")
        eventId= driver.execute_script("return events.legenditemclicked.eObj.eventId")
        cancelled= driver.execute_script("return events.legenditemclicked.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.legenditemclicked.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.legenditemclicked.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.legenditemclicked.eObj.preventDefault")
        detached= driver.execute_script("return events.legenditemclicked.eObj.detached")
        detachHandler= driver.execute_script("return events.legenditemclicked.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.legenditemclicked.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.legenditemclicked.eObj.data.chartX")
        chartY= driver.execute_script("return events.legenditemclicked.eObj.data.chartY")
        datasetIndex= driver.execute_script("return events.legenditemclicked.eObj.data.legendItemIndex")
        datasetName= driver.execute_script("return events.legenditemclicked.eObj.data.datasetName")
        id= driver.execute_script("return events.legenditemclicked.eObj.data.id")
        legendItemId= driver.execute_script("return events.legenditemclicked.eObj.data.legendItemId")
        legendItemIndex= driver.execute_script("return events.legenditemclicked.eObj.data.legendItemIndex")
        pageX= driver.execute_script("return events.legenditemclicked.eObj.data.pageX")
        pageY= driver.execute_script("return events.legenditemclicked.eObj.data.pageY")
        visible= driver.execute_script("return events.legenditemclicked.eObj.data.visible")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "legenditemclicked":
            obj_param="eventType = ",eventType
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        except:
            report.entry_csv('legenditemclicked', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
          
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "chartY is not correct",chartType , "FAIL")
            print chartY
          
        if val.check_if_int(datasetIndex):
            obj_param="datasetIndex = ",datasetIndex
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "datasetIndex is not correct",chartType , "FAIL")
            print datasetIndex           
         
        if val.check_if_not_empty_string(datasetName):
            obj_param="datasetName = ",datasetName
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "datasetName is not correct",chartType , "FAIL")
            print datasetName
            
        if val.check_if_not_empty_string(id):
            obj_param="id = ",id
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "id is not correct",chartType , "FAIL")
            print id
            
        if val.check_if_not_empty_string(legendItemId):
            obj_param="legendItemId = ",legendItemId
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "legendItemId is not correct",chartType , "FAIL")
            print legendItemId
            
        if val.check_if_int(legendItemIndex):
            obj_param="legendItemIndex = ",legendItemIndex
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "legendItemIndex is not correct",chartType , "FAIL")
            print legendItemIndex       
       
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "pageY is not correct",chartType , "FAIL")
            print pageY 
           
        if val.check_if_not_empty_string(visible):
            obj_param="visible = ",visible
            report.entry_csv('legenditemclicked', obj_param, chartType, "PASS")
        else:
            report.entry_csv('legenditemclicked', "visible is not correct",chartType , "FAIL")
            print visible
            
               
    except Exception as e:
        report.entry_csv('legenditemclicked', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

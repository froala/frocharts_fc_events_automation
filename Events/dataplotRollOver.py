
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


def f_dataplotrollover(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataplotrollover.eObj.eventType")
        eventId= driver.execute_script("return events.dataplotrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.dataplotrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataplotrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataplotrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataplotrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.dataplotrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.dataplotrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataplotrollover.eObj.sender.chartType()")
        
        categoryLabel= driver.execute_script("return events.dataplotrollover.eObj.data.categoryLabel")
        chartX= driver.execute_script("return events.dataplotrollover.eObj.data.chartX")
        chartY= driver.execute_script("return events.dataplotrollover.eObj.data.chartY")
        dataIndex= driver.execute_script("return events.dataplotrollover.eObj.data.dataIndex")
        dataValue= driver.execute_script("return events.dataplotrollover.eObj.data.dataValue")
        datasetIndex= driver.execute_script("return events.dataplotrollover.eObj.data.datasetIndex")
        datasetName= driver.execute_script("return events.dataplotrollover.eObj.data.datasetName")
        displayValue= driver.execute_script("return events.dataplotrollover.eObj.data.displayValue")
        id= driver.execute_script("return events.dataplotrollover.eObj.data.id")
        index= driver.execute_script("return events.dataplotrollover.eObj.data.index")
        link= driver.execute_script("return events.dataplotrollover.eObj.data.link")
        pageX= driver.execute_script("return events.dataplotrollover.eObj.data.pageX")
        pageY= driver.execute_script("return events.dataplotrollover.eObj.data.pageY")
        toolText= driver.execute_script("return events.dataplotrollover.eObj.data.toolText")
        value= driver.execute_script("return events.dataplotrollover.eObj.data.value")
        visible= driver.execute_script("return events.dataplotrollover.eObj.data.visible")
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataplotrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataplotrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        if val.check_if_not_empty_string(categoryLabel):
            obj_param="categoryLabel = ",categoryLabel
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "categoryLabel is not correct",chartType , "FAIL")
            print categoryLabel
          
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "chartY is not correct",chartType , "FAIL")
            print chartY
           
        
        if val.check_if_int(dataIndex):
            obj_param="dataIndex = ",dataIndex
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "dataIndex is not correct",chartType , "FAIL")
            print dataIndex
        
        if val.check_if_int(dataValue):
            obj_param="dataValue = ",dataValue
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "dataValue is not correct",chartType , "FAIL")
            print dataValue
            
        if val.check_if_int(datasetIndex):
            obj_param="datasetIndex = ",datasetIndex
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "datasetIndex is not correct",chartType , "FAIL")
            print datasetIndex
            
        if val.check_if_not_empty_string(datasetName):
            obj_param="datasetName = ",datasetName
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "datasetName is not correct",chartType , "FAIL")
            print datasetName
            
        if val.check_if_not_empty_string(displayValue):
            obj_param="displayValue = ",displayValue
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "displayValue is not correct",chartType , "FAIL")
            print displayValue
            
#         if val.check_if_not_empty_string(id):
#             obj_param="id = ",id
#             report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('dataplotrollover', "id is not correct",chartType , "FAIL")
#             print id
            
        if val.check_if_not_empty_string(index):
            obj_param="index = ",index
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "index is not correct",chartType , "FAIL")
            print index    
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "link is not correct",chartType , "FAIL")
            print link
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "pageY is not correct",chartType , "FAIL")
            print pageY
            
        if val.check_if_not_empty_string(toolText):
            obj_param="toolText = ",toolText
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "toolText is not correct",chartType , "FAIL")
            print toolText
            
        if val.check_if_int(value):
            obj_param="value = ",value
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "value is not correct",chartType , "FAIL")
            print value 
            
        if val.check_if_not_empty_string(visible):
            obj_param="visible = ",visible
            report.entry_csv('dataplotrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotrollover', "visible is not correct",chartType , "FAIL")
            print visible
           
    except Exception as e:
        report.entry_csv('dataplotrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

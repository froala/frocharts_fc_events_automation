
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


def f_datalabelclick(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.datalabelclick.eObj.eventType")
        eventId= driver.execute_script("return events.datalabelclick.eObj.eventId")
        cancelled= driver.execute_script("return events.datalabelclick.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.datalabelclick.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.datalabelclick.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.datalabelclick.eObj.preventDefault")
        detached= driver.execute_script("return events.datalabelclick.eObj.detached")
        detachHandler= driver.execute_script("return events.datalabelclick.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.datalabelclick.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.datalabelclick.eObj.data.chartX")
        chartY= driver.execute_script("return events.datalabelclick.eObj.data.chartY")
        dataIndex= driver.execute_script("return events.datalabelclick.eObj.data.dataIndex")
        index= driver.execute_script("return events.datalabelclick.eObj.data.index")
        link= driver.execute_script("return events.datalabelclick.eObj.data.link")
        pageX= driver.execute_script("return events.datalabelclick.eObj.data.pageX")
        pageY= driver.execute_script("return events.datalabelclick.eObj.data.pageY")
        text= driver.execute_script("return events.datalabelclick.eObj.data.text")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "datalabelclick":
            obj_param="eventType = ",eventType
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        except:
            report.entry_csv('datalabelclick', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "chartY is not correct",chartType , "FAIL")
            print chartY
            
        if val.check_if_int(dataIndex):
            obj_param="dataIndex = ",dataIndex
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "dataIndex is not correct",chartType , "FAIL")
            print dataIndex
            
        if val.check_if_int(index):
            obj_param="index = ",index
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "index is not correct",chartType , "FAIL")
            print index
           
         
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "link is not correct",chartType , "FAIL")
            print link
            
           
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "pageY is not correct",chartType , "FAIL")
            print pageY
        
        if val.check_if_not_empty_string(text):
            obj_param="text = ",text
            report.entry_csv('datalabelclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('datalabelclick', "text is not correct",chartType , "FAIL")
            print text
    
    except Exception as e:
        report.entry_csv('datalabelclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e


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


def f_categoryclick(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.categoryclick.eObj.eventType")
        eventId= driver.execute_script("return events.categoryclick.eObj.eventId")
        cancelled= driver.execute_script("return events.categoryclick.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.categoryclick.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.categoryclick.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.categoryclick.eObj.preventDefault")
        detached= driver.execute_script("return events.categoryclick.eObj.detached")
        detachHandler= driver.execute_script("return events.categoryclick.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.categoryclick.eObj.sender.chartType()")
        
        align= driver.execute_script("return events.categoryclick.eObj.data.align")
        chartX= driver.execute_script("return events.categoryclick.eObj.data.chartX")
        chartY= driver.execute_script("return events.categoryclick.eObj.data.chartY")
        id= driver.execute_script("return events.categoryclick.eObj.data.id")
        isHeader= driver.execute_script("return events.categoryclick.eObj.data.isHeader")
        label= driver.execute_script("return events.categoryclick.eObj.data.label")
        link= driver.execute_script("return events.categoryclick.eObj.data.link")
        pageX= driver.execute_script("return events.categoryclick.eObj.data.pageX")
        pageY= driver.execute_script("return events.categoryclick.eObj.data.pageY")
        vAlign= driver.execute_script("return events.categoryclick.eObj.data.vAlign")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "categoryclick":
            obj_param="eventType = ",eventType
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        except:
            report.entry_csv('categoryclick', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_not_empty_string(align):
            obj_param="align = ",align
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "align is not correct",chartType , "FAIL")
            print align
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "chartY is not correct",chartType , "FAIL")
            print chartY
            
        if val.check_if_not_empty_string(id):
            obj_param="id = ",id
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "id is not correct",chartType , "FAIL")
            print id
            
        if val.check_if_not_empty_string(isHeader):
            obj_param="isHeader = ",isHeader
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "isHeader is not correct",chartType , "FAIL")
            print isHeader
            
          
         
        if val.check_if_not_empty_string(label):
            obj_param="label = ",label
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "label is not correct",chartType , "FAIL")
            print label
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "link is not correct",chartType , "FAIL")
            print link
            
           
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "pageY is not correct",chartType , "FAIL")
            print pageY
        
        if val.check_if_not_empty_string(vAlign):
            obj_param="vAlign = ",vAlign
            report.entry_csv('categoryclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryclick', "vAlign is not correct",chartType , "FAIL")
            print vAlign
            
            
            
    except Exception as e:
        report.entry_csv('categoryclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

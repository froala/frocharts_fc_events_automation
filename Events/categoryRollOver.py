
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


def f_categoryrollover(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.categoryrollover.eObj.eventType")
        eventId= driver.execute_script("return events.categoryrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.categoryrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.categoryrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.categoryrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.categoryrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.categoryrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.categoryrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.categoryrollover.eObj.sender.chartType()")
        
        align= driver.execute_script("return events.categoryrollover.eObj.data.align")
        chartX= driver.execute_script("return events.categoryrollover.eObj.data.chartX")
        chartY= driver.execute_script("return events.categoryrollover.eObj.data.chartY")
        id= driver.execute_script("return events.categoryrollover.eObj.data.id")
        isHeader= driver.execute_script("return events.categoryrollover.eObj.data.isHeader")
        label= driver.execute_script("return events.categoryrollover.eObj.data.label")
        link= driver.execute_script("return events.categoryrollover.eObj.data.link")
        pageX= driver.execute_script("return events.categoryrollover.eObj.data.pageX")
        pageY= driver.execute_script("return events.categoryrollover.eObj.data.pageY")
        vAlign= driver.execute_script("return events.categoryrollover.eObj.data.vAlign")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "categoryrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('categoryrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_not_empty_string(align):
            obj_param="align = ",align
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "align is not correct",chartType , "FAIL")
            print align
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "chartY is not correct",chartType , "FAIL")
            print chartY
            
#         if val.check_if_int(id):
#             obj_param="id = ",id
#             report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('categoryrollover', "id is not correct",chartType , "FAIL")
#             print id
            
        if val.check_if_not_empty_string(isHeader):
            obj_param="isHeader = ",isHeader
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "isHeader is not correct",chartType , "FAIL")
            print isHeader
            
          
         
        if val.check_if_not_empty_string(label):
            obj_param="label = ",label
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "label is not correct",chartType , "FAIL")
            print label
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "link is not correct",chartType , "FAIL")
            print link
            
           
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "pageY is not correct",chartType , "FAIL")
            print pageY
        
        if val.check_if_not_empty_string(vAlign):
            obj_param="vAlign = ",vAlign
            report.entry_csv('categoryrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('categoryrollover', "vAlign is not correct",chartType , "FAIL")
            print vAlign
            

    except Exception as e:
        report.entry_csv('categoryrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

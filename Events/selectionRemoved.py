
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


def f_selectionremoved(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.selectionremoved.eObj.eventType")
        eventId= driver.execute_script("return events.selectionremoved.eObj.eventId")
        cancelled= driver.execute_script("return events.selectionremoved.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.selectionremoved.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.selectionremoved.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.selectionremoved.eObj.preventDefault")
        detached= driver.execute_script("return events.selectionremoved.eObj.detached")
        detachHandler= driver.execute_script("return events.selectionremoved.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.selectionremoved.eObj.sender.chartType()")
        
        categories= driver.execute_script("return events.selectionend.eObj.data.categories")
        chart= driver.execute_script("return events.selectionend.eObj.data.chart")
        dataset= driver.execute_script("return events.selectionend.eObj.data.dataset")
        endXValue= driver.execute_script("return events.selectionend.eObj.data.endXValue")
        endYValue= driver.execute_script("return events.selectionend.eObj.data.endYValue")
        id= driver.execute_script("return events.selectionend.eObj.data.id")
        selectionHeight= driver.execute_script("return events.selectionremoved.eObj.data.selectionHeight")
        selectionLeft= driver.execute_script("return events.selectionremoved.eObj.data.selectionLeft")
        selectionTop= driver.execute_script("return events.selectionremoved.eObj.data.selectionTop")
        selectionWidth= driver.execute_script("return events.selectionremoved.eObj.data.selectionWidth")
        startXValue= driver.execute_script("return events.selectionremoved.eObj.data.startXValue")
        startYValue= driver.execute_script("return events.selectionremoved.eObj.data.startYValue")
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "selectionremoved":
            obj_param="eventType = ",eventType
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        except:
            report.entry_csv('selectionremoved', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
            
        if val.check_if_not_empty_string(categories):
            obj_param="categories = ",categories
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "categories is not correct",chartType , "FAIL")
            print categories
            
        if val.check_if_not_empty_string(chart):
            obj_param="chart = ",chart
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "chart is not correct",chartType , "FAIL")
            print chart
        
        if val.check_if_not_empty_string(dataset):
            obj_param="dataset = ",dataset
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "dataset is not correct",chartType , "FAIL")
            print dataset
        
        if val.check_if_int(endXValue):
            obj_param="endXValue = ",endXValue
            report.entry_csv('selectionend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionend', "endXValue is not correct",chartType , "FAIL")
            print endXValue
        
        if val.check_if_int(endYValue):
            obj_param="endYValue = ",endYValue
            report.entry_csv('selectionend', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionend', "endYValue is not correct",chartType , "FAIL")
            print endYValue
            
        if val.check_if_not_empty_string(id):
            obj_param="id = ",id
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "id is not correct",chartType , "FAIL")
            print id
            
                
        if val.check_if_int(selectionHeight):
            obj_param="selectionHeight = ",selectionHeight
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "selectionHeight is not correct",chartType , "FAIL")
            print selectionHeight
        
        if val.check_if_int(selectionLeft):
            obj_param="selectionLeft = ",selectionLeft
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "selectionLeft is not correct",chartType , "FAIL")
            print selectionLeft
            
        if val.check_if_int(selectionTop):
            obj_param="selectionTop = ",selectionTop
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "selectionTop is not correct",chartType , "FAIL")
            print selectionTop
            
        if val.check_if_int(selectionWidth):
            obj_param="selectionWidth = ",selectionWidth
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "selectionWidth is not correct",chartType , "FAIL")
            print selectionWidth
            
        if val.check_if_int(startXValue):
            obj_param="startXValue = ",startXValue
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "startXValue is not correct",chartType , "FAIL")
            print startXValue
            
        if val.check_if_int(startYValue):
            obj_param="startYValue = ",startYValue
            report.entry_csv('selectionremoved', obj_param, chartType, "PASS")
        else:
            report.entry_csv('selectionremoved', "startYValue is not correct",chartType , "FAIL")
            print startYValue
            
        
    except Exception as e:
        report.entry_csv('selectionremoved', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

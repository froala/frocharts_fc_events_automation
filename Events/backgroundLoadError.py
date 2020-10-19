
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


def f_backgroundloaderror(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)

        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.backgroundloaderror.eObj.eventType")
        eventId= driver.execute_script("return events.backgroundloaderror.eObj.eventId")
        cancelled= driver.execute_script("return events.backgroundloaderror.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.backgroundloaderror.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.backgroundloaderror.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.backgroundloaderror.eObj.preventDefault")
        detached= driver.execute_script("return events.backgroundloaderror.eObj.detached")
        detachHandler= driver.execute_script("return events.backgroundloaderror.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.backgroundloaderror.eObj.sender.chartType()")
        
        bgImageAlpha= driver.execute_script("return events.backgroundloaderror.eObj.data.bgImageAlpha")
        bgImageDisplayMode= driver.execute_script("return events.backgroundloaderror.eObj.data.bgImageDisplayMode")
        bgImageHAlign= driver.execute_script("return events.backgroundloaderror.eObj.data.bgImageHAlign")
        bgImageScale= driver.execute_script("return events.backgroundloaderror.eObj.data.bgImageScale")
        bgImageVAlign= driver.execute_script("return events.backgroundloaderror.eObj.data.bgImageVAlign")
        error= driver.execute_script("return events.backgroundloaderror.eObj.data.error.type")
        url= driver.execute_script("return events.backgroundloaderror.eObj.data.url")
        
        
        chartType = chartType.replace('_bgImageError','')
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "backgroundloaderror":
            obj_param="eventType = ",eventType
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        except:
            report.entry_csv('backgroundloaderror', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        
        if val.check_if_int(bgImageAlpha):
            obj_param="bgImageAlpha = ",bgImageAlpha
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "bgImageAlpha is not correct",chartType , "FAIL")
            print bgImageAlpha
            
            
        if val.check_if_not_empty_string(bgImageDisplayMode):
            obj_param="bgImageDisplayMode = ",bgImageDisplayMode
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "bgImageDisplayMode is not correct",chartType , "FAIL")
            print bgImageDisplayMode
            
        if val.check_if_not_empty_string(bgImageHAlign):
            obj_param="bgImageHAlign = ",bgImageHAlign
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "bgImageHAlign is not correct",chartType , "FAIL")
            print bgImageHAlign
            
        if val.check_if_int(bgImageScale):
            obj_param="bgImageScale = ",bgImageScale
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "bgImageScale is not correct",chartType , "FAIL")
            print bgImageScale
           
         
        if val.check_if_not_empty_string(bgImageVAlign):
            obj_param="bgImageVAlign = ",bgImageVAlign
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "bgImageVAlign is not correct",chartType , "FAIL")
            print bgImageVAlign
            
           
        '''if val.check_if_int(imageheight):
            obj_param="imageheight = ",bgImageAlpha
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "imageheight is not correct",chartType , "FAIL")
            print imageheight   
        
        if val.check_if_int(imagewidth):
            obj_param="imagewidth = ",bgImageAlpha
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "imagewidth is not correct",chartType , "FAIL")
            print imagewidth'''
            
        if val.check_if_not_empty_string(error):
            obj_param="error = ",bgImageVAlign
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "error is not correct",chartType , "FAIL")
            print error    
            
        
        if val.check_if_url(url):
            obj_param="url = ",url
            report.entry_csv('backgroundloaderror', obj_param, chartType, "PASS")
        else:
            report.entry_csv('backgroundloaderror', "url is not correct",chartType , "FAIL")
            print url
    
    except Exception as e:
        report.entry_csv('backgroundloaderror', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

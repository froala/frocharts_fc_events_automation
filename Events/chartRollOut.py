
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
from Events import pomFile as pom, pomFile
import time
import csv
from Util import chart


def f_chartrollout(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.chartrollout.eObj.eventType")
        eventId= driver.execute_script("return events.chartrollout.eObj.eventId")
        cancelled= driver.execute_script("return events.chartrollout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.chartrollout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.chartrollout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.chartrollout.eObj.preventDefault")
        detached= driver.execute_script("return events.chartrollout.eObj.detached")
        detachHandler= driver.execute_script("return events.chartrollout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.chartrollout.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.chartrollout.eObj.data.width")
        dObj2= driver.execute_script("return events.chartrollout.eObj.data.height")
        dObj3= driver.execute_script("return events.chartrollout.eObj.data.id")
        dObj4= driver.execute_script("return events.chartrollout.eObj.data.pageX")
        dObj5= driver.execute_script("return events.chartrollout.eObj.data.pageY")
        dObj6= driver.execute_script("return events.chartrollout.eObj.data.chartX")
        dObj7= driver.execute_script("return events.chartrollout.eObj.data.chartY")
        dObj8= driver.execute_script("return events.chartrollout.eObj.data.pixelWidth")
        dObj9= driver.execute_script("return events.chartrollout.eObj.data.pixelHeight")
        dObj10= driver.execute_script("return events.chartrollout.eObj.data.container.baseURI")
        dObj11= driver.execute_script("return events.chartrollout.eObj.data.renderer")
        
        
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "chartrollout":
            obj_param="eventType = ",eventType
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "width is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "height is not number",chartType , "FAIL")
            
            
            
        
    #         if val.check_if_not_empty_string(dObj3):
    #             obj_param="dObj3 = ",dObj3
    #             report.entry_csv('chartrollout', obj_param, chartType, "PASS")
    #         else:
    #             report.entry_csv('chartrollout', "id is empty",chartType , "FAIL")
        
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "pageX is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "pageY is not number",chartType , "FAIL")
            
        
        
        
        try:
            if val.check_if_int(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "chartX is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj7):
                obj_param="dObj7 = ",dObj7
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "chartY is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj8):
                obj_param="dObj8 = ",dObj8
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "pixelWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj9):
                obj_param="dObj9 = ",dObj9
                report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartrollout', "pixelHeight is not number",chartType , "FAIL")
            
            
            
            
        if dObj10 == chart.url_to_hit():
            obj_param="dObj10 = ",dObj10
            report.entry_csv('chartrollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartrollout', "baseURI is not matching",chartType , "FAIL")
        
                
        
        
            
    except Exception as e:
        report.entry_csv('chartrollout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

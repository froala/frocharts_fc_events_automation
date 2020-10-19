
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


def f_multipleinstanceschartrollover(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.chartrollover.eObj.eventType")
        eventId= driver.execute_script("return events.chartrollover.eObj.eventId")
        cancelled= driver.execute_script("return events.chartrollover.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.chartrollover.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.chartrollover.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.chartrollover.eObj.preventDefault")
        detached= driver.execute_script("return events.chartrollover.eObj.detached")
        detachHandler= driver.execute_script("return events.chartrollover.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.chartrollover.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.chartrollover.eObj.data.width")
        dObj2= driver.execute_script("return events.chartrollover.eObj.data.height")
        dObj3= driver.execute_script("return events.chartrollover.eObj.data.id")
        dObj4= driver.execute_script("return events.chartrollover.eObj.data.pageX")
        dObj5= driver.execute_script("return events.chartrollover.eObj.data.pageY")
        dObj6= driver.execute_script("return events.chartrollover.eObj.data.chartX")
        dObj7= driver.execute_script("return events.chartrollover.eObj.data.chartY")
        dObj8= driver.execute_script("return events.chartrollover.eObj.data.pixelWidth")
        dObj9= driver.execute_script("return events.chartrollover.eObj.data.pixelHeight")
        #dObj10= driver.execute_script("return events.chartrollover.eObj.data.container.baseURI")
        dObj11= driver.execute_script("return events.chartrollover.eObj.data.renderer")
        
        
        chartType = chartType.replace('_multipleinstances','')
        

        count_rollover = driver.execute_script("return getEventCount('chartrollover')");
        print("Roll Over Event count:",count_rollover)
        
        if count_rollover == 4:
            obj_param="count_rollover = ",count_rollover
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "count_rollover is not correct",chartType , "FAIL")
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "chartrollover":
            obj_param="eventType = ",eventType
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        else:
            report.entry_csv('RED-8931:chartrollover', "senderChartType is not correct",chartType , "FAIL")
            
            
            
        
        try:
            if val.check_if_int(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "width is not number",chartType , "FAIL")
            
        
        
        try:
            if val.check_if_int(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "height is not number",chartType , "FAIL")
            
            
            
        
    #         if val.check_if_not_empty_string(dObj3):
    #             obj_param="dObj3 = ",dObj3
    #             report.entry_csv('chartrollover', obj_param, chartType, "PASS")
    #         else:
    #             report.entry_csv('chartrollover', "id is empty",chartType , "FAIL")
        
            
            
            
        try:
            if val.check_if_int(dObj4):
                obj_param="dObj4 = ",dObj4
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "pageX is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj5):
                obj_param="dObj5 = ",dObj5
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "pageY is not number",chartType , "FAIL")
            
        
        
        
        try:
            if val.check_if_int(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "chartX is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj7):
                obj_param="dObj7 = ",dObj7
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "chartY is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj8):
                obj_param="dObj8 = ",dObj8
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "pixelWidth is not number",chartType , "FAIL")
            
            
            
            
        try:
            if val.check_if_int(dObj9):
                obj_param="dObj9 = ",dObj9
                report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
        except:
            report.entry_csv('RED-8931:chartrollover', "pixelHeight is not number",chartType , "FAIL")
            
            
            
            
#         if dObj10 == chart.url_to_hit():
#             obj_param="dObj10 = ",dObj10
#             report.entry_csv('RED-8931:chartrollover', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('RED-8931:chartrollover', "baseURI is not matching",chartType , "FAIL")
        
                
        
        
            
    except Exception as e:
        report.entry_csv('RED-8931:chartrollover', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        

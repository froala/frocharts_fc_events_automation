
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
from Events import pomFile as pom
import time
import csv
from Util import chart


def f_chartupdated(driver,chartType):
    
    try:
        
        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.chartupdated.eObj.eventType")
        eventId= driver.execute_script("return events.chartupdated.eObj.eventId")
        cancelled= driver.execute_script("return events.chartupdated.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.chartupdated.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.chartupdated.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.chartupdated.eObj.preventDefault")
        detached= driver.execute_script("return events.chartupdated.eObj.detached")
        detachHandler= driver.execute_script("return events.chartupdated.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.chartupdated.eObj.sender.chartType()")
        dObj1= driver.execute_script("return events.chartupdated.eObj.data.id")
        dObj2= driver.execute_script("return events.chartupdated.eObj.data.sourceEvent")
        dObj3= driver.execute_script("return events.chartupdated.eObj.data.sourceType")
        dObj4= driver.execute_script("return events.chartupdated.eObj.data.index")
        dObj5= driver.execute_script("return events.chartupdated.eObj.data.datasetIndex")
        dObj6= driver.execute_script("return events.chartupdated.eObj.data.datasetName")
        dObj7= driver.execute_script("return events.chartupdated.eObj.data.x")
        dObj8= driver.execute_script("return events.chartupdated.eObj.data.y")
        dObj9= driver.execute_script("return events.chartupdated.eObj.data.shape")
        dObj10= driver.execute_script("return events.chartupdated.eObj.data.width")
        dObj11= driver.execute_script("return events.chartupdated.eObj.data.height")
        dObj12= driver.execute_script("return events.chartupdated.eObj.data.radius")
        dObj13= driver.execute_script("return events.chartupdated.eObj.data.sides")
        dObj14= driver.execute_script("return events.chartupdated.eObj.data.label")
        dObj15= driver.execute_script("return events.chartupdated.eObj.data.toolText")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        
        if eventType == "chartupdated":
            obj_param="eventType = ",eventType
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        except:
            report.entry_csv('chartupdated', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "detachHandler is not a function",chartType , "FAIL")
                
        
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('chartupdated', obj_param, chartType, "PASS")
        else:
            report.entry_csv('chartupdated', "senderChartType is not correct",chartType , "FAIL")
            
        
        if chartType == "dragnode":
        
            if val.check_if_not_empty_string(dObj1):
                obj_param="dObj1 = ",dObj1
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "id is empty string",chartType , "FAIL")
            
            
            
            if val.check_if_not_empty_string(dObj2):
                obj_param="dObj2 = ",dObj2
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "sourceEvent is empty string",chartType , "FAIL")
            
            
            if val.check_if_not_empty_string(dObj3):
                obj_param="dObj3 = ",dObj3
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "sourceType is empty string",chartType , "FAIL")
            
            
            
            try:
                if val.check_if_int(dObj4):
                    obj_param="dObj1 = ",dObj1
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "index is not int",chartType , "FAIL")
            
            
            
            try:
                if val.check_if_int(dObj5):
                    obj_param="dObj5 = ",dObj5
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "datasetIndex is not int",chartType , "FAIL")
                
            
            
            if val.check_if_not_empty_string(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "datasetName is empty string",chartType , "FAIL")
                
                
            try:
                if val.check_if_number(dObj7):
                    obj_param="dObj7 = ",dObj7
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "x is not int",chartType , "FAIL")
                
                
            
            try:
                if val.check_if_number(dObj8):
                    obj_param="dObj8 = ",dObj8
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "y is not int",chartType , "FAIL")
                
                
            if val.check_if_not_empty_string(dObj9):
                obj_param="dObj9 = ",dObj9
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "shape is empty string",chartType , "FAIL")
                
                
            
            try:
                if val.check_if_int(dObj10):
                    obj_param="dObj10 = ",dObj10
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "width is not int",chartType , "FAIL")
                
                
            
            try:
                if val.check_if_int(dObj11):
                    obj_param="dObj11 = ",dObj11
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "height is not int",chartType , "FAIL")
                
                
                
            try:
                if val.check_if_int(dObj12):
                    obj_param="dObj12 = ",dObj12
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "radius is not int",chartType , "FAIL")
                
                
                
            try:
                if val.check_if_int(dObj13):
                    obj_param="dObj13 = ",dObj13
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "sides is not int",chartType , "FAIL")
                
                
            
            if val.check_if_not_empty_string(dObj14):
                obj_param="dObj14 = ",dObj14
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "label is empty string",chartType , "FAIL")
                
                
                
            if val.check_if_not_empty_string(dObj15):
                obj_param="dObj15 = ",dObj15
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "tooltext is empty string",chartType , "FAIL")
                
                
        else:
            
            dObj13= driver.execute_script("return events.chartupdated.eObj.data.dataIndex")
            dObj14= driver.execute_script("return events.chartupdated.eObj.data.endValue")
            dObj15= driver.execute_script("return events.chartupdated.eObj.data.startValue")
            try:
                if val.check_if_int(dObj5):
                    obj_param="dObj5 = ",dObj5
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "datasetIndex is not int",chartType , "FAIL")
                
                
                
            if val.check_if_not_empty_string(dObj6):
                obj_param="dObj6 = ",dObj6
                report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            else:
                report.entry_csv('chartupdated', "datasetName is empty string",chartType , "FAIL")
                
            
            try:
                if val.check_if_number(dObj13):
                    obj_param="dObj13 = ",dObj13
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "dataIndex is not number",chartType , "FAIL")
                
            
            try:
                if val.check_if_number(dObj14):
                    obj_param="dObj14 = ",dObj14
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "endValue is not number",chartType , "FAIL")
                
                
            
            try:
                if val.check_if_number(dObj15):
                    obj_param="dObj15 = ",dObj15
                    report.entry_csv('chartupdated', obj_param, chartType, "PASS")
            except:
                report.entry_csv('chartupdated', "startValue is not number",chartType , "FAIL")
        
            
    except Exception as e:
        report.entry_csv('chartupdated', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e
        


    
        
        
    
    
    
    
    
    

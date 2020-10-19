
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


def f_milestonerollout(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.milestonerollout.eObj.eventType")
        eventId= driver.execute_script("return events.milestonerollout.eObj.eventId")
        cancelled= driver.execute_script("return events.milestonerollout.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.milestonerollout.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.milestonerollout.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.milestonerollout.eObj.preventDefault")
        detached= driver.execute_script("return events.milestonerollout.eObj.detached")
        detachHandler= driver.execute_script("return events.milestonerollout.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.milestonerollout.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.milestonerollout.eObj.data.chartX")
        chartY= driver.execute_script("return events.milestonerollout.eObj.data.chartY")
        date= driver.execute_script("return events.milestonerollout.eObj.data.date")
        link= driver.execute_script("return events.milestonerollout.eObj.data.link")
        numSides= driver.execute_script("return events.milestonerollout.eObj.data.numSides")
        pageX= driver.execute_script("return events.milestonerollout.eObj.data.pageX")
        pageY= driver.execute_script("return events.milestonerollout.eObj.data.pageY")
        radius= driver.execute_script("return events.milestonerollout.eObj.data.radius")
        sides= driver.execute_script("return events.milestonerollout.eObj.data.sides")
        taskId= driver.execute_script("return events.milestonerollout.eObj.data.taskId")
        toolText= driver.execute_script("return events.milestonerollout.eObj.data.toolText")
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "milestonerollout":
            obj_param="eventType = ",eventType
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        except:
            report.entry_csv('milestonerollout', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "chartY is not correct",chartType , "FAIL")
            print chartY
            
            
        if val.check_if_not_empty_string(date):
            obj_param="date = ",date
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "date is not correct",chartType , "FAIL")
            print date
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "link is not correct",chartType , "FAIL")
            print link
               
        if val.check_if_int(numSides):
            obj_param="numSides = ",numSides
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "numSides is not correct",chartType , "FAIL")
            print numSides
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "pageY is not correct",chartType , "FAIL")
            print pageY          
         
        if val.check_if_not_empty_string(radius):
            obj_param="radius = ",radius
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "radius is not correct",chartType , "FAIL")
            print radius
            
        if val.check_if_not_empty_string(sides):
            obj_param="sides = ",sides
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "sides is not correct",chartType , "FAIL")
            print sides
            
        if val.check_if_int(taskId):
            obj_param="taskId = ",taskId
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "taskId is not correct",chartType , "FAIL")
            print taskId  
            
        if val.check_if_not_empty_string(toolText):
            obj_param="toolText = ",toolText
            report.entry_csv('milestonerollout', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestonerollout', "toolText is not correct",chartType , "FAIL")
            print toolText    
            
            
    except Exception as e:
        report.entry_csv('milestonerollout', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

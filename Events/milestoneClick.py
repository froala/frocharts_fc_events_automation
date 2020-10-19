
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


def f_milestoneclick(driver, chartType):
    
    try:

        time.sleep(2)
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.milestoneclick.eObj.eventType")
        eventId= driver.execute_script("return events.milestoneclick.eObj.eventId")
        cancelled= driver.execute_script("return events.milestoneclick.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.milestoneclick.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.milestoneclick.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.milestoneclick.eObj.preventDefault")
        detached= driver.execute_script("return events.milestoneclick.eObj.detached")
        detachHandler= driver.execute_script("return events.milestoneclick.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.milestoneclick.eObj.sender.chartType()")
        
        chartX= driver.execute_script("return events.milestoneclick.eObj.data.chartX")
        chartY= driver.execute_script("return events.milestoneclick.eObj.data.chartY")
        date= driver.execute_script("return events.milestoneclick.eObj.data.date")
        link= driver.execute_script("return events.milestoneclick.eObj.data.link")
        numSides= driver.execute_script("return events.milestoneclick.eObj.data.numSides")
        pageX= driver.execute_script("return events.milestoneclick.eObj.data.pageX")
        pageY= driver.execute_script("return events.milestoneclick.eObj.data.pageY")
        radius= driver.execute_script("return events.milestoneclick.eObj.data.radius")
        sides= driver.execute_script("return events.milestoneclick.eObj.data.sides")
        taskId= driver.execute_script("return events.milestoneclick.eObj.data.taskId")
        toolText= driver.execute_script("return events.milestoneclick.eObj.data.toolText")
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "milestoneclick":
            obj_param="eventType = ",eventType
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        except:
            report.entry_csv('milestoneclick', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "preventDefault is not a function",chartType , "FAIL")
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "detached is not boolean",chartType , "FAIL")
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "detachHandler is not a function",chartType , "FAIL")
                
                
                
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
          
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "chartY is not correct",chartType , "FAIL")
            print chartY
            
            
        if val.check_if_not_empty_string(date):
            obj_param="date = ",date
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "date is not correct",chartType , "FAIL")
            print date
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "link is not correct",chartType , "FAIL")
            print link
               
        if val.check_if_int(numSides):
            obj_param="numSides = ",numSides
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "numSides is not correct",chartType , "FAIL")
            print numSides
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "pageY is not correct",chartType , "FAIL")
            print pageY          
         
        if val.check_if_not_empty_string(radius):
            obj_param="radius = ",radius
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "radius is not correct",chartType , "FAIL")
            print radius
            
        if val.check_if_not_empty_string(sides):
            obj_param="sides = ",sides
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "sides is not correct",chartType , "FAIL")
            print sides
            
        if val.check_if_int(taskId):
            obj_param="taskId = ",taskId
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "taskId is not correct",chartType , "FAIL")
            print taskId  
            
        if val.check_if_not_empty_string(toolText):
            obj_param="toolText = ",toolText
            report.entry_csv('milestoneclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('milestoneclick', "toolText is not correct",chartType , "FAIL")
            print toolText    
            
    except Exception as e:
        report.entry_csv('milestoneclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e


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


def f_dataplotclickline(driver, chartType):
    
    try:

        time.sleep(2)
        
        print "\n"
        print "chart type = ",chartType
        print "dataplotclick"
        print "\n"
        
        report.jsError_exists(chartType)
        
        #Assigning each of the event specific attributes to different variables  
        eventType= driver.execute_script("return events.dataplotclick.eObj.eventType")
        eventId= driver.execute_script("return events.dataplotclick.eObj.eventId")
        cancelled= driver.execute_script("return events.dataplotclick.eObj.cancelled")
        stopPropagation= driver.execute_script("return events.dataplotclick.eObj.stopPropagation")
        defaultPrevented= driver.execute_script("return events.dataplotclick.eObj.defaultPrevented")
        preventDefault= driver.execute_script("return events.dataplotclick.eObj.preventDefault")
        detached= driver.execute_script("return events.dataplotclick.eObj.detached")
        detachHandler= driver.execute_script("return events.dataplotclick.eObj.detachHandler")
        senderChartType= driver.execute_script("return events.dataplotclick.eObj.sender.chartType()")
        
        categoryLabel= driver.execute_script("return events.dataplotclick.eObj.data.categoryLabel")
        chartX= driver.execute_script("return events.dataplotclick.eObj.data.chartX")
        chartY= driver.execute_script("return events.dataplotclick.eObj.data.chartY")
        dataIndex= driver.execute_script("return events.dataplotclick.eObj.data.dataIndex")
        dataValue= driver.execute_script("return events.dataplotclick.eObj.data.dataValue")
        datasetIndex= driver.execute_script("return events.dataplotclick.eObj.data.datasetIndex")
        datasetName= driver.execute_script("return events.dataplotclick.eObj.data.datasetName")
        displayValue= driver.execute_script("return events.dataplotclick.eObj.data.displayValue")
        id= driver.execute_script("return events.dataplotclick.eObj.data.id")
        index= driver.execute_script("return events.dataplotclick.eObj.data.index")
        link= driver.execute_script("return events.dataplotclick.eObj.data.link")
        pageX= driver.execute_script("return events.dataplotclick.eObj.data.pageX")
        pageY= driver.execute_script("return events.dataplotclick.eObj.data.pageY")
        toolText= driver.execute_script("return events.dataplotclick.eObj.data.toolText")
        value= driver.execute_script("return events.dataplotclick.eObj.data.value")
        visible= driver.execute_script("return events.dataplotclick.eObj.data.visible")
        
        color= driver.execute_script("return events.dataplotclick.eObj.data.color")
        print "color = ",color
        alpha= driver.execute_script("return events.dataplotclick.eObj.data.alpha")
        print "alpha = ",alpha
        anchorAlpha= driver.execute_script("return events.dataplotclick.eObj.data.anchorAlpha")
        print "anchorAlpha = ",anchorAlpha
        anchorBgAlpha= driver.execute_script("return events.dataplotclick.eObj.data.anchorBgAlpha")
        print "anchorBgAlpha = ",anchorBgAlpha
        anchorBgColor= driver.execute_script("return events.dataplotclick.eObj.data.anchorBgColor")
        print "anchorBgColor = ",anchorBgColor
        anchorBorderColor= driver.execute_script("return events.dataplotclick.eObj.data.anchorBorderColor")
        print "anchorBorderColor = ",anchorBorderColor
        anchorBorderThickness= driver.execute_script("return events.dataplotclick.eObj.data.anchorBorderThickness")
        print "anchorBorderThickness = ",anchorBorderThickness
        anchorRadius= driver.execute_script("return events.dataplotclick.eObj.data.anchorRadius")
        print "anchorRadius = ",anchorRadius
        anchorSides= driver.execute_script("return events.dataplotclick.eObj.data.anchorSides")
        print "anchorSides = ",anchorSides
        anchorStartAngle= driver.execute_script("return events.dataplotclick.eObj.data.anchorStartAngle")
        print "anchorStartAngle = ",anchorStartAngle
        anchorHoverColor= driver.execute_script("return events.dataplotclick.eObj.data.anchorHoverColor")
        print "anchorHoverColor = ",anchorHoverColor
        anchorHoverAlpha= driver.execute_script("return events.dataplotclick.eObj.data.anchorHoverAlpha")
        print "anchorHoverAlpha = ",anchorHoverAlpha
        anchorHoverSides= driver.execute_script("return events.dataplotclick.eObj.data.anchorHoverSides")
        print "anchorHoverSides = ",anchorHoverSides
        dashed= driver.execute_script("return events.dataplotclick.eObj.data.dashed")
        print "dashed = ",dashed
        valuePosition= driver.execute_script("return events.dataplotclick.eObj.data.valuePosition")
        print "valuePosition = ",valuePosition
        link= driver.execute_script("return events.dataplotclick.eObj.data.link")
        print "link = ",link
        
        
        
        #Validating all the attributes whether their values fetched are correct for the particular event
        
        if eventType == "dataplotclick":
            obj_param="eventType = ",eventType
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "eventType is not correct",chartType , "FAIL")
        
        
        try:
            if val.check_if_int(eventId):
                obj_param="eventId = ",eventId
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        except:
            report.entry_csv('dataplotclick', "eventId is not an int",chartType , "FAIL")
        
        
        
        if val.check_if_boolean(cancelled):
            obj_param="cancelled = ",cancelled
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "cancelled is not boolean",chartType , "FAIL")
        
        
        
        if val.check_if_function(stopPropagation):
            obj_param="stopPropagation = ",stopPropagation
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "stopPropagation is not a function",chartType , "FAIL")
                
               
        
        
        if val.check_if_boolean(defaultPrevented):
                obj_param="defaultPrevented = ",defaultPrevented
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "defaultPrevented is not boolean",chartType , "FAIL") 
            
            
            
        if val.check_if_function(preventDefault):
                obj_param="preventDefault = ",preventDefault
                report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "preventDefault is not a function",chartType , "FAIL")
                
                
                
        
        if val.check_if_boolean(detached):
            obj_param="detached = ",detached
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "detached is not boolean",chartType , "FAIL")
                
        
        
        
        if val.check_if_function(detachHandler):
            obj_param="detachHandler = ",detachHandler
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "detachHandler is not a function",chartType , "FAIL")
                
                
                  
        if senderChartType == chartType:
            obj_param="senderChartType = ",senderChartType
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "senderChartType is not correct",chartType , "FAIL")
            print senderChartType
        
        if val.check_if_not_empty_string(categoryLabel):
            obj_param="categoryLabel = ",categoryLabel
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "categoryLabel is not correct",chartType , "FAIL")
            print categoryLabel
          
        if val.check_if_int(chartX):
            obj_param="chartX = ",chartX
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "chartX is not correct",chartType , "FAIL")
            print chartX
            
            
        if val.check_if_int(chartY):
            obj_param="chartY = ",chartY
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "chartY is not correct",chartType , "FAIL")
            print chartY
           
        
        if val.check_if_int(dataIndex):
            obj_param="dataIndex = ",dataIndex
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "dataIndex is not correct",chartType , "FAIL")
            print dataIndex
        
        if val.check_if_int(dataValue):
            obj_param="dataValue = ",dataValue
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "dataValue is not correct",chartType , "FAIL")
            print dataValue
            
        if val.check_if_int(datasetIndex):
            obj_param="datasetIndex = ",datasetIndex
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "datasetIndex is not correct",chartType , "FAIL")
            print datasetIndex
            
        if val.check_if_not_empty_string(datasetName):
            obj_param="datasetName = ",datasetName
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "datasetName is not correct",chartType , "FAIL")
            print datasetName
            
        if val.check_if_not_empty_string(displayValue):
            obj_param="displayValue = ",displayValue
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "displayValue is not correct",chartType , "FAIL")
            print displayValue
            
#         if val.check_if_not_empty_string(id):
#             obj_param="id = ",id
#             report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
#         else:
#             report.entry_csv('dataplotclick', "id is not correct",chartType , "FAIL")
#             print id
            
        if val.check_if_not_empty_string(index):
            obj_param="index = ",index
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "index is not correct",chartType , "FAIL")
            print index    
            
        if val.check_if_not_empty_string(link):
            obj_param="link = ",link
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "link is not correct",chartType , "FAIL")
            print link
            
        if val.check_if_int(pageX):
            obj_param="pageX = ",pageX
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "pageX is not correct",chartType , "FAIL")
            print pageX   
        
        if val.check_if_int(pageY):
            obj_param="pageY = ",pageY
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "pageY is not correct",chartType , "FAIL")
            print pageY
            
        if val.check_if_not_empty_string(toolText):
            obj_param="toolText = ",toolText
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "toolText is not correct",chartType , "FAIL")
            print toolText
            
        if val.check_if_int(value):
            obj_param="value = ",value
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "value is not correct",chartType , "FAIL")
            print value 
            
        if val.check_if_not_empty_string(visible):
            obj_param="visible = ",visible
            report.entry_csv('dataplotclick', obj_param, chartType, "PASS")
        else:
            report.entry_csv('dataplotclick', "visible is not correct",chartType , "FAIL")
            print visible
           
    except Exception as e:
        report.entry_csv('dataplotclick', "ERROR: There is an issue with event objects",chartType , "FAIL")
        print e

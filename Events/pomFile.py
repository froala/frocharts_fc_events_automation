from selenium.webdriver.common.action_chains import ActionChains
import time
from Util import Validate as val
from Util import Report as report
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#from buildtools import process

from unicodedata import category


class PageObjectModel:
    
    browser = ""
    
    def click_submit(self,driver,chartType):
        try:
            
            
            g_elements = driver.find_elements_by_tag_name('g')
            
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    driver.execute_script("arguments[0].scrollIntoView();", g_elem)
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            time.sleep(2)
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Submit":
                    ActionChains(driver).move_to_element(span).perform()
                    #ActionChains(driver).click(span.find_element_by_xpath("..")).perform()
                    span.click()
                    break
        except Exception as e:
            report.entry_csv('editable_event', "ERROR: There is an issue with clicking submit",chartType , "FAIL")
    
    
    
    def click_save(self,driver,chartType):
        try:
            time.sleep(3)
            g_elements = driver.find_elements_by_tag_name('g')
            driver.find_element_by_tag_name('svg').click()
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    driver.execute_script("arguments[0].scrollIntoView();", g_elem)
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
                    time.sleep(1)
                    ActionChains(driver).move_by_offset(0,1).perform()
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Save":
                    ActionChains(driver).move_to_element(span).perform()
                    span.click()
                    break
        except Exception as e:
            print(e)
            report.entry_csv('editable_event', "ERROR: There is an issue with clicking save",chartType , "FAIL")
            
            
            
    def click_restore(self,driver,chartType):
        try:
            span_elements = driver.find_elements_by_tag_name('span')
            #submit_btn = driver.find_element_by_tag_name('span')
            g_elements = driver.find_elements_by_tag_name('g')
            
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    driver.execute_script("arguments[0].scrollIntoView();", g_elem)
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            for span in span_elements:
                if span.text == "Restore":
                    span.click()
                    break
        except Exception as e:
            report.entry_csv('editable_event', "ERROR: There is an issue with clicking submit",chartType , "FAIL")
            
            
            
    def add_update_delete_node(self,driver,chartType):
        try:
            
            
            div_elements = driver.find_elements_by_tag_name('div')
            g_elements = driver.find_elements_by_tag_name('g')
            
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Add Node":
                    span.click()
                    break
            
            driver.find_element_by_name('id').send_keys('2435') 
            driver.find_element_by_name('id').send_keys(u'\ue007')
                
            all_rect_nodes = driver.find_elements_by_tag_name('rect')
              
            for rects in all_rect_nodes:
                if rects.get_attribute('width') == '10' and rects.get_attribute('height') == '10':
                    driver.execute_script("arguments[0].scrollIntoView();", rects)
                    ActionChains(driver).move_to_element(rects).perform()
                    ActionChains(driver).click_and_hold().perform()
                    time.sleep(2)
                    ActionChains(driver).release().perform()
                    break
              
            driver.find_element_by_name('label').send_keys('label1') 
            driver.find_element_by_name('label').send_keys(u'\ue007')
            
            for rects in all_rect_nodes:
                if rects.get_attribute('width') == '10' and rects.get_attribute('height') == '10':
                    driver.execute_script("arguments[0].scrollIntoView();", rects)
                    ActionChains(driver).move_to_element(rects).perform()
                    ActionChains(driver).click_and_hold().perform()
                    time.sleep(2)
                    ActionChains(driver).release().perform()
                    break
            
            delete_parent = driver.find_element_by_name('label').find_element_by_xpath("../..")
            
            
            for div in delete_parent.find_elements_by_tag_name('div'):
                if div.get_attribute('tabindex') == '3':
                    ActionChains(driver).move_to_element(div).perform()
                    ActionChains(driver).move_by_offset(0, 2).perform()
                    driver.execute_script("arguments[0].click();", div)
                    div.click()
                    break
              
        except Exception as e:
            print e
            report.entry_csv('draggingevent', "ERROR: There is an issue with clicking Add Node",chartType , "FAIL")
    
    
    
    def add_connector(self,driver,chartType):
        try:
            
            div_elements = driver.find_elements_by_tag_name('div')
            g_elements = driver.find_elements_by_tag_name('g')  
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Add Connector":
                    span.click()
                    break
            
            driver.find_element_by_name('toid').click() 
            to_select = Select(driver.find_element_by_name('toid'))
            to_select.select_by_value('10')
            driver.find_element_by_name('id').send_keys('67')
            driver.find_element_by_name('label').send_keys('20')
            driver.find_element_by_name('strength').clear()
            driver.find_element_by_name('strength').send_keys('6')
            time.sleep(2)
            
            for div in driver.find_element_by_name('label').find_element_by_xpath("../..").find_elements_by_tag_name('div'):
                if div.get_attribute('tabindex') == '1':
                    div.click()
              
        except Exception as e:
            print e
            report.entry_csv('draggingevent', "ERROR: There is an issue with clicking Add Node",chartType , "FAIL")
    
    
    
    def update_delete_connector(self,driver,chartType):
#         try:
        span_elements = driver.find_elements_by_tag_name('span')
        div_elements = driver.find_elements_by_tag_name('div')
        g_elements = driver.find_elements_by_tag_name('g')  
        
        #Updating a connector
        connector_parent = driver.find_element_by_xpath("//*[contains(@class,'connectorGroup')]").find_element_by_tag_name('g')
        connector_new= driver.find_elements_by_tag_name('svg')
        all_connectors = connector_parent.find_elements_by_xpath(".//*")
        
        for conn in all_connectors:
            connector_new = conn
            break
            
        driver.execute_script("arguments[0].scrollIntoView();", connector_new)
        ActionChains(driver).move_to_element(connector_new).perform()
        ActionChains(driver).click_and_hold().perform()
        time.sleep(2)
        ActionChains(driver).release().perform()
        
        time.sleep(2)
        #driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_name('label'))
        driver.execute_script("arguments[0].click();", driver.find_element_by_name('label'))#driver.find_element_by_name('label').click()
        driver.find_element_by_name('label').clear()
        driver.find_element_by_name('label').send_keys('30')
        
        for div in driver.find_element_by_name('label').find_element_by_xpath("../..").find_elements_by_tag_name('div'):
            if div.get_attribute('tabindex') == '1':
                div.click()
        
        #Deleting a connector
        driver.execute_script("arguments[0].scrollIntoView();", connector_new)
        ActionChains(driver).move_to_element(connector_new).perform()
        ActionChains(driver).click_and_hold().perform()
        time.sleep(2)
        ActionChains(driver).release().perform()
        
        for div in driver.find_element_by_name('label').find_element_by_xpath("../..").find_elements_by_tag_name('div'):
            if div.get_attribute('tabindex') == '3':
                div.click()
                    
            
    
    def drag_any_plot(self,driver,chartType):
        if chartType == "dragcolumn2d":
            try:
                g_elements = driver.find_elements_by_tag_name('g')
                
                for g_elem in g_elements:
                    if "plot-group" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_xpath('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:                                
                                driver.execute_script("arguments[0].scrollIntoView();", plot)
                                ActionChains(driver).move_to_element(plot).perform()
                                ActionChains(driver).move_by_offset(1,0).perform()
                                dragged = 1
                                break
                            if dragged == 1:
                                break
                            
                tooltip_element = driver.find_element_by_css_selector('.fc__tooltip.fusioncharts-div')
                
                for g_elem in g_elements:
                    if "plot-group" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_xpath('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:
                                ActionChains(driver).move_to_element(plot).perform()
                                dragged=1 
                                break
                        if dragged>0:
                            while val.check_if_not_empty_string(tooltip_element.text):
                                ActionChains(driver).move_by_offset(0,-5).perform() 
                
                ActionChains(driver).click_and_hold().perform()
                ActionChains(driver).move_by_offset(0, 30).perform()
                ActionChains(driver).release().perform()
            except Exception as e:
                report.entry_csv('draggingevent', "ERROR: There is an issue with dragging",chartType , "FAIL")
                print(e)
                
                
            
            
            
        elif chartType == "dragnode" :
            try:
                #ActionChains(driver).move_to_element(main_chart).perform()
                g_elements = driver.find_elements_by_tag_name('g')
                
                for g_elem in g_elements:
                    if "nodesGroup" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_tag_name('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:
                                ActionChains(driver).move_to_element(plot).perform()
                                break
                            
                tooltip_element = driver.find_element_by_css_selector('.fc__tooltip.fusioncharts-div')
                print(tooltip_element)
                
                for g_elem in g_elements:
                    if "nodesGroup" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_tag_name('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:
                                ActionChains(driver).move_to_element(plot).perform()
                                ActionChains(driver).click_and_hold().perform()
                                ActionChains(driver).move_by_offset(0, 30).perform()
                                ActionChains(driver).release().perform()
                                dragged=1 
                                break
                        if dragged>0:
                            break
            except Exception as e:
                report.entry_csv('draggingevent', "ERROR: There is an issue with dragging",chartType , "FAIL")
                print(e)
                
                
        else:
            try:
                g_elements = driver.find_elements_by_tag_name('g')
                
                for g_elem in g_elements:
                    if "plot-group" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_tag_name('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:
                                ActionChains(driver).move_to_element(plot).perform()
                                break
                            
                tooltip_element = driver.find_element_by_css_selector('.fc__tooltip.fusioncharts-div')
                
                for g_elem in g_elements:
                    if "plot-group" in g_elem.get_attribute("class"):
                        dragged=0
                        all_elements = g_elem.find_elements_by_tag_name('*')
                        if len(all_elements) > 0 :
                            for plot in all_elements:
                                ActionChains(driver).move_to_element(plot).perform()
                                ActionChains(driver).click_and_hold().perform()
                                ActionChains(driver).move_by_offset(0, 30).perform()
                                ActionChains(driver).release().perform()
                                dragged=1
                                break
                        if dragged>0:
                            break
            except Exception as e:
                report.entry_csv('draggingevent', "ERROR: There is an issue with dragging",chartType , "FAIL")
                print(e)
                
                
    def datalabel_click_rollover_rollout(self,driver,chartType):
        try:
            g_elements = driver.find_elements_by_tag_name('g')
            
            for allG in g_elements:
                if allG.get_attribute('class').endswith('dataset-axis'):
                    print "in dataset"
                    datasetTexts=allG.find_elements_by_tag_name('text')
                    for dataLabel in datasetTexts:
                        driver.execute_script("arguments[0].scrollIntoView();", dataLabel)
                        ActionChains(driver).move_to_element(dataLabel).perform()
                        dataLabel.click()
                        ActionChains(driver).click(dataLabel).perform()
                        ActionChains(driver).move_by_offset(1,0).perform()
                        dataLabel.click()
                        ActionChains(driver).click(dataLabel).perform()
                        ActionChains(driver).move_by_offset(20,0).perform()
                        ActionChains(driver).move_by_offset(0,20).perform() 
            time.sleep(2)
        except Exception as e:
            report.entry_csv('DataLabel Events', "ERROR: There is an issue with clicking on Data Label",chartType , "FAIL")
            print ("datalabel issue = ",e)
            
            
            
    def label_added_deleted(self,driver,chartType):
        try:
            
            
            g_elements = driver.find_elements_by_tag_name('g')
            
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Add Label":
                    span.click()
                    break    
            driver.find_element_by_name('label').send_keys('Test Label')
            driver.find_element_by_name('x').send_keys('30')
            driver.find_element_by_name('y').send_keys('30')
            driver.find_element_by_name('label').send_keys(u'\ue007')
                
            dragLabel = driver.find_element_by_xpath("//*[contains(@class,'dragLabelGroup')]")
            
            
            rect_elem = dragLabel.find_element_by_tag_name('rect')
            
            ActionChains(driver).move_to_element(rect_elem).perform()
            ActionChains(driver).move_by_offset(0,-1).perform() 
            ActionChains(driver).click_and_hold(rect_elem).perform()
            time.sleep(2)
            ActionChains(driver).release().perform()
            
            divs = driver.find_elements_by_tag_name('div')
            
            for div in divs:
                if div.text == 'Delete':
                    ActionChains(driver).move_to_element(div).perform()
                    ActionChains(driver).click(div).perform()
                    ActionChains(driver).move_by_offset(0, -10).perform()
                    ActionChains(driver).click(div).perform()
                    ActionChains(driver).move_by_offset(0, 10).perform()
                    ActionChains(driver).click(div).perform()
            
        except Exception as e:
            report.entry_csv('DataLabel Events', "ERROR: There is an issue with adding or Deleting the Label",chartType , "FAIL")           
            
                          
                          
    def label_click_rollover_rollout(self, driver,chartType):
#         try:
        
        div_elements = driver.find_elements_by_tag_name('div')
        g_elements = driver.find_elements_by_tag_name('g')
        
        for g_elem in g_elements:
            if "button" in g_elem.get_attribute('class'):
                ActionChains(driver).move_to_element(g_elem).perform()
                ActionChains(driver).move_by_offset(0,-1).perform() 
        
        span_elements = driver.find_elements_by_tag_name('span')
        
        for span in span_elements:
            if span.text == "Add Label":
                span.click()
                break    
        driver.find_element_by_name('label').send_keys('Test Label')
        driver.find_element_by_name('x').send_keys('30')
        driver.find_element_by_name('y').send_keys('30')
        driver.find_element_by_name('label').send_keys(u'\ue007')
            
        time.sleep(2)
        dragLabel = driver.find_element_by_xpath("//*[contains(@class,'dragLabelGroup')]")
        
        
        rect_elem = dragLabel.find_element_by_tag_name('rect')
        
        ActionChains(driver).move_to_element(rect_elem).perform()
        ActionChains(driver).click(rect_elem).perform()
        ActionChains(driver).move_by_offset(130,0).perform()
             
#         except Exception as e:
#             report.entry_csv('DataLabel Events', "ERROR: There is an issue with clicking or RollOver or RollOut of the Label",chartType , "FAIL")
        
    
    
    def rotate_slice(self,driver,chartType):
        try:
            time.sleep(3)
            if chartType == "pie2d" or chartType == "pie3d":
                g_elem = driver.find_elements_by_tag_name('g')
                for g in g_elem:
                    cnt =0
                    for el in g.find_elements_by_tag_name('path'):
                        if el.tag_name == "path":
                            driver.execute_script("arguments[0].scrollIntoView();", el)
                            ActionChains(driver).move_to_element(el).perform()
                            ActionChains(driver).click_and_hold().perform()
                            ActionChains(driver).move_by_offset(20,70).perform()
                            ActionChains(driver).release().perform()
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                            driver.execute_script("arguments[0].scrollIntoView();", el)
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                        break  
            
            elif chartType == "doughnut3d":
                parent_path = driver.find_elements_by_xpath("//*[contains(@class,'top-Side')]")
                for plot_class in parent_path:
                    for el in plot_class.find_elements_by_tag_name('path'):
                        if el.tag_name == "path":
                            driver.execute_script("arguments[0].scrollIntoView();", el)
                            ActionChains(driver).move_to_element(el).perform()
                            ActionChains(driver).click_and_hold().perform()
                            ActionChains(driver).move_by_offset(30, 30).perform()
                            ActionChains(driver).release().perform()
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                        
            else:
                parent_path = driver.find_elements_by_xpath("//*[contains(@class,'plots')]")
                for plot_class in parent_path:
                    for el in plot_class.find_elements_by_tag_name('path'):
                        if el.tag_name == "path":
                            driver.execute_script("arguments[0].scrollIntoView();", el)
                            ActionChains(driver).move_to_element(el).perform()
                            ActionChains(driver).click_and_hold().perform()
                            ActionChains(driver).move_by_offset(30, 30).perform()
                            ActionChains(driver).release().perform()
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                            ActionChains(driver).click(el).perform()
                            time.sleep(2)
                
        except Exception as e:
            report.entry_csv('DataLabel Events', "ERROR: There is an issue with Rotate and Slice",chartType , "FAIL")
            
            
            
    def doughnut_centerlabel(self,driver,chartType):
        try:
            parent_path = driver.find_elements_by_xpath("//*[contains(@class,'plots')]")
            for plot_class in parent_path:
                for el in plot_class.find_elements_by_tag_name('text'):
                    driver.execute_script("arguments[0].scrollIntoView();", el)
                    ActionChains(driver).move_to_element(el).perform()
                    ActionChains(driver).click(el).perform()
                    ActionChains(driver).move_by_offset(80, 30).perform()
                    
        except Exception as e:
            report.entry_csv('centerlabel event', "ERROR: There is an issue with clicking on Data Label",chartType , "FAIL")
            
           
     
    def zoomline(self,driver,chartType):
        try:
            time.sleep(3)
            chart_canvas = driver.find_element_by_xpath("//*[contains(@class,'-canvas')]")
            ActionChains(driver).move_to_element(chart_canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(50, 0).perform()
            ActionChains(driver).release().perform()
            
            buttons = driver.find_elements_by_xpath("//*[contains(@class,'-button')]")
            button_rect = driver.find_element_by_xpath("//*[contains(@class,'-button')]")
            
            cnt = 0
            
            for button in buttons:
                cnt+=1
                if cnt == 3:
                    button_rect = button.find_element_by_tag_name('rect')
            
            ActionChains(driver).click(button_rect).perform()
            
            ActionChains(driver).move_to_element(chart_canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(50, 0).perform()
            ActionChains(driver).release().perform()
            
            cnt = 0
            
            for button in buttons:
                cnt+=1
                if cnt == 2:
                    button_rect = button.find_element_by_tag_name('rect')
            
            ActionChains(driver).click(button_rect).perform()
            
        except Exception as e:
            print e
            report.entry_csv('gantt event', "ERROR: There is an issue with zoomline",chartType , "FAIL")
    
    
    
    def maps(self,driver,chartType):
        try:  
            #click, roll over, roll out for countries
            cnt = 0
            manager_plots = driver.find_elements_by_xpath("//*[contains(@class,'manager-plot')]")
            parent_plot = driver.find_element_by_xpath("//*[contains(@class,'manager-plot')]")
            
            for plot in manager_plots:
                cnt+=1
                if cnt == 2:
                    parent_plot = plot
            paths = parent_plot.find_elements_by_tag_name('path') 
            
            cnt=0
            
            for path in paths:
                cnt+=1
                if cnt == 5:
                    ActionChains(driver).move_to_element(path).perform()
                    ActionChains(driver).click(path).perform()
                    ActionChains(driver).move_by_offset(100, 30).perform()
            
            #click, roll over, roll out for markers
            parent_plot = driver.find_element_by_xpath("//*[contains(@class,'markers')]")
            marker = parent_plot.find_element_by_tag_name('ellipse')
            
            ActionChains(driver).move_to_element(marker).perform()
            ActionChains(driver).click(marker).perform()
            ActionChains(driver).move_by_offset(100, 30).perform()
            
            #click, roll over, roll out for markers
            parent_plot_con = driver.find_element_by_xpath("//*[contains(@class,'connectors')]")
            connectors = parent_plot_con.find_elements_by_tag_name('path')
            
            for connector in connectors:
                ActionChains(driver).move_to_element(connector).perform()
                ActionChains(driver).click(connector).perform()
                ActionChains(driver).move_by_offset(100, -30).perform()
            
        except Exception as e:
            print e
            report.entry_csv('gantt event', "ERROR: There is an issue with map",chartType , "FAIL")     
            
            
            
    def annotations(self,driver,chartType):
        import pdb;
        pdb.set_trace()
        annotation_parent = driver.find_element_by_xpath("//*[contains(@class,'Callout')]")
        anno_elems = annotation_parent.find_elements_by_xpath(".//*")
        
        for elem in anno_elems:
            ActionChains(driver).move_to_element(elem).perform()
            ActionChains(driver).click(elem).perform()
            ActionChains(driver).move_by_offset(100, -30).perform()
    
    
    
    def dispose_click(self,driver,chartType):
        dispose_btn = driver.find_element_by_id('btn_dispose')
        driver.execute_script("arguments[0].scrollIntoView();", dispose_btn)
        dispose_btn.click()
        
        
        
    def chart_actions(self,driver,chartType):

        chart_svg = driver.find_element_by_tag_name('svg')
        ActionChains(driver).move_to_element(chart_svg).perform()
        ActionChains(driver).click().perform()
        ActionChains(driver).move_by_offset(10, 0).perform()
        ActionChains(driver).click().perform()
        ActionChains(driver).move_by_offset(10, 0).perform()
        ActionChains(driver).click().perform()
        ActionChains(driver).move_by_offset(10, 0).perform()
        ActionChains(driver).click().perform()
        ActionChains(driver).move_by_offset(550, 0).perform()
        
        
        
    def multiple_chart_actions(self,driver,chartType):                
        chart1 = driver.find_element_by_xpath("//div[@id='chart-container']/span")   
        chart2 = driver.find_element_by_xpath("//div[@id='chart-container1']/span")
        for interact in range(0, 2):     
            ActionChains(driver).move_to_element(chart1).perform()
            ActionChains(driver).move_to_element(chart2).perform()
            ActionChains(driver).move_by_offset(500, 0).perform()


            
    def gantt_category_rollover_rollout_click(self,driver,chartType):
        try:
            parent_path = driver.find_element_by_xpath("//*[contains(@class,'gantt-label-back-container')]")
            rects = parent_path.find_elements_by_tag_name('rect')
            for category in rects:
                driver.execute_script("arguments[0].scrollIntoView();", category)
                ActionChains(driver).move_to_element(category).perform()
                ActionChains(driver).click(category).perform()
                ActionChains(driver).move_by_offset(-80, -30).perform()
        
        except Exception as e:
            report.entry_csv('GanttChart event', "ERROR: There is an issue with clicking on GanttChart Category",chartType , "FAIL")
        
            
            
    def gantt_milestone_rollover_rollout_click(self,driver,chartType):
        try:
#             scrollContainer = driver.find_element_by_xpath("//*[contains(@class,'scrollContainer')]")
#             driver.execute_script("arguments[0].scrollIntoView();", scrollContainer)
#             scrollbar = driver.find_element_by_xpath("//*[contains(@class,'scrollContainer')]")
#             rects_in_scroll = scrollContainer.find_elements_by_tag_name('rect')
#             cnt=0
#             for rect in rects_in_scroll:
#                 cnt += 1
#                 if cnt==2:
#                     scrollbar = rect
#             driver.execute_script("arguments[0].scrollIntoView();", scrollbar)
#             ActionChains(driver).move_to_element(scrollbar).perform()
#             ActionChains(driver).click_and_hold().perform()
#             ActionChains(driver).move_by_offset(220, 0).perform()
#             ActionChains(driver).release().perform()
                            
            
            parent_path = driver.find_element_by_xpath("//*[contains(@class,'milestone')]")
            milestone = parent_path.find_element_by_tag_name('path')
            
            #driver.execute_script("arguments[0].scrollIntoView();", milestone)
            ActionChains(driver).move_to_element(milestone).perform()
            ActionChains(driver).click(milestone).perform()
            ActionChains(driver).move_by_offset(1, 0).perform()
            ActionChains(driver).click(milestone).perform()
            ActionChains(driver).move_by_offset(70, 0).perform()
            ActionChains(driver).move_by_offset(-70, 0).perform()
            ActionChains(driver).move_by_offset(-20, 0).perform()
          
        except Exception as e:
            report.entry_csv('GanttChart event', "ERROR: There is an issue with clicking on GanttChart Milestone",chartType , "FAIL")
            print e
    
    
    
    def gantt_process_rollover_rollout_click(self,driver,chartType):
        try:
            time.sleep(3)
            cnt=0
            back_container_group = driver.find_elements_by_xpath("//*[contains(@class,'gantt-label-back-container')]")
            process_group=driver.find_elements_by_xpath("//*[contains(@class,'gantt-label-back-container')]")
            #first_process = process_group.find_elements_by_tag_name('rect')
            
            for container_elem in back_container_group:
                if cnt == 1:
                    process_group = container_elem.find_elements_by_tag_name('rect')
                cnt=1
            
            for rect in process_group:
                driver.execute_script("arguments[0].scrollIntoView();", rect)
                ActionChains(driver).move_to_element(rect).perform()
                ActionChains(driver).click(rect).perform()
                ActionChains(driver).move_by_offset(80, 30).perform()
                break
            
        except Exception as e:
            print e
            report.entry_csv('gantt event', "ERROR: There is an issue with process",chartType , "FAIL")
            
            
            
    def gantt_connector_rollover_rollout_click(self,driver,chartType):
        try:
            time.sleep(3)
            cnt=0
            container_parent_elem = driver.find_element_by_xpath("//*[contains(@class,'connectors')]")
            all_container_elem =container_parent_elem.find_elements_by_tag_name('path')
            #first_process = process_group.find_elements_by_tag_name('rect')
            
            for path in all_container_elem:
                driver.execute_script("arguments[0].scrollIntoView();", path)
                ActionChains(driver).move_to_element(path).perform()
                ActionChains(driver).click(path).perform()
                ActionChains(driver).move_by_offset(0, 30).perform()
                ActionChains(driver).move_by_offset(40, 0).perform()
            
        except Exception as e:
            print e
            report.entry_csv('gantt event', "ERROR: There is an issue with connector",chartType , "FAIL")
    
          
          
    def scatterchart_selection_start_end_removed(self,driver,chartType):
        try:
            canvas = driver.find_element_by_xpath("//*[contains(@class,'canvas')]")
            ActionChains(driver).move_to_element(canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(150, 150).perform()
            ActionChains(driver).release().perform()
            
            selection_box = driver.find_element_by_xpath("//*[contains(@class,'selection-box')]")
            print selection_box
            path = selection_box.find_elements_by_tag_name('path')
            print "path = ",len(path)
            cnt=0
            for cross in path:
                cnt += 1
                if cnt==3:
                    ActionChains(driver).move_to_element(cross).perform()
                    ActionChains(driver).click(cross).perform()
                    ActionChains(driver).move_by_offset(2, 2).perform()
                
        except Exception as e:
            report.entry_csv('Select-Scatter Event', "ERROR: There is an issue with Selection Start, End or Removed on SelectScatter Chart",chartType , "FAIL")
            print e


    
    def logo_click_rollover_rollout(self,driver,chartType):
        try:
            logo = driver.find_element_by_xpath("//*[contains(@class,'logo')]")
            ActionChains(driver).move_to_element(logo).perform()
            ActionChains(driver).click(logo).perform()
            ActionChains(driver).move_by_offset(0, 1).perform()
            ActionChains(driver).click(logo).perform()
            ActionChains(driver).move_by_offset(60, 60).perform()
                
        except Exception as e:
            report.entry_csv('Generic Logo Events', "ERROR: There is an issue with Logo Click or RollOver or RollOut",chartType , "FAIL")
            print e

    
    
    def changechart(self,driver,chartType):
        try:
            controllers = driver.find_element_by_id('controllers')
            all_controls = controllers.find_elements_by_tag_name('*')
            for elem in all_controls:
                ActionChains(driver).click(elem).perform()
        except Exception as e:
            report.entry_csv('Generic Logo Events', "ERROR: There is an issue with Logo Click or RollOver or RollOut",chartType , "FAIL")
            print e
    
    
    
    def pinned(self,driver,chartType):
        try:
            chart_canvas = driver.find_element_by_xpath("//*[contains(@class,'-canvas')]")
            buttons = driver.find_elements_by_xpath("//*[contains(@class,'-button')]")
            button_rect = driver.find_element_by_xpath("//*[contains(@class,'-button')]")
            
            cnt = 0
            
            for button in buttons:
                cnt+=1
                if cnt == 1:
                    button_rect = button.find_element_by_tag_name('rect')
            
            ActionChains(driver).click(button_rect).perform()
            
            ActionChains(driver).move_to_element(chart_canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(50, 0).perform()
            ActionChains(driver).release().perform()
            
            
            ActionChains(driver).move_to_element(chart_canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(50, 0).perform()
            ActionChains(driver).release().perform()
            
        except Exception as e:
            report.entry_csv('Pinned', "ERROR: There is an issue with pinned",chartType , "FAIL")
            print e
            
            
            
    def export(self,driver,chartType):
        try:
            time.sleep(3)
            button = driver.find_element_by_xpath("//*[contains(@class,'-button')]")
            ActionChains(driver).move_to_element(button).perform()
            ActionChains(driver).move_by_offset(1, 0).perform()
            ActionChains(driver).move_by_offset(0, 1).perform()
            time.sleep(1)
            
            spans = driver.find_elements_by_tag_name('span')
            
            for span in spans:
                if span.text == "Export As PDF":
                    span.click()
                    break
                     
        except Exception as e:
            report.entry_csv('Pinned', "ERROR: There is an issue with export",chartType , "FAIL")
            print e
                    
                    
                    
    def scrollschart(self,driver,chartType):
        try:
            chart_canvas = driver.find_element_by_xpath("//*[contains(@class,'-canvas')]")
            ActionChains(driver).move_to_element(chart_canvas).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(-80, 0).perform()
            ActionChains(driver).release().perform()
            
        except Exception as e:
            report.entry_csv('Scroll Event', "ERROR: There is an issue with scrolling chart",chartType , "FAIL")
            print e

    
    
    def linkchartinvoke(self,driver,chartType):
        try:
            plot = driver.find_element_by_xpath("//*[contains(@class,'plot-group')]")
            first_plot = plot.find_element_by_tag_name('rect')
            first_plot.click()
    
        except Exception as e:
            report.entry_csv('LinkedChart Event', "ERROR: There is an issue with clicking plot",chartType , "FAIL")
            print e
    
    
    
    def clearchart(self,driver,chartType):
        try:
            time.sleep(4)
            if chartType == "realtimearea_real" or chartType == "realtimecolumn_real" or chartType == "realtimeline_real" or chartType == "realtimelinedy_real" or chartType == "realtimestackedarea_real":
                driver.execute_script("fusioncharts.clearChart()")
                time.sleep(1)
    
        except Exception as e:
            report.entry_csv('Clear Chart Event', "ERROR: There is an issue with clearing chart",chartType , "FAIL")
            print e   



    def crosslinehover(self,driver,chartType):
        try:
            plot = driver.find_elements_by_xpath("//*[contains(@class,'plot-group')]")
        
            for plot_this in plot:
                all_plots = plot_this.find_elements_by_xpath('.//*')
                for this_plot in all_plots:
                    ActionChains(driver).move_to_element(this_plot).perform()
    
        except Exception as e:
            report.entry_csv('Crossline Event', "ERROR: There is an issue with hovering on plot",chartType , "FAIL")
            print e   
            
            
            
    def printdialogclose(self,driver,chartType):
        try:
            ActionChains(driver).send_keys(Keys.COMMAND, '.').perform()
    
        except Exception as e:
            report.entry_csv('Crossline Event', "ERROR: There is an issue with hovering on plot",chartType , "FAIL")
            print e 


            
    def legend_pointer_drag_start_stop(self,driver,chartType):
        try:
            legend = driver.find_element_by_xpath("//*[contains(@class, 'slider')]")
            legend_circle = legend.find_element_by_tag_name('circle')
            ActionChains(driver).move_to_element(legend_circle).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(220, 0).perform()
            ActionChains(driver).release().perform()
            
        except Exception as e:
            report.entry_csv('Generic Legend Events', "ERROR: There is an issue with Legend Pointer Drag Start Stop Update",chartType , "FAIL")
            print e
            
            
            
    def legend_item_click_rollover_rollout(self,driver,chartType):
        try:
            legend = driver.find_element_by_xpath("//*[contains(@class, 'item')]")
            legend_item = legend.find_element_by_tag_name('rect')
            ActionChains(driver).move_to_element(legend_item).perform()
            ActionChains(driver).click(legend_item).perform()
            ActionChains(driver).move_by_offset(-10,-10).context_click().perform()

                
        except Exception as e:
            report.entry_csv('Generic Legend Item Events', "ERROR: There is an issue with Legend Click or RollOver or RollOut",chartType , "FAIL")
            print e
            
            
            
    def link_clicked(self,driver,chartType):
        try:
            dataplot = driver.find_element_by_xpath("//*[contains(@class, 'plot-group')]")
            plot = dataplot.find_element_by_tag_name('rect')
            ActionChains(driver).move_to_element(plot).perform()
            ActionChains(driver).click(plot).perform()
            ActionChains(driver).move_by_offset(20, 20).perform()
                
        except Exception as e:
            report.entry_csv('Generic Link Click Events', "ERROR: There is an issue with Link Click",chartType , "FAIL")
            print e        
            
            
            
    def linked_item_open_back(self,driver,chartType): 
        try:
            dataplot = driver.find_element_by_xpath("//*[contains(@class, 'plot-group')]")
            plot = dataplot.find_element_by_tag_name('rect')
            ActionChains(driver).move_to_element(plot).perform()
            ActionChains(driver).click(plot).perform()
            time.sleep(2)
            
            spans = driver.find_elements_by_tag_name('span')
            for span in spans:
                if span.text== 'Back':
                    ActionChains(driver).move_to_element(span).perform()
                    ActionChains(driver).click(span).perform()
        except Exception as e:
            report.entry_csv('Generic Link Click Events', "ERROR: There is an issue with Link Click",chartType , "FAIL")
            print e
     
     
     
    def dataplot_click_rollover_rollover(self,driver,chartType):
        try:
            dataplot = driver.find_element_by_xpath("//*[contains(@class, 'plot-group')]")
            plot = dataplot.find_element_by_tag_name('rect')
            ActionChains(driver).move_to_element(plot).perform()
            ActionChains(driver).click(plot).perform()
            ActionChains(driver).move_by_offset(30, 0).perform()
                
        except Exception as e:
            report.entry_csv('Generic Dataplot Events', "ERROR: There is an issue with Dataplot Click or Rollover or Rollout",chartType , "FAIL")
            print e  
            
    def linedataplot_first_click_rollover_rollover(self,driver,chartType):
        try:
            cnt = 0
            allgroup = driver.find_elements_by_xpath("//*[contains(@class, 'plot-group')]")
            for dataplot in allgroup:
                time.sleep(1)
                cnt=0
                plots = dataplot.find_elements_by_xpath(".//*")
                for plot in plots:
                    cnt+=1
                    if cnt==1:
                        ActionChains(driver).move_to_element(plot).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, 2).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).click(plot).perform()
                        ActionChains(driver).move_by_offset(0, 20).perform()
                        ActionChains(driver).move_by_offset(0, -40).perform()
                        time.sleep(1)
#                         plot.click()
#                         break
                
        except Exception as e:
            report.entry_csv('Generic Dataplot Events', "ERROR: There is an issue with Dataplot Click or Rollover or Rollout",chartType , "FAIL")
            print e  
            
    def linedataplot_second_click_rollover_rollover(self,driver,chartType):
        try:
            cnt = 0
            allgroup = driver.find_elements_by_xpath("//*[contains(@class, 'plot-group')]")
            for dataplot in allgroup:
                time.sleep(1)
                cnt=0
                plots = dataplot.find_elements_by_xpath(".//*")
                for plot in plots:
                    cnt+=1
                    if cnt==2:
                        ActionChains(driver).move_to_element(plot).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, 2).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).move_by_offset(0, -1).perform()
                        time.sleep(1)
                        ActionChains(driver).click(plot).perform()
                        ActionChains(driver).move_by_offset(0, 20).perform()
                        ActionChains(driver).move_by_offset(0, -40).perform()
                        time.sleep(1)
#                         plot.click()
#                         break
                
        except Exception as e:
            report.entry_csv('Generic Dataplot Events', "ERROR: There is an issue with Dataplot Click or Rollover or Rollout",chartType , "FAIL")
            print e
            
            
            
    def chorddiagram_dataplot_link_click_rollover_rollout(self,driver,chartType):
        try:
            links = driver.find_elements_by_xpath("//*[contains(@class,'link-container')]/*")     
            for link in links:
                ActionChains(driver).move_to_element(link).perform()
                ActionChains(driver).click(link).perform()
                ActionChains(driver).move_by_offset(500, 0).perform() 
                            
            nodes = driver.find_elements_by_xpath("//*[contains(@class,'node-container')]/*")     
            for node in nodes:
                ActionChains(driver).move_to_element(node).perform()
                ActionChains(driver).click(node).perform()
                ActionChains(driver).move_by_offset(500, 0).perform()
                time.sleep(1)
                ActionChains(driver).click(node).perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(node).perform()
                                                
        except Exception as e:
            report.entry_csv('Generic Dataplot Events', "ERROR: There is an issue with Dataplot Click or Rollover or Rollout",chartType , "FAIL")
            print e          
     
     
            
    def label_added_dragged(self,driver,chartType):
        try:
            
            
            g_elements = driver.find_elements_by_tag_name('g')
            
            for g_elem in g_elements:
                if "button" in g_elem.get_attribute('class'):
                    ActionChains(driver).move_to_element(g_elem).perform()
                    ActionChains(driver).move_by_offset(0,-1).perform() 
            
            span_elements = driver.find_elements_by_tag_name('span')
            for span in span_elements:
                if span.text == "Add Label":
                    span.click()
                    break    
            driver.find_element_by_name('label').send_keys('Test Label')
            driver.find_element_by_name('x').send_keys('30')
            driver.find_element_by_name('y').send_keys('30')
            driver.find_element_by_name('label').send_keys(u'\ue007')
            
            
            dragLabel = driver.find_element_by_xpath("//*[contains(@class,'dragLabelGroup')]")
            label_text = dragLabel.find_element_by_tag_name('rect')
            ActionChains(driver).move_to_element(label_text).perform()
            ActionChains(driver).click_and_hold().perform()
            ActionChains(driver).move_by_offset(220, 0).perform()
            
            ActionChains(driver).release().perform()
            ActionChains(driver).click_and_hold().perform()
            
            ActionChains(driver).move_by_offset(-15, 0).perform()
            ActionChains(driver).release().perform()
            
            
        except Exception as e:
            report.entry_csv('DataLabel Events', "ERROR: There is an issue with Dragging Label in dragnode chart",chartType , "FAIL")           
     
     
              
    def drillup_drilldown(self,driver,chartType):
        try:
            textTags = driver.find_elements_by_tag_name('text')
            for span in textTags:
                if span.text== 'Samsung':
                    ActionChains(driver).move_to_element(span).perform()
                    ActionChains(driver).click(span).perform()
                    break
                         
            drillup = driver.find_element_by_xpath("//*[contains(@class,'labelfloat')]")
            label_text = drillup.find_elements_by_tag_name('text')
            for label in label_text:
                if label.text== 'Samsung':
                    driver.execute_script("arguments[0].scrollIntoView();", label)
                    ActionChains(driver).move_to_element(label).perform()
                    ActionChains(driver).click(label).perform()
                    break
       
        except Exception as e:
            report.entry_csv('DataLabel Events', "ERROR: There is an issue with Drilling up or down in Treemap",chartType , "FAIL")           
                    
    
    
                               
def loaded_url_chartdata():
    return "https://static.fusioncharts.com/fiddle/froalacharts/getSampleJSON.php"
                
                    
from Util import chart as chart
import time

from Events import pomFile as pom

from Events import rendered
from Events import ready

from Events import dataplotDragStart
from Events import dataplotDragEnd
from Events import dataLoadRequested
from Events import dataLoadError
from Events import dataLoadRequestCompleted
from Events import beforeDataUpdate
from Events import dataUpdated
from Events import dataLoaded
from Events import beforeDataLoad
from Events import dataLoadRequestCancelled
from Events import dataUpdateCancelled
from Events import dataInvalid
from Events import beforeInitialize
from Events import beforeRender
from Events import renderComplete
from Events import loaded
from Events import initialized
from Events import nodatatodisplay
from Events import backgroundLoaded
from Events import backgroundLoadError
from Events import dataRestored
from Events import dataLabelClick
from Events import dataLabelRollOver
from Events import dataLabelRollOut
from Events import beforeDataSubmit
from Events import dataSubmitError
from Events import dataSubmitted
from Events import dataSubmitCancelled
from Events import nodeAdded
from Events import nodeUpdated
from Events import nodeDeleted
from Events import connectorAdded
from Events import connectorUpdated
from Events import connectorDeleted
from Events import centerLabelClick
from Events import centerLabelRollOut
from Events import centerLabelRollover
from Events import rotationEnd
from Events import rotationStart
from Events import slicingEnd
from Events import slicingStart
from Events import labelAdded
from Events import labelDeleted
from Events import labelClick
from Events import labelRollOver
from Events import labelRollOut
from Events import processClick
from Events import processRollOver
from Events import processRollOut
from Events import connectorClick
from Events import connectorRollOver
from Events import connectorRollOut
from Events import zoomReset
from Events import zoomedOut
from Events import zoomedIn
from Events import zoomed
from Events import zoomModeChanged
from Events import entityRollOut
from Events import entityRollOver
from Events import entityClick
from Events import markerRollOver
from Events import markerRollOut
from Events import markerClick
from Events import connectorRollOverMap
from Events import connectorRollOutMap
from Events import connectorClickMap
from Events import annotationClick
from Events import annotationRollOver
from Events import annotationRollOut
from Events import beforeDispose
from Events import disposed
from Events import disposeCancelled
from Events import beforeResize
from Events import resizeCancelled
from Events import resized
from Events import chartClick
from Events import chartRollOver
from Events import chartRollOut
from Events import chartMouseMove
from Events import categoryClick
from Events import categoryRollOver
from Events import categoryRollOut
from Events import milestoneClick
from Events import milestoneRollOver
from Events import milestoneRollOut
from Events import selectionStart
from Events import selectionEnd
from Events import selectionRemoved
from Events import logoClick
from Events import logoRollOver
from Events import logoRollOut
from Events import logoLoaded
from Events import logoLoadError
from Events import chartTypeChanged
from Events import chartUpdated
from Events import alertComplete
from Events import realTimeUpdateComplete
from Events import realTimeUpdateError
from Events import pinned
from Events import beforeExport
from Events import exported
from Events import exportCancelled
from Events import dataLoadCancelled
from Events import scrollStart
from Events import scrollEnd
from Events import onScroll
from Events import beforedraw
from Events import drawComplete
from Events import drawcancelled
from Events import linkedChartInvoked
from Events import chartCleared
from Events import onChangeCrossLine
from Events import beforePrint
from Events import printComplete
from Events import printCancelled
from Events import chartTypeInvalid
from Events import legendPointerDragStart
from Events import legendPointerDragStop
from Events import legendRangeUpdated
from Events import legendItemClicked
from Events import legendItemRollover
from Events import legendItemRollout
from Events import linkClicked
from Events import beforeLinkedItemOpen
from Events import linkedItemOpened
from Events import beforeLinkedItemClose
from Events import linkedItemClosed
from Events import overlayButtonClick
from Events import dataplotRollOver
from Events import dataplotRollOut
from Events import dataplotClick
from Events import containerNotFound
from Events import labelDragStart
from Events import labelDragEnd
from Events import beforeDrillUp
from Events import beforeDrillDown
from Events import drillDown
from Events import drillUp
from Events import drillDownCancelled
from Events import drillUpCancelled
from Events import animationInvoked
from Events import centerLabelChanged
from Events import dataPlotClickLine
from Events import dataPlotRollOverLine
from Events import dataplotRollOutLine
from Events import multipleInstancesChartRollOver
from Events import multipleInstancesChartRollOut
from Events import dataPlotRollOverChordDiagram
from Events import dataPlotRollOutChordDiagram
from Events import dataPlotClickChordDiagram
from Events import linkRollOverChordDiagram
from Events import linkRollOutChordDiagram
from Events import linkClickChordDiagram
import Main


class CallEventsClass(Main.MainClass):
    
    def __init__(self):
        mainObj = Main.MainClass()
        self.driver = mainObj.driver
        self.all_charts = [ "scatter", "pie", "bubble", "doughnut", "funnel", "sankey", "chord", "heatmap", "combination", "bar",
                           "column","radar","area","angulargauge","pyramid","line",
                            "stackedbar","stackedcolumn","stackedarea"]

        self.dataload_charts = ["pie_URL"]
        self.dataloaderror_charts = ["pie_URLerror"]
        self.dataloadrequestcancelled_charts = ["pie_dlreq_cancelled"]
        self.dataupdatecancelled_charts = ["pie_du_cancelled"]
        self.datainvalid_charts = ["pie_invalid"]
        self.nodata_charts = ["pie_nodata"]
        self.datalabelinxaxis_charts = [ "bubble"]
        self.backgroundLoad_charts = [ "bubble",  "pie"]
        self.bgImageError_charts =  ["bubble_bgImageError"]
        self.pieanddoughnut_charts = ["doughnut","pie"]
        self.annotation_charts = ["stackedbar_annot"]
        self.dispose_charts = ["column_dispose"]
        self.disposecancelled_charts = ["column_dispose_cancel"]
        self.mousemove_charts = ["pie_mousemove"]
        self.heatmap_charts = ["heatmap"]
        self.legend_charts =["column"]
        self.linecharts = ["combination"]
        self.areacharts= ["area","stackedarea"]
        self.chord_chart= ["chord_links_nodes_events"]
    
        self.pom = pom.PageObjectModel()
    
    
    def run_event(self,chartType):
        chart.writefile(chartType)
        self.driver.refresh()
        
    def run_event2(self,chartType):
        chart.writefile2(chartType)
        self.driver.refresh()
    
    
    def exec_rendered(self):

        for chartType in self.all_charts:
            self.run_event(chartType)
            rendered.f_rendered(self.driver,chartType)
            ready.f_ready(self.driver,chartType)
            beforeInitialize.f_beforeInitialize(self.driver,chartType) 
            beforeRender.f_beforeRender(self.driver,chartType)
            renderComplete.f_renderComplete(self.driver,chartType)
            loaded.f_loaded(self.driver,chartType)
            initialized.f_initialized(self.driver,chartType)
        
    def exec_dragablecharts(self):
        #Executing drag start and drag end events for drag-able charts
        for chartType in self.dragable_charts:
            self.run_event(chartType)
            self.pom.drag_any_plot(self.driver,chartType)
            
            dataplotDragStart.f_dataplotdragstart(self.driver, chartType)
            dataplotDragEnd.f_dataplotdragend(self.driver, chartType)
            
    
    def exec_dataload_valid(self):
        for chartType in self.dataload_charts:
            self.run_event(chartType)
            
            dataLoadRequested.f_dataloadrequested(self.driver, chartType)
            dataLoadRequestCompleted.f_dataloadrequestcompleted(self.driver, chartType)
            beforeDataUpdate.f_beforedataupdate(self.driver, chartType)
            dataUpdated.f_dataupdated(self.driver, chartType)
            dataLoaded.f_dataloaded(self.driver, chartType)
            beforeDataLoad.f_beforedataload(self.driver, chartType)
            time.sleep(3)
    
    
    def exec_dataLoadError(self):
        for chartType in self.dataloaderror_charts:

            self.run_event(chartType)
            
            dataLoadError.f_dataloaderror(self.driver, chartType)   
    
    
    def exec_dataloadrequestcancelled(self):
        for chartType in self.dataloadrequestcancelled_charts:
            self.run_event(chartType)
            
            dataLoadRequestCancelled.f_dataloadrequestcancelled(self.driver, chartType)
    
    def exec_dataupdatecancelled(self):
        for chartType in self.dataupdatecancelled_charts:
            self.run_event(chartType)
            
            dataUpdateCancelled.f_dataupdatecancelled(self.driver, chartType)
            
    
    def exec_datainvalid(self):
        for chartType in self.datainvalid_charts:
            self.run_event(chartType)
            
            dataInvalid.f_datainvalid(self.driver,chartType)
            
    
    def exec_nodatatodisplay(self):
        for chartType in self.nodata_charts:
            self.run_event(chartType)
            nodatatodisplay.f_nodatatodisplay(self.driver,chartType)
    
    def exec_backgroundloaded(self):
        for chartType in self.backgroundLoad_charts:
            self.run_event(chartType)
            
            backgroundLoaded.f_backgroundloaded(self.driver,chartType)
    
    
    def exec_backgroundloaderror(self):
        for chartType in self.bgImageError_charts:
            self.run_event(chartType)
            
            backgroundLoadError.f_backgroundloaderror(self.driver,chartType)
    
    
    def exec_datarestored(self):
        for chartType in self.dragable_charts:
            self.run_event(chartType)
            
            self.pom.drag_any_plot(self.driver,chartType)
            self.pom.click_restore(self.driver,chartType)
            dataRestored.f_datarestored(self.driver,chartType)
            
    def exec_datalabelclick_rollover_rollout(self):
        for chartType in self.datalabelinxaxis_charts:
            self.run_event(chartType)
            
            self.pom.datalabel_click_rollover_rollout(self.driver,chartType)
            dataLabelRollOver.f_datalabelrollover(self.driver,chartType)
            dataLabelRollOut.f_datalabelrollout(self.driver,chartType)
            dataLabelClick.f_datalabelclick(self.driver,chartType)
    
    
    def exec_editable(self):
        for chartType in self.editable_charts:
            self.run_event(chartType)
            self.pom.click_submit(self.driver,chartType)
            
            beforeDataSubmit.f_beforedatasubmit(self.driver, chartType)
            
    def exec_datasubmiterror(self):
        for chartType in self.dataSubmitError_charts:
            self.run_event(chartType)
            self.pom.click_save(self.driver,chartType)
            
            dataSubmitError.f_datasubmiterror(self.driver, chartType)
    
    
    def exec_datasubmitted(self):
        for chartType in self.dataSubmitted_charts:
            self.run_event(chartType)
            self.pom.click_save(self.driver,chartType)
            
            dataSubmitted.f_datasubmitted(self.driver, chartType)
            
    def exec_datasubmitcancelled(self):
        for chartType in self.dataSubmitCancelled_charts:
            self.run_event(chartType)
            self.pom.click_submit(self.driver,chartType)
            
            dataSubmitCancelled.f_datasubmitcancelled(self.driver, chartType)
            
    def exec_dragnodeevents(self):
        for chartType in self.editable_charts:
            if chartType == "dragnode":
                self.run_event(chartType)
                self.pom.add_update_delete_node(self.driver,chartType)
                 
                nodeAdded.f_nodeadded(self.driver, chartType)
                nodeUpdated.f_nodeupdated(self.driver, chartType)
                nodeDeleted.f_nodedeleted(self.driver, chartType)
                
                self.run_event(chartType)
                self.pom.add_connector(self.driver,chartType)
                
                connectorAdded.f_connectoradded(self.driver, chartType)
                
                self.run_event(chartType)
                self.pom.update_delete_connector(self.driver,chartType)
                
                connectorUpdated.f_connectorupdated(self.driver, chartType)
                connectorDeleted.f_connectordeleted(self.driver, chartType)
                
                
    def exec_pieanddoughnutevents(self):
        for chartType in self.pieanddoughnut_charts:
            self.run_event(chartType)
            self.pom.rotate_slice(self.driver,chartType)
            if chartType == "doughnut":
                self.pom.doughnut_centerlabel(self.driver,chartType)
                
                centerLabelClick.f_centerlabelclick(self.driver, chartType)
                centerLabelRollOut.f_centerlabelrollout(self.driver, chartType)
                centerLabelRollover.f_centerlabelrollover(self.driver, chartType)
                centerLabelChanged.f_centerlabelchanged(self.driver, chartType)
            rotationEnd.f_rotationend(self.driver, chartType)
            rotationStart.f_rotationstart(self.driver, chartType)
            slicingEnd.f_slicingend(self.driver, chartType)
            slicingStart.f_slicingstart(self.driver, chartType)
            
            
    
    def exec_dragnodelabelevents(self):
        for chartType in self.editable_charts:
            if chartType == "dragnode":
                self.run_event(chartType)
                self.pom.label_added_deleted(self.driver,chartType)
                
                labelAdded.f_labeladded(self.driver,chartType)
                labelDeleted.f_labeldeleted(self.driver,chartType)
    
                
    def exec_dragnodelabelclick_rollover_rollout(self):
        for chartType in self.editable_charts:
            if chartType == "dragnode":
                self.run_event(chartType)
                self.pom.label_click_rollover_rollout(self.driver,chartType)
                
                labelClick.f_labelclick(self.driver, chartType)
                labelRollOver.f_labelrollover(self.driver, chartType)
                labelRollOut.f_labelrollout(self.driver, chartType)
                
                 
    def exec_selection_start_end_removed(self):
        for chartType in self.editable_charts:
            if chartType == "selectscatter":
                self.run_event(chartType)
                self.pom.scatterchart_selection_start_end_removed(self.driver,chartType)
            
                selectionStart.f_selectionstart(self.driver, chartType)
                selectionEnd.f_selectionend(self.driver, chartType)
                selectionRemoved.f_selectionremoved(self.driver, chartType)
                
    def exec_logo_click_rollover_rollout(self):
        for chartType in self.logo_charts:
            if chartType == "column2d_logo_error":
                self.run_event(chartType)
                logoLoadError.f_logoloaderror(self.driver, chartType)
                
            else:
                self.run_event(chartType)
                self.pom.logo_click_rollover_rollout(self.driver,chartType)
                logoClick.f_logoclick(self.driver, chartType)
                logoRollOver.f_logorollover(self.driver, chartType)
                logoRollOut.f_logorollout(self.driver, chartType)
                logoLoaded.f_logoloaded(self.driver, chartType)
                
                
    
    
    def exec_gantt(self):
        for chartType in self.gantt_charts:
            self.run_event(chartType)
            
            self.pom.gantt_process_rollover_rollout_click(self.driver,chartType)
            processClick.f_processclick(self.driver, chartType)
            processRollOver.f_processrollover(self.driver, chartType)
            processRollOut.f_processrollout(self.driver, chartType)
            
            self.pom.gantt_connector_rollover_rollout_click(self.driver,chartType)
            connectorClick.f_connectorclick(self.driver, chartType)
            connectorRollOver.f_connectorrollover(self.driver, chartType)
            connectorRollOut.f_connectorrollout(self.driver, chartType)
            
            self.pom.gantt_category_rollover_rollout_click(self.driver,chartType)
            categoryClick.f_categoryclick(self.driver, chartType)
            categoryRollOver.f_categoryrollover(self.driver, chartType)
            categoryRollOut.f_categoryrollout(self.driver, chartType)
            
            self.pom.gantt_milestone_rollover_rollout_click(self.driver,chartType)
            milestoneClick.f_milestoneclick(self.driver, chartType)
            milestoneRollOver.f_milestonerollover(self.driver, chartType)
            milestoneRollOut.f_milestonerollout(self.driver, chartType)
            
    
    def exec_zoom(self):
        for chartType in self.zoom_charts:
            self.run_event(chartType)
            
            self.pom.zoomline(self.driver,chartType)
            zoomReset.f_zoomreset(self.driver, chartType)
            zoomedOut.f_zoomedout(self.driver, chartType)
            zoomedIn.f_zoomedin(self.driver, chartType)
            zoomed.f_zoomed(self.driver, chartType)
            zoomModeChanged.f_zoommodechanged(self.driver, chartType)
            
            self.run_event(chartType)
            
            self.pom.pinned(self.driver,chartType)
            pinned.f_pinned(self.driver, chartType)
            
            
    def exec_map(self):
        for chartType in self.map_charts:
            self.run_event(chartType)
            
            self.pom.maps(self.driver,chartType)
            entityRollOut.f_entityrollout(self.driver, chartType)
            entityRollOver.f_entityrollover(self.driver, chartType)
            entityClick.f_entityclick(self.driver, chartType)
            markerRollOver.f_markerrollover(self.driver, chartType)
            markerRollOut.f_markerrollout(self.driver, chartType)
            markerClick.f_markerclick(self.driver, chartType)
            connectorRollOverMap.f_connectorrollover(self.driver, chartType)
            connectorRollOutMap.f_connectorrollout(self.driver, chartType)
            connectorClickMap.f_connectorclick(self.driver, chartType)
    
    
    
    def exec_annotations(self):
        for chartType in self.annotation_charts:
            self.run_event(chartType)


            
            self.pom.annotations(self.driver,chartType)  
            # annotationClick.f_annotationclick(self.driver, chartType)
            annotationRollOver.f_annotationrollover(self.driver, chartType)
            annotationRollOut.f_annotationrollout(self.driver, chartType)
    
    def exec_dispose(self):
        for chartType in self.dispose_charts:

            self.run_event(chartType)

            
            self.pom.dispose_click(self.driver,chartType)
            beforeDispose.f_beforedispose(self.driver, chartType)
            disposed.f_disposed(self.driver, chartType)
        
        for chartType in self.disposecancelled_charts:
            self.run_event(chartType)
             
            self.pom.dispose_click(self.driver,chartType)
            disposeCancelled.f_disposecancelled(self.driver, chartType) 
    
    
    
    def exec_resize(self):
        for chartType in self.resize_charts:
            self.run_event(chartType)
            
            beforeResize.f_beforeresize(self.driver, chartType)
            resized.f_resized(self.driver, chartType)
    
        for chartType in self.resizecancelled_charts:
            self.run_event(chartType)
            
            resizeCancelled.f_resizecancelled(self.driver, chartType)
        
    
    def exec_chartactions(self):
        time.sleep(2)
        for chartType in self.all_charts:

            self.run_event(chartType)
            
            self.pom.chart_actions(self.driver,chartType)
            chartClick.f_chartclick(self.driver, chartType)
            chartRollOver.f_chartrollover(self.driver, chartType)
            chartRollOut.f_chartrollout(self.driver, chartType)
            
        for chartType in self.mousemove_charts:
            self.run_event(chartType)
            
            self.pom.chart_actions(self.driver,chartType)
            chartMouseMove.f_chartmousemove(self.driver, chartType)
    
    
    
    def exec_changechart(self):
        for chartType in self.change_charts:
            self.run_event(chartType)
            
            self.pom.changechart(self.driver,chartType)
            chartTypeChanged.f_charttypechanged(self.driver, chartType)
            beforedraw.f_beforedraw(self.driver, chartType)
            drawComplete.f_drawcomplete(self.driver, chartType)
            
            
    def exec_chartupdate(self):
        for chartType in self.dragable_charts:
            self.run_event(chartType)
            
            self.pom.drag_any_plot(self.driver,chartType)
            chartUpdated.f_chartupdated(self.driver, chartType)
            
            
    def exec_realtime(self):
        for chartType in self.realtime_charts:
            self.run_event(chartType)
             
            time.sleep(14)
            alertComplete.f_alertcomplete(self.driver, chartType)
            realTimeUpdateComplete.f_realtimeupdatecomplete(self.driver, chartType)
            
            
        for chartType in self.realtimeerror_charts:
            self.run_event(chartType)
            
            time.sleep(3)
            realTimeUpdateError.f_realtimeupdateerror(self.driver, chartType)
    
    def exec_export(self):
        for chartType in self.all_charts:
            self.run_event(chartType)
            
            self.pom.export(self.driver,chartType)
            beforeExport.f_beforeexport(self.driver, chartType)
            exported.f_exported(self.driver, chartType)
            
        for chartType in self.exportcancelled_charts:
            self.run_event(chartType)
            
            self.pom.export(self.driver,chartType)
            exportCancelled.f_exportcancelled(self.driver, chartType)
            
    def exec_print(self):
        for chartType in self.print_charts:
            self.run_event(chartType)
            
            
            self.pom.printdialogclose(self.driver,chartType)
            beforePrint.f_beforeprint(self.driver, chartType)
            if self.pom.browser == "Firefox":
                printComplete.f_printcomplete(self.driver, chartType)
        
        for chartType in self.printcancelled_charts:
            self.run_event(chartType)   
            
            printCancelled.f_printcancelled(self.driver, chartType)
            
    def exec_dataloadcancelled(self):
        for chartType in self.dataloadcancelled_charts:
            self.run_event(chartType)
            
            dataLoadCancelled.f_dataloadcancelled(self.driver, chartType)
            
    
    
    def exec_scrollevents(self):
        for chartType in self.scroll_charts:
            self.run_event(chartType)    
            
            self.pom.scrollschart(self.driver,chartType)
            scrollStart.f_scrollstart(self.driver, chartType)
            scrollEnd.f_scrollend(self.driver, chartType)
            onScroll.f_onscroll(self.driver, chartType)
            
    
    def exec_drawcanc(self):
        for chartType in self.drawcancelled_charts:
            self.run_event(chartType)         
            
            drawcancelled.f_drawcancelled(self.driver, chartType)
            
    
    
    def exec_linkedchart(self):
        for chartType in self.linked_charts:
            self.run_event(chartType)
            
            self.pom.linkchartinvoke(self.driver,chartType)
            linkedChartInvoked.f_linkedchartinvoked(self.driver, chartType)
    
    def exec_clearchart(self):
        for chartType in self.clear_charts:
            self.run_event(chartType)
            
            time.sleep(7)
            self.pom.clearchart(self.driver,chartType)
            chartCleared.f_chartcleared(self.driver, chartType)
            
            
    def exec_crossline(self):
        for chartType in self.crossline_charts:
            self.run_event(chartType)
            
            self.pom.crosslinehover(self.driver,chartType)
            onChangeCrossLine.f_onchangecrossline(self.driver, chartType)
            
    
    def exec_invalid(self):
        for chartType in self.invalid_charts:
            self.run_event(chartType)       
            
            chartTypeInvalid.f_charttypeinvalid(self.driver, chartType)
            
            
            
    def exec_legendpointerdrag_start_stop_updated(self):
        for chartType in self.heatmap_charts:
            self.run_event(chartType)
            
            self.pom.legend_pointer_drag_start_stop(self.driver,chartType)
            legendPointerDragStart.f_legendpointerdragstart(self.driver, chartType)
            legendPointerDragStop.f_legendpointerdragstop(self.driver, chartType)
            legendRangeUpdated.f_legendrangeupdated(self.driver, chartType)
            
    def exec_legenditem_click_rollover_rollout(self):
        for chartType in self.legend_charts:
            self.run_event(chartType)
            
            self.pom.legend_item_click_rollover_rollout(self.driver,chartType)
            legendItemClicked.f_legenditemclicked(self.driver, chartType)
            legendItemRollover.f_legenditemrollover(self.driver, chartType)
            legendItemRollout.f_legenditemrollout(self.driver, chartType)
            
    def exec_linkclicked(self):
        for chartType in self.column2d_link_charts:
            self.run_event(chartType)
            
            self.pom.link_clicked(self.driver,chartType)
            linkClicked.f_linkclicked(self.driver, chartType)
                 
    def exec_beforelinked_item_open_back(self):        
        for chartType in self.column2d_linked_item_charts:   
            self.run_event(chartType)
            
            self.pom.linked_item_open_back(self.driver,chartType)
            beforeLinkedItemOpen.f_beforelinkeditemopen(self.driver, chartType)
            linkedItemOpened.f_linkeditemopened(self.driver, chartType)
            beforeLinkedItemClose.f_beforelinkeditemclose(self.driver, chartType)
            linkedItemClosed.f_linkeditemclosed(self.driver, chartType)
            overlayButtonClick.f_overlaybuttonclick(self.driver, chartType)
            
    def exec_dataplot_click_rollover_rollout(self):        
        for chartType in self.all_charts:  
            if chartType == "column2d": 
                self.run_event(chartType)
            
                self.pom.dataplot_click_rollover_rollover(self.driver,chartType)
                dataplotRollOver.f_dataplotrollover(self.driver,chartType)
                dataplotRollOut.f_dataplorollout(self.driver,chartType)
                dataplotClick.f_dataplotclick(self.driver,chartType)
                    
    def exec_container_not_found(self):
        for chartType in self.no_container_charts:
            self.run_event(chartType)         
            containerNotFound.f_containernotfound(self.driver,chartType)   
            
    def exec_labeldrag_start_end(self):       
        for chartType in self.editable_charts:
            if chartType == "dragnode":
                self.run_event(chartType) 
            
                self.pom.label_added_dragged(self.driver,chartType)
                labelDragStart.f_labeldragstart(self.driver,chartType)
                labelDragEnd.f_labeldragend(self.driver,chartType)
                
    def exec_beforedrillup_drilldown_beforedrilldown(self):
        for chartType in self.treemap:
            if chartType == "treemap":
                self.run_event(chartType) 
            
                self.pom.drillup_drilldown(self.driver,chartType)
                beforeDrillUp.f_beforedrillup(self.driver,chartType)
                beforeDrillDown.f_beforedrilldown(self.driver,chartType)
                drillDown.f_drilldown(self.driver,chartType)
                drillUp.f_drillup(self.driver,chartType)
            
    def exec_drilldowncancelled(self):
        for chartType in self.treemap:
            if chartType == "treemap_drilldowncancelled":
                self.run_event(chartType) 
                
                self.pom.drillup_drilldown(self.driver,chartType)
                drillDownCancelled.f_drilldowncancelled(self.driver,chartType)
                
    def exec_drillupcancelled(self):
        for chartType in self.treemap:
            if chartType == "treemap_drillupcancelled":
                self.run_event(chartType)
                 
                self.pom.drillup_drilldown(self.driver,chartType)
                drillUpCancelled.f_drillupcancelled(self.driver,chartType)
                
    def exec_animationInvoked(self):
        for chartType in self.treemap:
            if chartType == "treemap_animation":
                self.run_event(chartType)
                
                animationInvoked.f_animationinvoked(self.driver,chartType)  
                
    def exec_line_dataplot_click_rollover_rollout(self):        
        for chartType in self.linecharts:  
            self.run_event2(chartType)
        
            self.pom.linedataplot_first_click_rollover_rollover(self.driver,chartType)
            dataPlotRollOverLine.f_dataplotrolloverline(self.driver,chartType)
            dataplotRollOutLine.f_dataplorolloutline(self.driver,chartType)
            dataPlotClickLine.f_dataplotclickline(self.driver,chartType)
            
            self.pom.linedataplot_second_click_rollover_rollover(self.driver,chartType)
            dataPlotRollOverLine.f_dataplotrolloverline(self.driver,chartType)
            dataplotRollOutLine.f_dataplorolloutline(self.driver,chartType)
            dataPlotClickLine.f_dataplotclickline(self.driver,chartType)
            
    def exec_area_dataplot_click_rollover_rollout(self):        
        for chartType in self.areacharts:  
            self.run_event2(chartType)
        
            self.pom.linedataplot_first_click_rollover_rollover(self.driver,chartType)
            dataPlotRollOverLine.f_dataplotrolloverline(self.driver,chartType)
            dataplotRollOutLine.f_dataplorolloutline(self.driver,chartType)
            dataPlotClickLine.f_dataplotclickline(self.driver,chartType)
            
            self.pom.linedataplot_second_click_rollover_rollover(self.driver,chartType)
            dataPlotRollOverLine.f_dataplotrolloverline(self.driver,chartType)
            dataplotRollOutLine.f_dataplorolloutline(self.driver,chartType)
            dataPlotClickLine.f_dataplotclickline(self.driver,chartType)
            
    def exec_multiplechartinstances_actions(self):
        for chartType in self.multipleinstances_charts:   
            self.run_event(chartType)
            
            self.pom.multiple_chart_actions(self.driver,chartType)
            multipleInstancesChartRollOver.f_multipleinstanceschartrollover(self.driver, chartType)
            multipleInstancesChartRollOut.f_multipleinstanceschartrollout(self.driver, chartType)      

    def exec_chordDiagram(self):        
        for chartType in self.chord_chart:  
            self.run_event(chartType)
            
            self.pom.chorddiagram_dataplot_link_click_rollover_rollout(self.driver,chartType)
            dataPlotRollOverChordDiagram.f_dataplotrolloverchorddiagram(self.driver,chartType)
            dataPlotRollOutChordDiagram.f_dataplotrolloutchorddiagram(self.driver,chartType)
            dataPlotClickChordDiagram.f_dataplotclickchorddiagram(self.driver,chartType)
            
            linkRollOverChordDiagram.f_linkrolloverchorddiagram(self.driver,chartType)
            linkRollOutChordDiagram.f_linkrolloutchorddiagram(self.driver,chartType)
            linkClickChordDiagram.f_linkclickchorddiagram(self.driver,chartType)

 
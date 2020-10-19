import csv

browser =""
driver = None
    
def create_csv():
    with open('Event_report.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Browser','Event', 'Object Parameters','Chart','Status'])

def entry_csv(event, obj_parameters, chartType, status):
    with open('Event_report.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([browser,event,obj_parameters,chartType,status])
        
def jsError_exists(chartType):
        errBrowser = driver.execute_script("return window.jsError")
        if errBrowser != None:
            print "JS error in ",chartType
            jsErr = "JS error: " + errBrowser
            entry_csv('animationinvoked', jsErr, chartType, "FAIL")
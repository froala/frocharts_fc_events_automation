import csv
import os

def writefile(chart):
    html_content=""
    with open('../Util/chartdata.csv', 'r') as csvFile:
        try:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[0] == chart:
                    html_content=row[1]
                    html_file = open('../File/NewTestTry.html', 'w')
                    html_file.write(html_content)
                    html_file.close()
        except Exception as e:
            print "could not open csv: ",e
        finally:
            csvFile.close()

def writefile2(chart):
    html_content=""
    with open('../Util/chartdata2.csv', 'r') as csvFile:
        try:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[0] == chart:
                    html_content=row[1]
                    html_file = open('../File/NewTestTry.html', 'w')
                    html_file.write(html_content)
                    html_file.close()
        except Exception as e:
            print "could not open csv: ",e
        finally:
            csvFile.close()
                    
def url_to_hit():
    return "http://localhost:8080/frocharts_fc_events_automation/File/NewTestTry.html"
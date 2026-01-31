import requests
from bs4 import BeautifulSoup
import csv

def main():
    classdict = []
    finalsdict = []
    with open('classschedule.csv', newline='') as classschedule:
        spamreader = csv.DictReader(classschedule, delimiter=',')
        for row in spamreader:
            classdict.append(row)

    r = requests.get('https://www.unr.edu/admissions/records/academic-calendar/finals-schedule')
    soup = BeautifulSoup(r.text, 'html.parser')

    elements = soup.find_all(class_='footable')

    #UNCOMMENT THIS WHEN READY TO MAKE FULL SCHEDULE
    for element in elements:
        single_day = element.get_text(strip=False)
        generate_days_schedule(single_day, classdict, finalsdict)
    writefile(finalsdict)

def generate_days_schedule(single_day, classdict, finalsdict):
        lines = single_day.splitlines()
        for i, line in enumerate(lines):
            for classinfo in classdict:
                if classinfo['StartingTime'] in line:
                    if i+2 < len(lines) and classinfo['DayOfWeek'] in lines[i+1]:
                        finalsdict.append([classinfo['Class'],lines[0].strip(),lines[i+2].strip()])

def writefile(finalsdict):
    with open('finalsschedule.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Class', 'Day', 'Time'])
        writer.writerows(finalsdict)

if __name__ == '__main__':
    main()
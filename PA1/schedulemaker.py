import requests
from bs4 import BeautifulSoup
import csv

def main():
    classes = []
    finals = []
    with open('classschedule.csv', newline='') as classschedule:
        spamreader = csv.DictReader(classschedule, delimiter=',')
        for row in spamreader:
            classes.append(row)

    r = requests.get('https://www.unr.edu/admissions/records/academic-calendar/finals-schedule')
    soup = BeautifulSoup(r.text, 'html.parser')

    elements = soup.find_all(class_='footable')

    for element in elements:
        isolated_date = element.get_text(strip=False)
        find_matching_dates(isolated_date, classes, finals)
    writefile(finals)

def find_matching_dates(isolated_date, classes, finals):
        lines = isolated_date.splitlines()
        for i, line in enumerate(lines):
            for classinfo in classes:
                if classinfo['StartingTime'] in line:
                    if i+2 < len(lines) and classinfo['DayOfWeek'] in lines[i+1]:
                        finals.append([classinfo['Class'],lines[0].strip(),lines[i+2].strip()])

def writefile(finals):
    with open('finalsschedule.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Class', 'Day', 'Time'])
        writer.writerows(finals)

if __name__ == '__main__':
    main()
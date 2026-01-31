import requests
from bs4 import BeautifulSoup
import csv

def main():
    classdict = []  #reading to dict because finding values will be fast
    with open('classschedule.csv', newline='') as classschedule:
        spamreader = csv.DictReader(classschedule, delimiter=',')
        for row in spamreader:
            classdict.append(row)

    print(classdict)

    r = requests.get('https://www.unr.edu/admissions/records/academic-calendar/finals-schedule')
    soup = BeautifulSoup(r.text, 'html.parser')

    elements = soup.find_all(class_='footable')

    # for element in elements:
    single_day = elements[0].get_text(strip=False)
    generate_days_schedule(single_day, classdict)


def generate_days_schedule(single_day, classdict):
    lines = single_day.splitlines()
    for i, line in enumerate(lines):
        if line == '8:30 a.m.':
            if i+2 < len(lines) and lines[i+1] == 'Tuesday/Thursday (TR)':
                print(lines[i+2])

    return 0

if __name__ == '__main__':
    main()
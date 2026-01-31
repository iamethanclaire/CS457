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

    for element in elements:
        single_day = element.get_text(strip=False)
        generate_days_schedule(single_day)


def generate_days_schedule(single_day):

    print(single_day)
    return 0

if __name__ == '__main__':
    main()
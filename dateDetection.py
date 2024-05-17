import re

dateRegex = re.compile(r'''
    ([0-3][0-9])    # days from 1-31 or 01-31
    [/,._:-]        # separator
    ([0-1][0-9])    # months from 1-12 or 01-12
    [/,._:-]        # separator
    ([1-2][0-9]{3}) # year from 1000-2999
''', re.VERBOSE)

text = 'Was about 15.12,3000... but then I have got some 17:05/2024'

dates = dateRegex.findall(text)

days, months, years = [], [], []

validDates = []

for groups in dates:
    day, month, year = groups[0], groups[1], groups[2]

    days.append(day)
    months.append(month)
    years.append(year)

def showFormatedDates():
    for i in range(len(days)):
        print(f'{days[i]}/{months[i]}/{years[i]}')

showFormatedDates()
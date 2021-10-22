import csv
import urllib.request
def run():
    url = 'http://health-infobase.canada.ca/src/data/covidLive/covid19-download.csv'
    total = []

    prov = ["BC","AB","SAS","MA","ON","QB","NL","NB","NS","PEI","YK","NW","NUN"]
    d = {'prov': prov, 'cases' : []}

    # with open('covid19-download (3).csv') as c:
    #     csv_reader = csv.reader(c)

    #     for line in csv_reader:
    #         total.append(line[15])
    r = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in r.readlines()]
    cr = csv.reader(lines)
    for line in cr:
        total.append(line[15])

    total = total[-15:-1]
    total.pop(13)


    i=0
    for p in prov:
        d['cases'].append(int(total[i]))
        i+=1
        
    return d
a = run()
print(a)
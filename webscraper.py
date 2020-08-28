from bs4 import BeautifulSoup,Comment
import requests
import json
import jsons as j
import matplotlib.pyplot as plt
import operator
import numpy
import html

def web():
    
    def absolute_value(val):
        a  = numpy.round(val/100.*numpy.array(top10).sum(), 0)
        return int(a)
    def absolute_values(val):
        a  = numpy.round(val/100.*numpy.array(least10).sum(), 0)
        return int(a)
    list=[]

    response=requests.get("https://covidindia.org/").content

    soup = BeautifulSoup(response, 'html5lib')
    table=soup.findAll('table')[0].findAll('tr')
    header=table[0].find_all('th')
    head=[]
    for i in header:
        head.append(i.text)
    
    list.append(head)
    
    for rows in table[1:]:
        u=[]
        tds=rows.find_all('td')
        for i in tds:
            u.append(i.text)
        list.append(u)
    past=j.load()
    print(list)
    curr={x[0]:x[1:] for x in list[1:-1]}
    print(curr)
    j.save(curr)
    changed=False
    for states in curr:
        if states not in past:
            changed=True
            past[states]=['0','0','0','0']
    states=[x for x in curr.keys()]
    states=states[:-1]
    print(states)
    data_total=[int(curr[x][0]) for x in states]
    data_cure=[int(curr[x][1]) for x in states]
    data_death=[int(curr[x][2]) for x in states]
    
    b={}
    for i in range(0,len(states)):
        b[states[i]]=data_total[i]
    
    sorted_curr=dict(sorted(b.items(),key=operator.itemgetter(1),reverse=True))
    states=[x for x in sorted_curr.keys()]
    data_total=[int(curr[x][0]) for x in states]
    top10=data_total[0:10]
    least10=data_total[-10:]
    plt.clf()
    plt.pie(top10,labels=states[0:10],startangle=90,autopct=absolute_value,shadow=True)
    
    plt.axis('equal')
    plt.title("Total cases in Top 10 states in india\n")
    print(sorted_curr)
    plt.savefig("static/images/a.png")

    plt.clf()
    plt.clf()
    plt.pie(least10,labels=states[-10:],startangle=45,autopct=absolute_values,shadow=True)
    plt.title("Total cases in Least 10 states in india")

    plt.savefig("static/images/b.png")

    
    if changed:
        print("changed")
    else:
        print("not changed")
    total=sum(data_total)
    death=sum(data_death)
    cure=sum(data_cure)
    print(len(data_total))
    li=[total,cure,death]
    print(li)
    return li       
d=web()



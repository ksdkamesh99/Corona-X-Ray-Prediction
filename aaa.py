    soup = BeautifulSoup(response, 'html5lib')
    table=soup.findAll("tr")
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
    curr={x[1]:x[2:] for x in list[1:-1]}
    j.save(curr)
    changed=False
    for states in curr:
        if states not in past:
            changed=True
            past[states]=['0','0','0','0']
    states=[x for x in curr.keys()]
    states=states[:-1]
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

    #plt.pie(top10,labels=states[0:10],startangle=90,autopct=absolute_value,shadow=True)
    
    #plt.axis('equal')
    #plt.title("Total cases in Top 10 states in india\n")
    #print(sorted_curr)
    #plt.savefig("templates/images/a.png")

    #plt.clf()
    #plt.pie(least10,labels=states[-10:],startangle=45,autopct=absolute_values,shadow=True)
    #plt.title("Total cases in Least 10 states in india")

    #plt.savefig("templates/images/b.png")

    
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests


    

def Home(request):
    
    link = 'https://www.theguardian.com/football/premierleague/table'
    if request.method == "POST":
        link=request.POST.get('liga')
        print(request.POST.get('liga') , 'ligaaa')

    url = requests.get(link)
    data = BeautifulSoup(url.content,'html.parser')
    data.findChild('')

    data1 = data.find('div',class_='u-cf').div.table.tbody.findChildren('tr',recursive=False)

    komands = []
    for x in data1:

        komands.append({
            '1': x.findChild('td',{'class':'table-column--sub'} ).text ,
            '2': x.findChild('td',{'class':'table-column--main'}).a.text.strip(),
            '3': x.findChildren()[5].text ,
            '4': x.findChildren()[3]['src'],
            '5': x.findChildren()[11].text ,
            '6': x.findChildren()[12].text ,

            # '2': ,
            # '2': ,
            # '2': ,
        
        })

    return render(request, 'index.html',  {'data':komands , 'link':link} )

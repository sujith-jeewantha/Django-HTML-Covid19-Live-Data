from multiprocessing import context
from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com",
	"X-RapidAPI-Key": "363c456a36mshbb8e44e8a450bf5p14bb03jsn9c6df710dc3c"
}

response = requests.request("GET", url, headers=headers).json()

def mydata(request):
    
    mylist = []
    noofresults = int(response['results'])
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
        
    if request.method == 'POST':
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) -  int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'death': deaths}
        return render(request, 'index.html', context)

    noofresults = int(response['results'])
   
    context = {'mylist': mylist}
    return render(request, 'index.html', context)
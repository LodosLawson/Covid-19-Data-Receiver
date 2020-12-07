#Cvoid-19 DataReceiver v0.5
#The code is written and developed by Mehemmed AC

#My Instagram Page : mehemmed_ac

#If you have used and liked it, don't forget to follow.
#If there is a problem, please do not forget to report it.

#this is the my email : mehemmedac@gmail.com

import requests
import lxml.html as lh

#Do not play with these functions
def CovidInfoColector(Country):    #enter a list here
    
    #Do not play with these functions
    All_Info = []
    
    Referenced_information_ink = "https://www.worldometers.info/coronavirus/"
    Read_Page = requests.get(Referenced_information_ink)
    Information_Gatherer = lh.fromstring(Read_Page.content)
    Distributed_Information = Information_Gatherer.xpath('//tr')
    
    Counter = 0 
    number = []
    country = []
    cases = []
    newcases = []
    deaths = []
    newdeaths = [] 
    recovered = []
    activecases = []
    seriouscritical = []
    totaltests = []
    population = []
    
    #Do not play with these functions
    while True:
        if Counter == 220:
            break 
        number.append(Distributed_Information[Counter].text_content().splitlines()[1])
        country.append(Distributed_Information[Counter].text_content().splitlines()[2])
        cases.append(Distributed_Information[Counter].text_content().splitlines()[3])
        newcases.append(Distributed_Information[Counter].text_content().splitlines()[4])
        deaths.append(Distributed_Information[Counter].text_content().splitlines()[5])
        newdeaths.append(Distributed_Information[Counter].text_content().splitlines()[6])
        recovered.append(Distributed_Information[Counter].text_content().splitlines()[7])
        activecases.append(Distributed_Information[Counter].text_content().splitlines()[9])
        seriouscritical.append(Distributed_Information[Counter].text_content().splitlines()[10])
        totaltests.append(Distributed_Information[Counter].text_content().splitlines()[13])
        population.append(Distributed_Information[Counter].text_content().splitlines()[15])
        Counter = Counter + 1
    
    #Do not play with these functions
    allinfo = [number, country, cases, newcases, deaths, newdeaths, 
               recovered, activecases, seriouscritical, totaltests, population]
    
    #Do not play with these functions
    for One_Country in Country:
        Counter = 0
        while True:
            if str(One_Country) == country[Counter]:
                All_Info.append([allinfo[0][Counter]+" <Country Number>", allinfo[1][Counter]+" <Select Country>", allinfo[2][Counter]+" <Total Cases>",
                                 allinfo[3][Counter]+" <New Cases>", allinfo[4][Counter]+" <Total Deaths>", allinfo[5][Counter]+" <New Deaths>",
                                 allinfo[6][Counter]+" <Total Recovered>", allinfo[7][Counter]+" <Active Cases>", allinfo[8][Counter]+" <Serious Critical *There's a Problem Here.*>",
                                 allinfo[9][Counter]+" <Total Tests>", allinfo[10][Counter]+" <Country Population>"])
                break
            Counter = Counter + 1
    return All_Info

def InformationFullReceiver(Requests): #enter a string here
    
    #Do not play with these functions
    Referenced_information_ink = "https://www.worldometers.info/coronavirus/"
    Read_Page = requests.get(Referenced_information_ink)
    Information_Gatherer = lh.fromstring(Read_Page.content)
    Distributed_Information = Information_Gatherer.xpath('//tr')
    
    Counter = 0
    
    #Do not play with these functions
    Back_Frozen = []
    while True:
        if Counter == 220:
            break
        else:
            pass
         
        #Do not play with these functions
        if Requests == "Number":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[1])
        elif Requests == "Country":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[2])
        elif Requests == "TotalCases":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[3])
        elif Requests == "NewCases":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[4])
        elif Requests == "TotalDeaths":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[5])
        elif Requests == "NewDeaths":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[6])
        elif Requests == "TotalRecovered":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[7])
        elif Requests == "ActiveCases":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[8])
        elif Requests == "SeriousCritical":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[9])
        elif Requests == "TotalTests":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[12])
        elif Requests == "Population":
             Back_Frozen.append(Distributed_Information[Counter].text_content().splitlines()[15])
             
        Counter = Counter + 1
        
    return Back_Frozen

#Auxiliary Code to Use Functions

Selected_Countrys = ["USA", "Russia", "France", "UAE", "Palestine"] #Enter the name of the country you want to receive information here. 
for x in CovidInfoColector(Selected_Countrys):
    print("----------------", x[1], "-----------------------")
    for y in x:
        print(y)

#CODE THE END
import requests
import json
import pandas as pd

BASE_URL = "https://api.covid19api.com" 
dataFile = open("data.csv","w+")

def get_DayOne(country, num=200):
    infoList = pd.DataFrame()

    countryURL = BASE_URL + "/dayone/country/" + country + "/status/confirmed"
    countries = requests.get(countryURL)

    FullCountryList = json.loads(countries.text)
    
    for country in FullCountryList['response']['countries'][0:num]:
            infoList.append(country['Country']['Cases']['Status']['Date'])

    return infoList
    
    # i = 0
    # for country in FullCountryList[i:200]:
    #         infoList.append(country[i])
    #         i = i + 1
    # return infoList
        # gave me KeyError: 0

dayOneCasesSA = get_DayOne("switzerland")
print(dayOneCasesSA)





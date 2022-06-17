import wget
import os

#data from john hopkins

#url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series'
url1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
url2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

wget.download(url1, os.getcwd() + '/time_series_covid19_confirmed_US.csv')
wget.download(url2, os.getcwd() + '/time_series_covid19_deaths_US.csv')
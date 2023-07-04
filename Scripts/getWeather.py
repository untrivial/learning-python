import requests, bs4
res = requests.get('https://weather.com/weather/today/l/166a5dffdd4f5ccb70e0b40ef5538562f3479b7755222894988454ec5183ceff')
res.raise_for_status()
weatherFile = bs4.BeautifulSoup(res.text, 'html.parser')

temperature_value = weatherFile.select('.CurrentConditions--tempValue--MHmYY')
print(temperature_value[0].getText())


from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getData(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bsObj = BeautifulSoup(html.read())
    divData = bsObj.body.div
  except AttributeError as e:
    return None
  return divData

def main():
  divData = getData('https://launchpad.binance.com/en/viewall/lpd')
  if divData == None:
    print('The divData could not be found')
  else:
    data = [element for element in divData.find_all('div', 'css-1vuyzse')]
    
    a = [element.text for element in data[0].find_all('div', 'css-99b0hx')]
    print(a)

if __name__ == '__main__':
  main()

from selenium import webdriver

url = "https://data.typeracer.com/pit/race_history?user=reckful&universe=play&n=100&cursor=&startDate="

def scrape(url, ChromeDriverPath):
    """
    scrape downloads all races in the race history of a profile provided by url
    scrape(typeracer race history URL, ChromeDriverPath) -> List of Raw TypeRacer Data
    """
    driver = webdriver.Chrome("C:/Users/Earl/Desktop/Temp 2/chromedriver/chromedriver.exe")
    driver.get(url)
    data = []
    while(1):
        data += (driver.find_element_by_class_name('scoresTable').text.split('\n'))[1:]
        try:
            driver.find_element_by_partial_link_text('load older results').click()
        except:
            break
    return data

#from openpyxl import Workbook

#data = scrape(url)

#wb = Workbook()
#ws = wb.active

#for pos, val in enumerate(data):
    #ws.cell(row=pos + 1, column=1).value = val

#wb.save('TypeRacer Data.xlsx')

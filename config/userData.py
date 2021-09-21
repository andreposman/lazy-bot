import os
from dotenv import load_dotenv

load_dotenv()

class UserData: 
    url = 'https://www.ahgora.com.br/externo/index/a382748'
    companyId = 'a382748'
    username =  os.getenv('MELI_USERNAME')
    password = os.getenv('MELI_PASSWORD')
    inputMessage = 'lazy bot was here'
    driverPath = os.getenv('WEB_DRIVER_PATH')


class WorkingHours:
    firstHour = '0900'
    exitLunch = '1200'
    returnLunch = '1300'
    exitHour = '1848'

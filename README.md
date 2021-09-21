# lazy-bot

This repo was created to automate my laziness, this bot will (eventually) fill all my working hours. 


To run the project, first you need:
* Python 3.x
*  [selenium web driver]([https://www.selenium.dev/documentation/webdriver/])
* run the command:
    ```bash
    python3 -m pip install python-dotenv     
    ```


Then create a `.env` file in the root folder and change the values to your data:  
```bash
MELI_USERNAME=your_user
MELI_PASSWORD=your_password
WEB_DRIVER_PATH=/your_path/to/webdriver
```


After that run:
```bash
python3 script.py
```
        
        
# Importing the libraries...
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
import time
import pyautogui
from speak import speak
from selenium.webdriver.chrome.service import Service
warnings.simplefilter("ignore")
warnings.simplefilter("module")
warnings.filterwarnings("ignore", category=ResourceWarning)

#Opening the browser for voice recognition...
#-------------------------------------------------------------------------------------------------------------------------------------
try:
    # Define the URL
    url = "https://www.speechtexter.com/"

    # Set up Chrome options
    chrome_options = Options()
    # Run in headless mode
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU to prevent some issues
    prefs = {"hardware.audio_capture_allowed_urls" : ["speechtexter.com","www.speechtexter.com","speechtexter"]}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Emulate UI pop-ups for media access
    chrome_options.add_argument("--use-fake-device-for-media-stream")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.minimize_window()
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/button").click()
    
        
    
except Exception as e:
    print("Error: Unable to configure the ChromeDriver properly.")
    print("To resolve this error, make sure to set up the ChromeDriver correctly.")
    print(e)
#-------------------------------------------------------------------------------------------------------------------------------------


# Defining functions here...
def recognize():
        text_element_xpath = '/html/body/div[1]/div[3]/div[2]/div[3]/div'
        text = driver.find_element(by=By.XPATH, value=text_element_xpath).text
        if len(text) == 0:
            
            return ""
        else:
            div_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/div")
            div_element.clear()
            text = text.strip()
            return text
        
def open_app(app):
    pyautogui.press('win')
    time.sleep(0.7)
    pyautogui.typewrite(f'{app}', 0.01)
    time.sleep(0.5)
    pyautogui.press('enter')



#-------------------------------------------------------------------------------------------------------------------------------------
speak("Hello Sir, I am Jarvis, your personal assistant. How may I help you?")
print("Listening from now on...")
while(True):
    text = recognize().lower()
    if text != "":
        if ("jarvis" in text ):
            speak("Yes sir?")
            while(True):
                query = recognize().lower()
                if query != "":
                    print(f'You: {query}')
                    if "stop" in query:
                        speak("Okay sir, I am going to sleep now.")
                        break

                    elif "open" in query:
                        speak(f"Opening {query.split(maxsplit=1)[1]}.")
                        open_app(query.split()[1])
                        break
                    
                    else:
                        speak("Sorry sir, I didn't get you. Please try again.")

                
            
        
        


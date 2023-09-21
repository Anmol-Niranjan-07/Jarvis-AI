# Importing the necessary libraries for the program
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
import time
import pyautogui
from speak import speak
from selenium.webdriver.chrome.service import Service

# Ignoring warnings to keep the console clean
warnings.simplefilter("ignore")
warnings.simplefilter("module")
warnings.filterwarnings("ignore", category=ResourceWarning)

# Opening the browser for voice recognition
#-------------------------------------------------------------------------------------------------------------------------------------
try:
    # Define the URL for the speech to text service
    url = "https://www.speechtexter.com/"

    # Set up Chrome options for headless operation
    chrome_options = Options()
    # Run in headless mode
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU to prevent some issues
    # Allow audio capture from the specified URLs
    prefs = {"hardware.audio_capture_allowed_urls" : ["speechtexter.com","www.speechtexter.com","speechtexter"]}
    chrome_options.add_experimental_option("prefs",prefs)
    # Exclude logging and set log level to 3
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    # Emulate UI pop-ups for media access and use fake device for media stream
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  
    chrome_options.add_argument("--use-fake-device-for-media-stream")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    # Minimize the browser window
    driver.minimize_window()
    # Open the specified URL
    driver.get(url)
    # Click the button to start voice recognition
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/button").click()
    
        
    
except Exception as e:
    # Print error message if unable to configure the ChromeDriver properly
    print("Error: Unable to configure the ChromeDriver properly.")
    print("To resolve this error, make sure to set up the ChromeDriver correctly.")
    print(e)
#-------------------------------------------------------------------------------------------------------------------------------------


# Defining functions for voice recognition and opening applications
def recognize():
        # XPath for the text element in the speech to text service
        text_element_xpath = '/html/body/div[1]/div[3]/div[2]/div[3]/div'
        # Get the text from the text element
        text = driver.find_element(by=By.XPATH, value=text_element_xpath).text
        # If the text is empty, return an empty string
        if len(text) == 0:
            
            return ""
        else:
            # Clear the text element for the next recognition
            div_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/div")
            div_element.clear()
            # Remove leading and trailing spaces from the text
            text = text.strip()
            return text
        
def open_app(app):
    # Press the Windows key to open the start menu
    pyautogui.press('win')
    # Wait for the start menu to open
    time.sleep(0.7)
    # Type the name of the app to search for it
    pyautogui.typewrite(f'{app}', 0.01)
    # Wait for the search results to appear
    time.sleep(0.5)
    # Press enter to open the app
    pyautogui.press('enter')



#-------------------------------------------------------------------------------------------------------------------------------------
# Start the assistant with a greeting and start listening for commands
speak("Hello Sir, I am Jarvis, your personal assistant. How may I help you?")
print("Listening from now on...")
while(True):
    # Recognize the spoken text
    text = recognize().lower()
    # If the text is not empty and contains the word "jarvis"
    if text != "" and "jarvis" in text:
        # Respond to the user
        speak("Yes sir?")
        while(True):
            # Recognize the user's query
            query = recognize().lower()
            if query != "":
                print(f'You: {query}')
                # If the query contains the word "stop", put the assistant to sleep
                if "stop" in query:
                    speak("Okay sir, I am going to sleep now.")
                    break

                # If the query contains the word "open", open the specified app
                elif "open" in query:
                    speak(f"Opening {query.split(maxsplit=1)[1]}.")
                    open_app(query.split()[1])
                    break
                
                # If the query is not recognized, ask the user to try again
                else:
                    speak("Sorry sir, I didn't get you. Please try again.")

                
            
        
        


from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire.utils import decode

def interceptor(request):
    if 'ws_api.php?ip' in request.url:
        request.url = request.url.replace("136.228.172.22","46.196.32.69");
        print("Reached Here !")
        

# Create a new instance of the Chrome driver with Selenium Wire capabilities
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.request_interceptor = interceptor
driver.get('https://weatherstack.com/')


# Interact with the browser as needed (e.g., navigate to a website, perform actions)

# # Access and manipulate network requests and responses
# for request in driver.requests:
#     if 'ws_api.php?' in request.url:
#         response = request.response
#         body = decode(response.body,response.headers.get('Content-Encoding', 'identity'))
#         body_content = body.decode('utf-8')
#         print(body_content)


# Close the browser
driver.quit()

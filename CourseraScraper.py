'''
@author: Rajarshi Das
'''

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

if __name__ == '__main__':
   
    # http://kb.mozillazine.org/Firefox_:_FAQs_:_About:config_Entries
    profile = webdriver.FirefoxProfile(sys.argv[2])

    # Setting profile parameters
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.download.dir", sys.argv[3])
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf, video/mp4")
    profile.set_preference("pdfjs.disabled", True);
    profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
    profile.set_preference('browser.helperApps.alwaysAsk.force',False)

    # Start Firefox webdriver
    driver = webdriver.Firefox(firefox_profile=profile)
    
    # Go to class page
    className = sys.argv[1]
    driver.get("https://class.coursera.org/" + className + "/lecture/index")
    
    # Wait 10 seconds for page to load
    time.sleep(10)
    
    # Parsing html of page
    soup = BeautifulSoup(driver.page_source)
    
    downloadLinks = []
    for link in soup.find_all('a'):
        if (link.get('href')) <> None:
            # mp4 Files
            if (link.get('href').startswith('https://class.coursera.org/' + className + '/lecture/download.mp4')):
                downloadLinks.append(link.get('href'))
            # pdf files
            if(link.get('href')[-3:]) == 'pdf':
                downloadLinks.append(link.get('href'))
  
    for item in downloadLinks:
        print("Downloading Item: " + item)
        try:
            driver.get(item)
        except:
            print ('Error - check link')
            continue

    # Browser must be closed manually
   

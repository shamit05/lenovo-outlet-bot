import sys
import time
from selenium import webdriver
from sms import send
from datetime import timedelta
from chromedriverauto import chromedriverautodownload
from cryptography.fernet import Fernet
from lenovosettings import settingscool, setup
default = 0
key = b'VRYVm3P5pRgUVwTF2dt5T4oHpBdMW78k3E0kibU8BNY='
cipher_suite = Fernet(key)
def mainclick(website):
    global limit, costmax, savedmin
    while limit == 0:
        time.sleep(1)
        price_saved = [i.text.replace('$', "").replace(',', '') for i in driver.find_elements_by_css_selector('[itemprop=youSave]')]
        cost = [i.text.replace('$', "").replace(',', '') for i in driver.find_elements_by_css_selector('[itemprop=price]')]
        item = [i.text.replace('\n?', "") for i in driver.find_elements_by_css_selector(".facetedResults-title")]
        print(item)
        print(price_saved)
        print(cost)
        for g in range(len(price_saved)):
            if float(cost[g]) > float(costmax):
                limit = 1
            if float(price_saved[g]) >= float(savedmin):
                if float(data[6])/100 <= (float(price_saved[g])/(float(cost[g])+float(price_saved[g]))):
                    try:
                        driver.find_elements_by_link_text("SHOP NOW")[g].click()
                        try:
                            driver.find_element_by_id("addToCartButtonTop").click()
                            itemdetails = '{} added to cart'.format(item[g])
                            itemprice = '\nPrice of item: {}'.format(cost[g])
                            details = '\nPrice saved: {}'.format(price_saved[g])
                            print(itemdetails)
                            print(itemprice)
                            print(details)
                            send(itemdetails)
                            send(itemprice)
                            send(details)
                            driver.execute_script("window.history.go(-2)")

                        except:
                            driver.execute_script("window.history.go(-1)")
                    except:
                        pass
        try:
            driver.find_element_by_link_text("Next Page").click()
        except:
            print("All done")
            break

    print("Finished searching deals")
    send("Finished searching deals")
    elapsed_time_secs = time.time() - start_time
    timetook = '\nTime took: {} (HOUR:MIN:SEC)'.format(timedelta(seconds=round(elapsed_time_secs)))
    send(timetook)


usersettings = open("user.txt","r")
data = usersettings.readlines()
if data[0] == 'setupuser':
    setup(default)

with open('user.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line

while True:
    try:
        usersettings = open("user.txt", "r")
        data = usersettings.readlines()
        phone_number = data[0]
        carrier = data[1]
        break
    except:

        print("setup phone number")
        setup(1)
        send("successfully changed phone number")
        print("Successfully changed phone number. If text isn't recieved please make sure you put in the "
              "right phone number")


while True:
    try:
        usersettings = open("user.txt", "r")
        data = usersettings.readlines()

        with open('user.bin', 'rb') as file_object:
            for line in file_object:
                encryptedpwd = line

        login_id = data[2]
        uncipher_text = (cipher_suite.decrypt(encryptedpwd))
        login_pass = bytes(uncipher_text).decode("utf-8") #convert to string
        break
    except:
        print("setup login credentials")
        setup(2)
while True:
    try:
        usersettings = open("user.txt", "r")
        data = usersettings.readlines()

        costmax = data[4]
        savedmin = data[3]
        mainweb = data[5]
        percentsaved = data[6]
        break
    except:
        print("setup search parameters")
        setup(3)

usersettings = open("user.txt", "r")
data = usersettings.readlines()
settings = input("Choose to run (normal/indefinetly) or change settings ([r]/i/s): ")
while settings == 's':
    if settings == 's':
        settingscool(default)
    settings = input("Choose to run (normal/indefinetly) or change settings ([r]/i/s): ")

chromedriverautodownload()
chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
# logs in
a = 0
try:
    driver.get("https://www.lenovo.com/us/en/outletus/login")
    driver.find_element_by_name('j_username').send_keys(login_id)
    driver.find_element_by_name('j_password').send_keys(login_pass)
    driver.find_element_by_class_name("button-called-out").click()
    driver.find_element_by_name('j_username').send_keys("failedlogin")
    a = 1

except:
    pass
if a == 1:
    exit()
if settings == 'i':
    while True:
        # starts time
        start_time = time.time()
        mainweb = data[5]
        limit = 0
        driver.get(mainweb)
        mainclick(mainweb)
else:
    # starts time
    start_time = time.time()
    mainweb = data[5]
    limit = 0
    driver.get(mainweb)
    mainclick(mainweb)


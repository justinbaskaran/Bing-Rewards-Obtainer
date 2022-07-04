#!/usr/bin/python
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import re
import string
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from datetime import date
# MAKE SURE TIME ZONE IS DETROIT, THIS IS VERY VERY IMPORTANT

# word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
# resp=requests.get('https://httpbin.org/user-agent')
# response = requests.get(word_site,headers={'User-Agent':resp.json()['user-agent']})
# file1 = open('words.txt', 'r')

# TotalRewardsLinnk="/home/pi/Documents/BingSpammer/outputofgenerate.txt"
# with open(TotalRewardsLinnk,"w+") as abc:
#       abc.seek(0)
#      abc.truncate()

Lines = []
with open('/home/pi/Documents/BingSpammer/words.txt') as f:
    Lines = f.read().splitlines()
WORDS = Lines
# print(len(WORDS))
if (len(WORDS)) < 50:
    print("Invalid words dict")
    sys.exit()


def pcSearch(username, password):
    # os.system('killall firefox-esr')
    ##################################################################################    PC SEARCH ##########################################################

    os.environ["DISPLAY"] = ":0.0"

    driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path="/usr/lib/geckodriver",capabilities= {"marionette": False })

    driver.get(
        "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1564176731&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d429A197447C948E1BD086D1B86205782%2526wlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d31F52067648160FD3A4F2DC2652961ED&lc=1033&id=264960&CSRFToken=c19aafb6-3c77-4d03-8449-3086ea6d5785&aadredir=1")

    time.sleep(5)
    elem = driver.find_element_by_name("loginfmt")
    elem.clear()
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    passelem = driver.find_element_by_name("passwd")
    passelem.clear()
    passelem.send_keys(password)
    passelem.send_keys(Keys.RETURN)
    time.sleep(5)
    buttons=driver.find_elements_by_tag_name("input")
    for i in buttons:
        #print("Next Screen " + i.text)
        if i.get_attribute("value").strip()=="Yes":
            #time.sleep(20)
            #print("Yes Clicked")
            i.click()
            break
            #time.sleep(20)

       
    
    time.sleep(30)
    print("bing stage of validate")
    driver.get("https://www.bing.com")
    time.sleep(30)    
    buttons=driver.find_elements_by_tag_name("a")
    for i in buttons:
        print(i.text.strip())
        if i.text.strip()=="SIGN IN >":
            i.click()
            break

    time.sleep(5)
    driver.get("https://www.bing.com")
    time.sleep(5)
    for i in range(1, 35):
        time.sleep(random.randint(0, 1) + 1 * i)
        if len(driver.find_elements_by_id("idSIButton9")) > 0:
            driver.find_element_by_id("idSIButton9").click()
        else:
            # time.sleep(10)
            elem = driver.find_element_by_name("q")
            elem.clear()
            elem.send_keys(WORDS[random.randint(0, 4000)])
            elem.send_keys(Keys.RETURN)

    driver.close()


def mobileIESearch(username, password):
    # os.system('killall chromium-browser')

    ############################################################################## MOBILE BROWSERS #######################################################

    os.environ["DISPLAY"] = ":0.0"
    mobile_emulation = "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", mobile_emulation)
    driver = webdriver.Firefox(firefox_profile=profile)

    # driver = webdriver.Firefox(firefox_profile=profile,executable_path="/usr/lib/geckodriver",capabilities= {"marionette": False })
    driver.get("https://www.bing.com/account")

    driver.find_element_by_id("geoname").send_keys("Sterling Heights, MI 48312")
    driver.find_element_by_id("geoname").send_keys(Keys.RETURN)

    print(driver.execute_script("return navigator.userAgent"))
    driver.get(
        "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1564176731&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d429A197447C948E1BD086D1B86205782%2526wlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d31F52067648160FD3A4F2DC2652961ED&lc=1033&id=264960&CSRFToken=c19aafb6-3c77-4d03-8449-3086ea6d5785&aadredir=1")
    time.sleep(5)
    elem = driver.find_element_by_name("loginfmt")
    elem.clear()
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    passelem = driver.find_element_by_name("passwd")
    passelem.clear()
    passelem.send_keys(password)
    passelem.send_keys(Keys.RETURN)
    time.sleep(2)
    if len(driver.find_elements_by_id("idSIButton9")) > 0:
        driver.find_element_by_id("idSIButton9").click()
    time.sleep(2)
    time.sleep(5)
    buttons=driver.find_elements_by_tag_name("input")
    for i in buttons:
        #print("Next Screen " + i.text)
        if i.get_attribute("value").strip()=="Yes":
            #time.sleep(20)
            #print("Yes Clicked")
            i.click()
            break
            #time.sleep(20)

       
    
    time.sleep(30)
    print("bing stage of validate")
    driver.get("https://wwww.bing.com")
    time.sleep(30)    
    buttons=driver.find_elements_by_tag_name("a")
    for i in buttons:
        print(i.text.strip())
        if i.text.strip()=="SIGN IN >":
            i.click()
            break

    time.sleep(5)
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(WORDS[random.randint(0, 100) * 2 + 2])
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    for i in range(1, 35):

        time.sleep(random.randint(0, 1) + 1 * i)

        searchUser(driver)

        time.sleep(2)

        if len(driver.find_elements_by_id("idSIButton9")) > 0:
            driver.find_element_by_id("idSIButton9").click()
        else:
            if len(driver.find_elements_by_id("hb_n")) > 0:
                if driver.find_element_by_id("hb_n").text == "Sign in":
                    driver.find_element_by_id("mHamburger").click()
                    driver.find_element_by_id("hb_n").click()
            # time.sleep(10)
            # elem = driver.find_element_by_name("q")
            # elem.clear()
            # elem.send_keys(WORDS[random.randint(0,4000)])
            driver.get("https://www.bing.com/search?q=" + str(WORDS[random.randint(0, 4000)]))
        # elem.send_keys(Keys.RETURN)

    #        break

    driver.close()


def searchUser(driver):
    driver.get("https://login.live.com")
    time.sleep(5)
    if len(driver.find_elements_by_id("loginHeader")) > 0:

        driver.get("https://www.bing.com/account")

        driver.find_element_by_id("geoname").clear()
        driver.find_element_by_id("geoname").send_keys("Sterling Heights, MI 48312")
        driver.find_element_by_id("geoname").send_keys(Keys.RETURN)

        print(driver.execute_script("return navigator.userAgent"))
        driver.get(
            "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1564176731&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d429A197447C948E1BD086D1B86205782%2526wlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d31F52067648160FD3A4F2DC2652961ED&lc=1033&id=264960&CSRFToken=c19aafb6-3c77-4d03-8449-3086ea6d5785&aadredir=1")
        time.sleep(5)
        elem = driver.find_element_by_name("loginfmt")
        elem.clear()
        elem.send_keys(sys.argv[1])
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        passelem = driver.find_element_by_name("passwd")
        passelem.clear()
        passelem.send_keys(sys.argv[2])
        passelem.send_keys(Keys.RETURN)
        time.sleep(5)
        buttons=driver.find_elements_by_tag_name("input")
        for i in buttons:
            #print("Next Screen " + i.text)
            if i.get_attribute("value").strip()=="Yes":
                #time.sleep(20)
                #print("Yes Clicked")
                i.click()
                break
            #time.sleep(20)

       
    
        time.sleep(30)
        print("bing stage of validate")
        driver.get("https://www.bing.com/account")
        time.sleep(30)    
        buttons=driver.find_elements_by_tag_name("a")
        for i in buttons:
            print(i.text.strip())
            if i.text.strip()=="SIGN IN >":
                i.click()
                break

        time.sleep(5)
        time.sleep(2)
        if len(driver.find_elements_by_id("idSIButton9")) > 0:
            driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

    driver.get("https:/www.bing.com")


def survey(username, password):
    # os.system('killall chromium-browser')
    # os.system('killall firefox-esr')

    os.environ["DISPLAY"] = ":0.0"

    # fp = webdriver.FirefoxProfile()

    driver = webdriver.Firefox()
    # driver = webdriver.Firefox(firefox_profile=fp,executable_path="/usr/lib/geckodriver",capabilities= {marionette": False })
    driver.get(
        "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1564176731&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d429A197447C948E1BD086D1B86205782%2526wlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d31F52067648160FD3A4F2DC2652961ED&lc=1033&id=264960&CSRFToken=c19aafb6-3c77-4d03-8449-3086ea6d5785&aadredir=1")

    time.sleep(5)
    elem = driver.find_element_by_name("loginfmt")
    elem.clear()
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    passelem = driver.find_element_by_name("passwd")
    passelem.clear()
    passelem.send_keys(password)
    passelem.send_keys(Keys.RETURN)

    time.sleep(5)
    buttons=driver.find_elements_by_tag_name("input")
    for i in buttons:
        if i.text=="Next":
            i.click()

    #driver.get("https://www.google.com")
    #time.sleep(5)
    #driver.get("https://www.bing.com")
    time.sleep(5)
    driver.get("https://account.microsoft.com/rewards/")
    #time.sleep(60)
    buttons=driver.find_elements_by_tag_name("input")
    for i in buttons:
        if i.text=="Sign In":
            i.click()
    time.sleep(100)
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/div/mee-rewards-daily-set-section/div/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/div[3]/a/span/ng-transclude").click()

    # clickable = driver.find_element_by_partial_link_text("points")[0]

    time.sleep(5)
    # print (clickable.text)

    # clickable.click()

    time.sleep(5)

    # driver.find_element_by_xpath().click()

    driver.close()


#     with open(TotalRewardsLinnk, 'a') as f:
#            f.write(str(username) + " Clicked Search: 10/10\n")

# os.system('killall firefox-esr')

# os.system('killall chromium-browse')
def validate(username, password):
    # os.system('killall chromium-browser')
    # os.system('killall firefox-esr')
    os.environ["DISPLAY"] = ":0.0"

    # driver = webdriver.Firefox(firefox_profile=fp,executable_path="/usr/lib/geckodriver",capabilities= {"marionette": False })
    driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",capabilities= {"marionette": False })
    driver.get(
        "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1564176731&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d429A197447C948E1BD086D1B86205782%2526wlexpsignin%253d1%2526wlexpsignin%253d1%26sig%3d31F52067648160FD3A4F2DC2652961ED&lc=1033&id=264960&CSRFToken=c19aafb6-3c77-4d03-8449-3086ea6d5785&aadredir=1")

    time.sleep(5)
    elem = driver.find_element_by_name("loginfmt")
    elem.clear()
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    passelem = driver.find_element_by_name("passwd")
    passelem.clear()
    passelem.send_keys(password)
    passelem.send_keys(Keys.RETURN)
    time.sleep(10)
    buttons=driver.find_elements_by_tag_name("input")
    for i in buttons:
        #print("Next Screen " + i.text)
        if i.get_attribute("value").strip()=="Yes":
            #time.sleep(20)
            #print("Yes Clicked")
            i.click()
            break
            #time.sleep(20)

       
    
    time.sleep(30)
    #print("bing stage of validate")
    driver.get("https://account.microsoft.com/rewards")
    time.sleep(30)    
    buttons=driver.find_elements_by_tag_name("a")
    #buttons.append(driver.find_elements_by_tag_name("input"))
    for a in driver.find_elements_by_tag_name("input"):
       buttons.append(a)
    for i in buttons:
     #   print(i.text.strip())
        if i.text.strip()=="SIGN IN >":
            i.click()
            break
    
    
    time.sleep(5)
    driver.get("https://account.microsoft.com/rewards/pointsbreakdown")
    time.sleep(180)

    #element = WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH,
     #                                                                          "/html[1]/body[1]/div[4]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/mee-rewards-user-points-details[1]/div[1]/div[1]/div[1]/div[1]/p[2]")))

    edgeBonusAmt=""
    pcAmt=""
    mobileAmt=""


    import re

    value="0"
    for i in range(0,10):
        if len(driver.find_elements_by_xpath("/html[1]/body[1]/div["+str(i)+"]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/mee-rewards-user-points-details[1]/div[1]/div[1]/div[1]/div[1]/p[2]"))==1: 
                if re.match("[0-9]{0,3}\s*/\s*[0-9]{0,3}",driver.find_element_by_xpath("/html[1]/body[1]/div["+str(i)+"]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/mee-rewards-user-points-details[1]/div[1]/div[1]/div[1]/div[1]/p[2]").text.strip()):	
                        value=str(i)

    edgeBonusAmt = driver.find_element_by_xpath("/html/body/div["+str(value)+"]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown/div/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]")
    pcAmt = driver.find_element_by_xpath("/html/body/div["+str(value)+"]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown/div/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]")
    mobileAmt = driver.find_element_by_xpath("/html/body/div["+str(value)+"]/div[2]/div[2]/mee-rewards-earning-report-points-breakdown/div/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]")


    edgeBonusAmt=edgeBonusAmt.text
    pcAmt=pcAmt.text
    mobileAmt=mobileAmt.text

    time.sleep(20)

    os.system('killall firefox-esr')

    print(edgeBonusAmt)
    print(pcAmt)
    print(mobileAmt)


    if ( int(pcAmt.split(" / ",1)[0]) == int(pcAmt.split(" / ",1)[1]) and int(mobileAmt.split(" / ",1)[0]) == int(mobileAmt.split(" / ",1)[1])) and int(edgeBonusAmt.split(" / ",1)[0]) == int(edgeBonusAmt.split(" / ",1)[1]):
        #           with open(TotalRewardsLinnk, 'a') as f:
        #                  f.write(str(username)+ " Searches: 270/270\n")
        return True
    else:
        #         with open(TotalRewardsLinnk, 'a') as f:
        #                f.write(str(username) + " Searches 0/270!\n")
        return False


def doSearches(tries,username,password):
    try:
        while True:
           if validate(username,password) == True:
                break
           mobileIESearch(username,password)
           pcSearch(username,password)
           #survey(username,password)
           time.sleep(random.randint(1, 10) * 60)

    except Exception as e:
        print(e)
        os.system('killall chromium-browser')
        os.system('killall firefox-esr')
        time.sleep(random.randint(1, 10) * 60)
        if tries < sys.getrecursionlimit():  # By default 1,000 can be bumped up by setrecursionlimit

            # just for kicks
            # else:
            sys.setrecursionlimit(sys.getrecursionlimit() + 1)
            # print("Yes we'll win this game the old-fashioned way, the tried and true way:")
            # print("We'll cheat!")
            # refactor / prettify if's to call init_driver if you want to cheat.
            return doSearches(tries + 1,username,password)

        else:
            print("OH NO RECURSION LIMIT HIT!!!!!!")




doSearches(0,"USERNAME@gmail.com", "PASSWORD")


#os.system('killall chromium-browser')
#os.system('killall firefox-esr')
#os.system('python3 /home/pi/Documents/BingSpammer/status.py')

TotalRewardsLinnk="/home/pi/Documents/BingSpammer/outputofgenerate.txt"
with open(TotalRewardsLinnk,"a") as abc:
      #abc.seek(0)
      #abc.truncate()
      abc.write(str(date.today())+":  All Rewards Recieved\n")



#os.system("export DISPLAY=:0 && export PATH=$PATH:/usr/lib/  && /usr/bin/python3 /home/pi/Documents/BingSpammer/status.py")

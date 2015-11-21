__author__ = 'Mandeep Jadon'
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print "####################################################################################" \
 '''

' _______          _               _______        _ _
 |__   __|        (_)             |__   __|      | | |
    | |_   _ _ __  _ _ __   __ _     | |_ __ ___ | | | ___ _ __
    | | | | | '_ \| | '_ \ / _` |    | | '__/ _ \| | |/ _ \ '__|
    | | |_| | |_) | | | | | (_| |    | | | | (_) | | |  __/ |
    |_|\__, | .__/|_|_| |_|\__, |    |_|_|  \___/|_|_|\___|_|  
        __/ | |             __/ |
       |___/|_|            |___/

                                                           V 1.0
                                                           
                            THE MOST UNPRODUCTIVE TOOL OF THE DECADE

                            AUTHOR : MANDEEP JADON (CIPH3R7R0LL)
                            


"####################################################################################" \''''
print "Welcome to the typing bot !!! \n \n \n Select the site that you want to troll \n \n \n 1.app.typrx.com \n 2.careerstep.com \n 3.goodtyping.com \n 4.keyhero.com \n 5.rapidtyping.com \n 6.ratatype.com \n 7.typingtest.com \n 8.calculatorcat.com \n \n "
choice = int(raw_input())
while True:
    try:
        driver=webdriver.Chrome()
        driver.implicitly_wait(30)
        if choice==1:
            driver.get("http://www.ultimatetypingchampionship.com/")
            submit=driver.find_element_by_xpath("//*[@id='middle-section']/div[3]/a/img")
            submit.click()
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            driver.get("http://app.typrx.com/#RacePlace:race")
            '''click_button=driver.find_element_by_class_name("GNCH05MCEJ")
            click_button.click()
            username=driver.find_element_by_class_name("gwt-TextBox")
            username.send_keys("Enter you registered email ID here ")
            password= driver.find_element_by_class_name("gwt-PasswordTextBox")
            password.send_keys("Enter the password ")
            submit=driver.find_element_by_css_selector("body > div.gwt-DialogBox > div > table > tbody > tr.dialogMiddle > td.dialogMiddleCenter > div > table > tbody > tr:nth-child(7) > td > table > tbody > tr > td:nth-child(1) > button")
            submit.click()
            #compete=driver.find_element_by_xpath("//*[@id='GWTUI']/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/img")
            #compete.click()'''
            time.sleep(18)
            inputbox = driver.find_element_by_class_name("cw-QuotePanel-textToTypePanel")
            wordsarray = inputbox.find_elements_by_tag_name("span")
            li=[]
            for i in wordsarray:
                li.append(i.text)
            writebox= driver.find_element_by_xpath("//*[@id='GWTUI']/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")
            for i in li:
                writebox.send_keys(i+" ")


        elif choice==2:
            driver.get("http://www.careerstep.com/free-typing-test")
            inputbox = driver.find_element_by_class_name("text")
            wordsarray=str(inputbox.text).split()
            writebox= driver.find_element_by_tag_name("textarea")
            for i in wordsarray:
                writebox.send_keys(i+" ")


        elif choice==3:
            driver.get("http://www.goodtyping.com/test.php")
            inputbox = driver.find_element_by_id("clock")
            wordsarray=str(inputbox.text).split()
            writebox= driver.find_element_by_tag_name("textarea")
            for i in wordsarray:
                writebox.send_keys(i+" ")



        elif choice==4:
            driver.get("http://www.keyhero.com/free-typing-test")
            #driver.get("http://www.keyhero.com/logincreate/")
            #username= driver.find_element_by_id("id_usernamelogin")
            #username.send_keys("name here ")
            #password=driver.find_element_by_id("id_password")
            #password.send_keys("password here ")
            submit=driver.find_element_by_css_selector("#typing-test > div > div.col-md-8 > div.input-menu > button.start-button.btn.btn-lg.btn-success")
            submit.click()
            #practice_start=driver.find_element_by_css_selector("body > div.navbar.navbar-default.navbar-static-top > div > div.navbar-collapse.collapse > ul:nth-child(1) > li:nth-child(1) > a")
            #practice_start.click()
            #typing_test=driver.find_element_by_css_selector("body > div.container > div.row > div.col-md-8 > a.btn.btn-success.btn-lg")
            #typing_test.click()
            #submit=driver.find_element_by_xpath("//*[@id='typing-test']/div/div[1]/div[2]/button[1]/span[3]")
            #submit.click()
            time.sleep(6)
            first_letter= driver.find_element_by_class_name("quote-current")
            first_letter=[first_letter.text.strip("\"")]
            inputbox = driver.find_element_by_xpath("//*[@id='typing-test']/div/div[1]/div[1]/div/span[5]")
            #wordsarray = inputbox.find_elements_by_tag_name("span")
            li= str(inputbox.text).split()
            li=first_letter + li
            writebox= driver.find_element_by_class_name("user-input-text")
            for i in li:
                #time.sleep(0.4)
                writebox.send_keys(i+" ")



        elif choice==5:
            driver.get("http://www.rapidtyping.com/online-typing-test.html")
            driver.find_element_by_xpath("//*[@id='man']/div[2]/form/select[1]/option[4]").click()
            driver.find_element_by_name("update").click()
            myname=driver.find_element_by_xpath("//*[@id='man']/div[2]/form/input[1]")
            myname.clear()
            myname.send_keys("DEATH ANGEL")
            words=driver.find_element_by_id("area1")
            words=str(words.text).split()
            driver.find_element_by_name("start").click()
            writebox= driver.find_element_by_xpath("//*[@id='area3']")
            for i in words:
                writebox.send_keys(i+" ")
            driver.find_element_by_name("done").click()


        elif choice==6:
            driver.get("http://www.ratatype.com/typing-test/test/")
            submit=driver.find_element_by_tag_name("button")
            submit.click()
            inputbox = driver.find_element_by_class_name("mainTxt")
            wordsarray = inputbox.find_elements_by_tag_name("span")
            li=[]
            for i in wordsarray:
                li.append(i.text)
            del li[1::2]
            writebox= driver.find_element_by_tag_name("textarea")
            for i in range(len(li)):
                #time.sleep(.24)
                #if i==len(li)-1:
                 #   writebox.send_keys(li[i])
                #else:
                writebox.send_keys(li[i]+" ")

        elif choice==7:
            driver.get("http://www.typingtest.com/test.html?minutes=1&textfile=aesop.txt")
            inputbox = driver.find_element_by_xpath("//*[@id='test-container']/div[2]")
            wordsarray = inputbox.find_elements_by_tag_name("span")
            li=[]
            for i in wordsarray:
                li.append(i.text)
            writebox= driver.find_element_by_id("test-edit-area")
            for i in li:
                writebox.send_keys(i+" ")


        elif choice ==8:
            driver.get("http://www.calculatorcat.com/typing_test/")
            for i in range(15):
                inputbox = driver.find_element_by_id("eTT_id_text")
                li=str(inputbox.text).split()
                writebox= driver.find_element_by_tag_name("textarea")
                for i in li:
                    writebox.send_keys(i+" ")
                nextbutton=driver.find_element_by_name("newtext")
                nextbutton.click()

    except KeyboardInterrupt:
        print "Y u prezzzz ctrl+c :'( :'( ')"
        sys.exit(0)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise







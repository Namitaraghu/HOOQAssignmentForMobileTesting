from appium import webdriver

desired_cap={
  "deviceName": "e204b7b0",
  #"app": "D:\\\\Appium Stuff\\\\209.apk", --> showing dialog box for new updates. Outdated app so taken latest .apk from Google.
  "app":"D:\\\\Appium Stuff\\\\HOOQ Watch Movies TV Shows Live Channels News_v3.12.1-b940_apkpure.com.apk",
  "appPackage":"tv.hooq.android",
  "appActivity":"tv.hooq.androidbeta.features.launcher.SplashActivity",
  #"appActivity":"tv.hooq.androidbeta.features.launcher.LoadingActivity",
  "version": "9.0",
  "platformName": "Android",
  "autoAcceptAlerts" : "FALSE"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(10)
driver.find_element_by_id("tv.hooq.android:id/loginButton").click()
driver.implicitly_wait(10)
driver.find_element_by_id("android:id/button1").click()
# loop for selecting one email id from list displayed
for element in driver.find_elements_by_class_name('android.widget.TextView'):
     if element.text == "namitaraghuvanshi92@gmail.com":
          driver.implicitly_wait(10)
          element.click()
driver.implicitly_wait(10)
driver.find_element_by_id("tv.hooq.android:id/emailDone").click()
#Getting message "Account does not exist.[2000]"

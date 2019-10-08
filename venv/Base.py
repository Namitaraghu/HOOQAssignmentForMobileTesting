from appium import webdriver

desired_cap={
  "deviceName": "e204b7b0",
  "app": "D:\\\\Appium Stuff\\\\209.apk",
  "version": "9.0",
  "platformName": "Android"
}
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.install_app('D:\\Appium Stuff\\209.apk')

# Getting error: Original error: packageAndLaunchActivityFromManifest failed. Original error: Could not find 'aapt.exe' in ["D:\\Appium Stuff\\Android SDK\\platform-tools\\aapt.exe","D:\\Appium Stuff\\Android SDK\\emulator\\aapt.exe","D:\\Appium Stuff\\Android SDK\\tools\\aapt.exe","D:\\Appium Stuff\\Android SDK\\tools\\bin\\aapt.exe"]. Do you have Android Build Tools installed at 'D:\Appium Stuff\Android SDK'?
Skip to content

Search…
All gists
GitHub
New gist
382
152 @ziadozziadoz/install.sh
Last active 17 hours ago • 
 
<script src="https://gist.github.com/ziadoz/3e8ab7e944d02fe872c3454d17af31a5.js"></script>
  
 Code  Revisions 18  Stars 382  Forks 152
Install Chrome, ChromeDriver and Selenium on Ubuntu 16.04
 install.sh
#!/usr/bin/env bash
# https://developers.supportbee.com/blog/setting-up-cucumber-to-run-with-Chrome-on-Linux/
# https://gist.github.com/curtismcmullan/7be1a8c1c841a9d8db2c
# http://stackoverflow.com/questions/10792403/how-do-i-get-chrome-working-with-selenium-using-php-webdriver
# http://stackoverflow.com/questions/26133486/how-to-specify-binary-path-for-remote-chromedriver-in-codeception
# http://stackoverflow.com/questions/40262682/how-to-run-selenium-3-x-with-chrome-driver-through-terminal
# http://askubuntu.com/questions/760085/how-do-you-install-google-chrome-on-ubuntu-16-04

# Versions
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
SELENIUM_STANDALONE_VERSION=3.4.0
SELENIUM_SUBDIR=$(echo "$SELENIUM_STANDALONE_VERSION" | cut -d"." -f-2)

# Remove existing downloads and binaries so we can start from scratch.
sudo apt-get remove google-chrome-stable
rm ~/selenium-server-standalone-*.jar
rm ~/chromedriver_linux64.zip
sudo rm /usr/local/bin/chromedriver
sudo rm /usr/local/bin/selenium-server-standalone.jar

# Install dependencies.
sudo apt-get update
sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4

# Install Chrome.
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

# Install ChromeDriver.
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

# Install Selenium.
wget -N http://selenium-release.storage.googleapis.com/$SELENIUM_SUBDIR/selenium-server-standalone-$SELENIUM_STANDALONE_VERSION.jar -P ~/
sudo mv -f ~/selenium-server-standalone-$SELENIUM_STANDALONE_VERSION.jar /usr/local/bin/selenium-server-standalone.jar
sudo chown root:root /usr/local/bin/selenium-server-standalone.jar
sudo chmod 0755 /usr/local/bin/selenium-server-standalone.jar
 start-chrome.sh
#!/usr/bin/env bash

# Run Chrome via Selenium Server
start-chrome() {
    xvfb-run java -Dwebdriver.chrome.driver=/usr/local/bin/chromedriver -jar /usr/local/bin/selenium-server-standalone.jar
}

start-chrome-debug() {
    xvfb-run java -Dwebdriver.chrome.driver=/usr/local/bin/chromedriver -jar /usr/local/bin/selenium-server-standalone.jar -debug
}

# Run Chrome Headless
start-chrome-headless() {
    chromedriver --url-base=/wd/hub
}

# Start
# start-chrome
# start-chrome-debug
# start-chrome-headless
 @jeremyrader
jeremyrader commented on 28 Apr 2017
Dude, you are a lifesaver! Thank you!

 @liang42hao
liang42hao commented on 10 May 2017
update on version:
https://selenium-release.storage.googleapis.com/3.4/selenium-server-standalone-3.4.0.jar
https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip

 @aolave
aolave commented on 12 May 2017 • 
Thank you!

Taking into consider the following permission:

chown root:root /usr/local/share/chromedriver

 @reense
reense commented on 14 May 2017
Thank you so much!

I didn't have unzip installed. So i ran sudo apt-get install unzip. For everyone running into problems. :)

 @mikaelkundert
mikaelkundert commented on 24 May 2017
Thanks! I used different version of chromedriver and selenium and I noticed that the -debug option wasn't working on my setup, so I left it out.

 @partinder
partinder commented on 3 Jul 2017
Sweet!

 @jeniaefimov
jeniaefimov commented on 4 Jul 2017
Thank you guy, so much!

 @ralexrong
ralexrong commented on 10 Jul 2017
thank you

 @mangena-dave
mangena-dave commented on 17 Jul 2017
defiantly a Lifesaver!

 @sanasa
sanasa commented on 17 Jul 2017
Thank youuu !!!

 @derryberni
derryberni commented on 19 Jul 2017
Thank youuu

 @545314690
545314690 commented on 20 Jul 2017
thank you

 @noyoung
noyoung commented on 26 Jul 2017
thank you

 @opiumated
opiumated commented on 26 Jul 2017
Thank you, i keep coming back for this

 @sarikabagga7
sarikabagga7 commented on 15 Aug 2017 • 
Hello, Thanks for sharing. I have added shared code in my project but I am facing below error;

Exception: unknown error: Chrome failed to start: exited normally
  (Driver info: chromedriver=2.20.353124 (035346203162d32c80f1dce587c8154a1efa0c3b),platform=Linux 4.4.0-89-generic x86_64) (WARNING: The server did not provide any stacktrace information)
Command duration or timeout: 60.04 seconds
Build info: version: '3.4.0', revision: 'unknown', time: 'unknown'
System info: host: 'a39f04d0b59d', ip: '172.17.0.4', os.name: 'Linux', os.arch: 'amd64', os.version: '4.4.0-89-generic', java.version: '1.8.0_131'

 @Xosmond
Xosmond commented on 31 Aug 2017
Thank you so muuch

 @rohit12sh
rohit12sh commented on 3 Sep 2017
Thanks!!

 @HoangJerry
HoangJerry commented on 6 Sep 2017
I am beginer, please noted me how to do step by step.

 @onassar
onassar commented on 9 Sep 2017
Anyone tested this on Ubuntu 14.04.5 LTS? Tried and no luck. Getting:
./start-chrome.sh: line 5: xvfb-run: command not found

 @sunilkhuwal
sunilkhuwal commented on 19 Sep 2017
any alternative to wget command when executing the shell on windows OS machine

 @mangena-dave
mangena-dave commented on 28 Sep 2017
@sarikabagga7
For unknown reasons it seems like your script is complaining with your current ChromeDriver 2.30
Uninstall the current ChromeDriver and # install latest version of ChromeDriver, in my case is 2.32.

 @werdlv
werdlv commented on 29 Sep 2017
I tried this using php-webdriver but I get following error:

PHP Fatal error:  Uncaught Facebook\WebDriver\Exception\WebDriverCurlException: Curl error thrown for http POST to /session with params: {"desiredCapabilities":{"browserName":"chrome","platform":"ANY","chromeOptions":{"binary":""}}}

Operation timed out after 30000 milliseconds with 0 bytes received in .../vendor/facebook/webdriver/lib/Remote/HttpCommandExecutor.php:286
Stack trace:
#0 /.../vendor/facebook/webdriver/lib/Remote/RemoteWebDriver.php(126): Facebook\WebDriver\Remote\HttpCommandExecutor->execute(Object(Facebook\WebDriver\Remote\WebDriverCommand))
#1 /.../test.php(16): Facebook\WebDriver\Remote\RemoteWebDriver::create('http://localhos...', Object(Facebook\WebDriver\Remote\DesiredCapabilities))
#2 {main}
  thrown in /.../vendor/facebook/webdriver/lib/Remote/HttpCommandExecutor.php on line 286
It seems that for some reason Chrome is unreachable. What could be the issue?

 @MorrisLaw
MorrisLaw commented on 2 Oct 2017
This works beautifully, thank you!

 @abhijity
abhijity commented on 6 Oct 2017 • 
It works fine for me with chrome 61.0.3163.100, chromedriver 2.33 and selenium server standalone 2.53.1. Thank you..

 @ttruong15
ttruong15 commented on 10 Oct 2017 • 
thank you, works beautifully. I been trying getting this things to work for the last couple days now. Pulling my hair out. You are a life saver. Thankyou, Thankyou and Thankyou.

 @mamunrashid001
mamunrashid001 commented on 14 Oct 2017
worked like a charm!

 @dmitryck
dmitryck commented on 16 Oct 2017
thanx!

 @mamontovdmitriy
mamontovdmitriy commented on 21 Oct 2017
Nice job, thank you!

I would added for start-chrome.sh
-Dwebdriver.chrome.whitelistedIps="localhost,127.0.0.1,192.168.*.*"

 @robywan27
robywan27 commented on 25 Oct 2017
Thanks a lot!

 @rifaterdemsahin
rifaterdemsahin commented on 2 Nov 2017
Testing with Chrome Driver and getting these errors

Message: Test method SeleniumGridSmokeTest.UnitTest1.TestMethod1 threw exception: System.InvalidOperationException: Unable to create new service: ChromeDriverService Build info: version: '3.6.0', revision: '6fbf3ec767', time: '2017-09-27T16:15:40.131Z' System info: host: 'seleniumnode', ip: '10.0.0.9', os.name: 'Linux', os.arch: 'amd64', os.version: '4.4.0-97-generic', java.version: '1.8.0_151' Driver info: driver.version: unknown (InsecureCertificate)

 @nobodyme
nobodyme commented on 6 Nov 2017 • 
 wget -N https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P ~/
sudo dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb
sudo apt-get -f install -y
sudo dpkg -i --force-depends ~/google-chrome-stable_current_amd64.deb
Why is that line, 'dpkg -i --force-depends' repeated twice? Can someone explain? Thanks.

 @markusguenther
markusguenther commented on 7 Nov 2017
@nobodyme Also ask me that ;)

 @Alqama
Alqama commented on 11 Nov 2017
Thanks, Man!! That was really helpful. (y)

 @andreasneuber
andreasneuber commented on 20 Nov 2017
Thanks a lot ziadoz!
Actually this gist solves two challenges for me: 1) Install Chrome driver fast, and 2) How to run Codeception acceptance tests headless via xvfb :-)

Just some minor things: I noticed:
xvfb-run java -Dwebdriver.chrome.driver=/usr/local/bin/chromedriver -jar /usr/local/bin/selenium-server-standalone.jar runs better for me with additional flag -a (after xvfb-run)

And Google Chrome install works better for me if line 27 looks like this:
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

 @matthewmuscat
matthewmuscat commented on 21 Nov 2017
Where exactly do past the code for the start_chrome.sh file?

 @trungtnm
trungtnm commented on 29 Nov 2017 • 
@matthewmuscat : you can call it by typing
source start-chrome.sh; start-chrome

 @alsilva86
alsilva86 commented on 12 Dec 2017
Dude you are the best! Still working on ubuntu 16.04

 @Divyapabba16
Divyapabba16 commented on 13 Dec 2017
Hi i followed your code and getting the below error, how can we fix it. please help me in resolving the issue

Starting ChromeDriver 2.29.461571 (8a88bbe0775e2a23afda0ceaf2ef7ee74e822cc5) on port 11458
Only local connections are allowed.
Exception in thread "main" org.openqa.selenium.WebDriverException: unknown error: Chrome failed to start: exited abnormally
(Driver info: chromedriver=2.29.461571 (8a88bbe0775e2a23afda0ceaf2ef7ee74e822cc5),platform=Linux 4.10.0-28-generic x86_64) (WARNING: The server did not provide any stacktrace information)
Command duration or timeout: 60.10 seconds

 @Divyapabba16
Divyapabba16 commented on 13 Dec 2017
@mangena-dave I tried chromedriver with 2.32, 2.33, 2.29, 2.34 and many more still getting the same error, as below

Starting ChromeDriver 2.29.461571 (8a88bbe0775e2a23afda0ceaf2ef7ee74e822cc5) on port 11458
Only local connections are allowed.
Exception in thread "main" org.openqa.selenium.WebDriverException: unknown error: Chrome failed to start: exited abnormally
(Driver info: chromedriver=2.29.461571 (8a88bbe0775e2a23afda0ceaf2ef7ee74e822cc5),platform=Linux 4.10.0-28-generic x86_64) (WARNING: The server did not provide any stacktrace information)
Command duration or timeout: 60.10 seconds

 @shakhal
shakhal commented on 26 Dec 2017
Thanks for sharing! saved me!

 @hadeelsharaf
hadeelsharaf commented on 17 Jan
Thanks,that is very helpful.

 @larry852
larry852 commented on 31 Jan
Thanks

 @andreasneuber
andreasneuber commented on 3 Feb
If unknown error: Chrome failed to start: exited abnormally check if adding arg --no-sandbox to chrome options makes a difference.
Helped me at least.

capabilities:
 chromeOptions:
   args: [ "disable-infobars", "--no-sandbox" ]
 @ORESoftware
ORESoftware commented on 10 Feb • 
this worked for me (need to update the download link):

set -e;

wget -N https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip -P ~/
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip

sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver
 @ksair
ksair commented on 2 Mar
https://linux-tips.com/t/how-to-install-java-8-on-debian-jessie/349

 @aderusha
aderusha commented on 17 Mar • 
You're calling sudo in the wrong place on a couple of lines:

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
should read:
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add

sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
should read:
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee -a /etc/apt/sources.list.d/google-chrome.list

 @jtajtajta
jtajtajta commented on 17 Mar • 
Thank you! Didn't work out as easy as for most others, but extremely helpful in succeeding with installation.

I have a fresh Ubuntu 16.04 installation and curl was not installed. So, at first,initiating the CHROME_DRIVER_VERSION variable would not work. Installed curl and that part was cured.
Everything went smoothly until installation of Chrome driver and Selenium. It was necessary to download them manually, as the script was not able to do that. Opening the http connection was successful, but finding the Chrome and Selenium versions resulted in 404 error.
However, manually downloading, unpacking , installing, moving around and granting rights was easy to do with these instructions. Great work, much appreciated!
EDIT:
After some testing things are not looking good. Firstly, you should mention that in addition to the installation script, Selenium needs to be installed within the python versions that you intend to use, i.e.
pip install selenium
pip3 install selenium

And while having a brand new Ubuntu 16.04 installation, its necessary to install pip, before you can run the two lines above
sudo apt-get install python-pip
sudo apt-get install python3-pip

And yet, after days of trial and error, there is some prognosis, but its still not working. Running following commands in python3:
from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
The second row reports an error after some 30
"......
File "/home/me/.local/lib/python2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: chrome not reachable
(Driver info: chromedriver=2.37.543619 (a237acd3116cac3b3f0da42a000502ce3fafcb23),platform=Linux 4.13.0-37-generic x86_64)"

Clearly, Chrome cannot be found. I installed it using the above script, so obviously I'm missing something that I sholud fix in my environment.

EDIT --- SOLVED!!!
Well, as it so often happens you make some changes and suddenly everything works. I actually tried to open Chrome from the X and failed. It would not open...!!! So I thought that if I have Chromium open, then maybe Chrome doesn't start. I closed Chromium and started Chrome, with success.

Then, running the script worked like charm! Funnily, after that I tried and found out that I CAN have Chromium open, and still get the script working and Chrome opening, just like it should. So, I am not sure why it started working, but am really glad that it did.

 @pwfcurry
pwfcurry commented on 27 Mar
You can also use yarn/npm to install (and update) the driver -
sudo yarn global add chromedriver --prefix /usr/bin
Run to install, and re-run to update when necessary.

 @nshores
nshores commented on 10 Apr • 
EDIT 2 - I have created a docker image to automate the creation of an environment for this, and I've already started to build some notifications around it. Find it here if you want a easier way to get an environment up and running for this great library --

https://github.com/nshores/my_usps_notifications

EDIT I have resolved this. By default, getting a session with myusps.get_session will use PhantomJS. This behavior works in Windows, but not linux. You must manually specificfy Chrome as the webdriver to use in linux - IE myusps.get_session(username, password, driver='chrome') See issue here - happyleavesaoc/python-myusps#14

Major issues getting this running on Ubuntu LTS 16.04. Getting a timeout when trying to login.

raceback (most recent call last):
  File "/home/nshores/.local/lib/python3.5/site-packages/myusps/__init__.py", line 180, in _login
    WebDriverWait(driver, LOGIN_TIMEOUT).until(EC.title_is(WELCOME_TITLE))
  File "/home/nshores/.local/lib/python3.5/site-packages/selenium/webdriver/support/wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message: 


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/nshores/.local/lib/python3.5/site-packages/myusps/__init__.py", line 300, in get_session
    _login(session)
  File "/home/nshores/.local/lib/python3.5/site-packages/myusps/__init__.py", line 182, in _login
    raise USPSError('login failed')
myusps.USPSError: login failed
Tried a bunch of combinations of ChromeDrive, Google Chrome, and Selenium. My environment is --

Chrome - 65.0.333325.181
ChromeDriver -- 2.37
Latest Myusps Script
Python 3.5.2

I'm able to run this fine in windows. Just can't seem to narrow down the issue in Linux. Any ideas? This is very frustrating as I'm trying to work on getting a Docker image together for this project, as well as working on some notification modules to extend it out to Slack, etc.

 @Manoj-nathwani
Manoj-nathwani commented on 16 Apr
This is great! Thank you pray

 @xbacon29x
xbacon29x commented on 17 Apr
I already update my webdriver but when I run my script it always prompt this error.

WebDriverException: Message: disconnected: unable to connect to renderer
(Session info: chrome=65.0.3325.181)
(Driver info: chromedriver=2.31.488763 (092de99f48a300323ecf8c2a4e2e7cab51de5ba8),platform=Linux 4.13.0-37-generic x86_64)

 @lijun003
lijun003 commented 9 days ago
Wonderful job. Thanks！

 @ucanbehack
 
            
 
 

Leave a comment
Attach files by dragging & dropping, , or pasting from the clipboard.  Styling with Markdown is supported
© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
Press h to open a hovercard with more details.

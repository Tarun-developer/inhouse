public  useStoredSessionInNewWindow() {
 // initiate web driver and go to an website
 _webDriver = new FirefoxDriver();
 _webDriver.navigate().to("www.abc.com");

 // add code to login in the website

 // store the current session
 Set<Cookie> cookiesInstance1 = _webDriver.manage().getCookies();
 System.out.println("Coockies = "+cookiesInstance1);

 // close the web driver instance
 _webDriver.close();

 // again initiate web driver and go to the same website. This will open the login page
 _webDriver = new FirefoxDriver();
 _webDriver.navigate().to("www.abc.com");

 // add the stored session in the bew web driver instance
 for(Cookie cookie : cookiesInstance1)
 {
  _webDriver.manage().addCookie(cookie);
 }

 // re-visit the page
 _webDriver.navigate().to("www.abc.com");

 // get the current session of new web driver instance
 Set<Cookie> cookiesInstance2 = _webDriver.manage().getCookies();
 System.out.println("Coockies = "+cookiesInstance2);

 // notice that session of previous web driver instanse is achieved
 Assert.assertEquals(cookiesInstance1, cookiesInstance2);

 }
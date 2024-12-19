Feature: Checking Login and Logout Functionality

Scenario:Verifing Login of LetsKode application
  Given  User should be able to launch chrome browser
  When  User should enter Url
  When  user should navigate to login
  And  Enter Username and Enter Password in Text Box
  And  Click on login button
  Then  Message displayed Login successfull
  Then  User should close the browser
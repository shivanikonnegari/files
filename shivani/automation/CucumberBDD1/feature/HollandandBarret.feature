Feature:Checking Login and Logout Functionality

  Scenario:Verify/Checking the HollandandBarret login and logout Application
    Given User should open Edge Browser
    When User should Enter Url in Browser
    When User should Navigate Login Page
    And Enter UserName and Password in Edit Box
    And Click on Login Button
    Then Message displayed Login Successfully
    Then User should Close Browser
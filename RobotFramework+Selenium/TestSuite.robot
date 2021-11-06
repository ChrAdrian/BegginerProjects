*** Settings ***
Documentation    Robot Framework with Python and Selenium
Library     SeleniumLibrary

Suite Setup  Log  This is open browser Test
Suite Teardown  Log  This is close browser Test

Test Setup  Log  This is Loggin Test
Test Teardown  Log  This is Logout Test

*** Variables ***
# Scalar variable
${Browser}  Chrome
${URL}  https://opensource-demo.orangehrmlive.com/
# List variable
@{Credentials}  Admin   admin123
# Dictionary variable
&{LoginData}    username=Admin  password=admin123

*** Test Cases ***
TC_001_Login test
    Do Login

TC_002_Log prepaid Test
    Log  This is prepaid Test

TC_003_Log recharge Test
    Log  This is recharge Test

TC_004_Log search Test
    Log  This is search Test

TC_005_Log advanced search Test
    Log  This is Advanced Search Test

*** Keywords ***
Do Login
    open browser    ${URL}  ${Browser}
    maximize browser window
    input text  id:txtUsername     @{Credentials} [0]
    input text  id:txtPassword     &{LoginData} [password]
    click element   id:btnLogin
    close browser
    log     This test in ran by %{username} on %{os}    # Environment variables
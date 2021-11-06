*** Settings ***
Library     SeleniumLibrary

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

*** Keywords ***
Do Login
    open browser    ${URL}  ${Browser}
    maximize browser window
    input text  id:txtUsername     @{Credentials} [0]
    input text  id:txtPassword     &{LoginData} [password]
    click element   id:btnLogin
    close browser
    log     This test in ran by %{username} on %{os}    # Environment variables
*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://opensource-demo.orangehrmlive.com/

*** Test Cases ***
TC_001_Login test
    open browser    ${URL}  ${Browser}
    maximize browser window
    input text  id:txtUsername     Admin
    input text  id:txtPassword     admin123
    click element   id:btnLogin
    close browser

*** Keywords ***

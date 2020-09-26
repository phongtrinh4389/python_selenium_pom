# 1. What is this repository for? ###
This project is a simple automation framework using pytest, selenium, api

# 2. How do I get set up? ###
 - Pull the latest code from repo
 - Go to the root project, run the commands to install all dependencies: 
    pip install -r requirements.txt
 - ".env" file is already in the repo, but in a real project, it should be kept private and do not push into the repo.
    Update your own credentials in that file
 
# 3. How to run tests
Open the cmd from the root folder then follow the below setting to run the test

## 3.1 Run API tests
`pytest -q --disable-warnings tests\api\`

## 3.2 Run UI tests (Local)
Under ./settings/ folder, edit the settings.json file with: "type": "local"
`pytest -q --disable-warnings --browser chrome tests\ui\`
Notes: browser(optional) = [chrome, firefox]. Otherwise, the browser param will be passed from the settings.json file

## 3.3 Run UI tests (Cloud - Browserstack)
Under ./settings/ folder, edit the settings.json file with: "type": "cloud"
`pytest -q --disable-warnings --browser chrome tests\ui\`

## 3.3 Run UI tests (Distributed test - Grid)
- Under ./settings/ folder, edit the settings.json file with: "type": "remote"
- Set up the grid (Hub - slaves) then get the hub address
- Edit settings.json file, for e.g: "remote_url": "http://127.0.0.1:4444/wd/hub"
- Command: `pytest -q --disable-warnings --browser chrome tests\ui\`

## 3.4 Run parallel
`pytest -q --disable-warnings -n 3 --browser chrome tests\ui\`

# Test Report
Check the html report under ./reports/ folder
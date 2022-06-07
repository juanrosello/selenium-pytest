Python & Selenium - Web UI / Test Automation <br />

Test Case: Web Search.<br />
Open DuckDuckGo home page and search for "mekas".<br />
Search results title contains "mekas".<br />
Search result query is "mekas".<br />
Search result links pertain to "mekas".<br />
<br />
Setup:<br />
<br />
Chrome Webdriver<br />
https://chromedriver.chromium.org/downloads<br />
$ sudo mv chromedriver /usr/local/bin<br />
$ export PATH=$PATH:/usr/local/bin/chromedriver<br />
$ chromedriver --version<br />
<br />  
Firefox Webdriver<br />
https://github.com/mozilla/geckodriver/releases/<br />
$ sudo mv geckodriver /usr/local/bin<br />
$ export PATH=$PATH:/usr/local/bin/geckodriver<br />
$ geckodriver --version<br /><br />

$ python3 -m venv venv<br />
$ . venv/bin/activate  <br />
(venv) $ pip --version<br />
(venv) $ pip install --upgrade pip<br />
(venv) $ pip install pytest<br />
(venv) $ pip install selenium<br />
(venv) $ python3 -m pip freeze > requirements.txt<br />
(venv) $ deactivate<br /><br />

Do not commit the venv to github, use it .gitignore<br /><br />

Coverage:<br />
(venv) pip install pytest-cov<br />
(venv)$ python3 -m pytest --cov=<project-name><br /><br />

Generate HTML with coverage:<br />
(venv) $ cd /path/to/code<br />
(venv) $ pytest --cov=<project-name> --cov-report=html <file-name><br />
or:<br />
(venv) $ pytest --cov=<project-name><br />
(venv) $ coverage html<br /><br />

To run Pytest:<br />
(venv) $ python3 -m pytest<br />
(venv) $ python3 -m pytest -v<br />
(venv) $ python3 -m pytest <tests/dir-name/><br />
(venv) $ pytest -v test_search.py<br />
(venv) $ pytest test_search.py<br />

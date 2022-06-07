Python & Selenium - Web UI / Test Automation

Test Case: Web Search.
Open DuckDuckGo home page and search for "mekas".
Search results title contains "mekas".
Search result query is "mekas".
Search result links pertain to "mekas".

Setup:

Chrome Webdriver
https://chromedriver.chromium.org/downloads
$ sudo mv chromedriver /usr/local/bin
$ export PATH=$PATH:/usr/local/bin/chromedriver
$ chromedriver --version
  
Firefox Webdriver
https://github.com/mozilla/geckodriver/releases/
$ sudo mv geckodriver /usr/local/bin
$ export PATH=$PATH:/usr/local/bin/geckodriver
$ geckodriver --version

$ python3 -m venv venv
$ . venv/bin/activate  
(venv) $ pip --version
(venv) $ pip install --upgrade pip
(venv) $ pip install pytest
(venv) $ pip install selenium
(venv) $ python3 -m pip freeze > requirements.txt
(venv) $ deactivate

Do not commit the venv to github, use it .gitignore

Coverage:
(venv) pip install pytest-cov
(venv)$ python3 -m pytest --cov=<project-name>

Generate HTML with coverage:
(venv) $ cd /path/to/code
(venv) $ pytest --cov=<project-name> --cov-report=html <file-name>
or:
(venv) $ pytest --cov=<project-name>
(venv) $ coverage html

To run Pytest:
(venv) $ python3 -m pytest
(venv) $ python3 -m pytest -v
(venv) $ python3 -m pytest <tests/dir-name/>
(venv) $ pytest -v test_search.py
(venv) $ pytest test_search.py

# Integrate
Welcome to Integrate! A testing framework that runs selenium-webdriver and ChromeDriver in a Docker Container

The tests use the python bindings and includes the bare minimum. It includes tests and page objects for both chrome, phantomjs and examples on how to work with sensitive data using environment variables. It also includes a [Dockerfile](https://github.com/shawnshaligram/selenium-python-docker-boilerplate/blob/master/Dockerfile). Implementing this in existing project is easy, just clone this repo and get going!

## Features
 - Sample Page Object Pattern 
 - Sample Selenium Tests 
 - Dockerfile setup
 - Screenshotting Capability
 - More to Come! 

## Usage

- docker run -it -p 4444:4444 shawnshaligram/selenium-webdriver-docker-boilerplate
- Selenium UI is available at: http://DOCKERHOST:4444/wd/hub/static/resource/hub.html
- You should be able to click the "Create session" button and select "Chrome"

## Write tests

Check out [this document](http://www.seleniumhq.org/docs/) for Selenium's concepts and operations.

To write new tests, you can either bind mount your python files to the container or create a new Docker image and copy files into the image.
The example code is located at `tests` and `page_objects` in the container. You may overwrite this file or place your files at different locations.

## Library documentation

Selenium http://www.seleniumhq.org/docs/
ChromeDriver https://sites.google.com/a/chromium.org/chromedriver/
BrowserStack https://www.browserstack.com
Cucumber http://www.rubydoc.info/github/cucumber/cucumber-ruby/
Docker https://docs.docker.com/engine/quickstart/

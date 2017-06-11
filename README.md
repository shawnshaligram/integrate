# WebDriver - Docker Boilerplate

This is a sample repo which runs selenium WebDriver tests inside docker container.
The tests use the python bindings and includes the bare minimum. It includes unittests for both firefox, phantomjs and examples on how to work with sensitive data using environment variables. It also includes a [Dockerfile](https://github.com/shawnshaligram/selenium-python-docker-boilerplate/blob/master/Dockerfile). Implementing this in existing project is easy, just create clone this repro into a folder called seleniumand get going.

## Run example code

The example test querys the keyword "test" at google.com and print the first search result to stdout:

    $ docker run shawnshaligram/webdriver-python

To export screenshots to the ./shots folder on the host computer:

    $ docker run -v $PWD/shots:/screenshots aerofs/webdriver-python

## Write tests

Check out [this document](http://www.seleniumhq.org/docs/) for Selenium's concepts and operations.

To write new tests, you can either bind mount your python files to the container or create a new Docker image and copy files into the image.
The example code is located at `/main.py` in the container. You may overwrite this file or place your files at different locations. For the latter,
run the container as follows:

    $ docker run weihan/webdriver-python python -u /path/to/your/python/code

At the beginning of your code, call `webdriver_util.init()` to set up the
environment and retrieve a few utility objects. Screenshots will be saved at the container's "/screenshots" folder.
You may use bind mount to export them to the host.

    from webdriver_util import init
    driver, wait, selector = init()

`driver` is the Selenium WebDriver object

`wait` is a convenience wrapper around WebDriverWait. Every call to `wait.until*()` methods produce useful console output and a screenshot at the end of the wait.
You can also use `wait.shoot()` at any time to save a screenshot.

`selector` provides shortcuts to `WebDriver.find_element_by_css_selector()`. It restricts element selection to using CSS selectors only.

See [example code](https://github.com/weihanwang/webdriver-python/tree/master/root/main.py) for the usage of these objects.
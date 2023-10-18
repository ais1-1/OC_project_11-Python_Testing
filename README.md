# gudlift-registration
**_This is a project done as part of my degree program at Openclassrooms (project 11: Améliorez une application Web Python par des tests et du débogage)._**

**_The objective of the project is to fix bugs in the project [Python_Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing) and implement Phase 2 with new functionalities. Each functionality and bug fix is in its own branch. Also each new implementation respects TDD._**


1. Why

    This is a proof of concept (POC) project to show a lightweight version of our competition booking platform. The aim is the keep things as light as possible and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages here without affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the Python file. However you do that, you'll want to set the file to be <code>server.py</code>. To do that run the following command in your terminal:
        - On Linux/MacOs: <code>export FLASK_APP=server.py</code>
        - On Windows, 
            1. Command Prompt: <code>set FLASK_APP=server.py</code>
            2. PowerShell: <code>$env:FLASK_APP = "server.py"</code>

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    To run all the tests inside the project you need [pytest](https://docs.pytest.org/en/7.4.x/), [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/) and [locust](https://locust.io/). Also to see how well we're testing you need [coverage](https://coverage.readthedocs.io/en/7.3.2/). These packages are installed in your virtual environment if you use requirements.txt to install.

    * Unit tests and integration tests

        You can run all unit tests and integration tests together by running the following command:

            pytest tests/

        To run only the unit tests run the following command instead:

            pytest tests/unit_tests/
        
        To run the integration tests:

            pytest tests/integration_tests/
        
        To see the test coverage, use the following command:

            coverage report

    * Performance test
    
        To run the performance test server, run the following command:

            locust -f tests/perfomance_tests/locustfile.py
        
        Then go to http://localhost:8089 and enter your options, with 'Host' as the default address of the site (http://127.0.0.1:5000/).

    

6. Naming convention

    This project follows [PEP8](https://peps.python.org/pep-0008/) for Python. It follows the recommendations from [djlint](https://www.djlint.com/docs/getting-started/) for HTML.




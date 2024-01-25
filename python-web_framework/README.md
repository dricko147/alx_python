

Project badge
Python - Web framework - 1

    Master
    By: Guillaume Salva, CTO at Holberton School
    Weight: 1
    Your score will be updated once you launch the project review.
    Project will start Jan 20, 2024 12:00 AM, must end by Jan 25, 2024 11:59 PM

Resources

Read or watch:

    What is a Web Framework?
    A Minimal Application
    Routing (except “HTTP Methods”)
    Rendering Templates
    Synopsis
    Variables
    Comments
    Whitespace Control
    List of Control Structures (read up to “Call”)
    Flask
    Jinja

Recommended YouTube playlist to get you started
Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What is a Web Framework
    How to build a web framework with Flask
    How to define routes in Flask
    What is a route
    How to handle variables in a route
    What is a template
    How to create a HTML response in Flask by using a template
    How to create a dynamic template (loops, conditions…)
    How to display in HTML data from a MySQL database

Requirements
Python Scripts

    Recommended editors: Visual studio code
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7)
    The length of your files will be tested using wc
    All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

HTML/CSS Files

    Recommended editors: Visual studio code
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
    All your CSS files should be in the styles folder
    All your images should be in the images folder
    You are not allowed to use !important or id (#... in the CSS file)
    All tags must be in uppercase
    Current screenshots have been done on Chrome 56.0.2924.87.
    No cross browsers

More Info
Install Flask

$ pip3 install Flask

Introductory session for this project
Live learning session for this project
Tasks
0. Hello Flask!
mandatory

Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 0-hello_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 0-hello_route.py

0/10 pts
1. HBNB
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 1-hbnb_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 1-hbnb_route.py

0/10 pts
2. C is fun!
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 2-c_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in Flask.

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 2-c_route.py

0/10 pts
3. Python is cool!
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 3-python_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in Flask. You can check this out for a clearer understanding

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 3-python_route.py

0/12 pts
4. Is it a number?
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 4-number_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in Flask. You can check this out for a clearer understanding

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 4-number_route.py

0/11 pts
5. Number template
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 5-number_template.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in Flask. You can check this out for a clearer understanding

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 5-number_template.py, templates/5-number.html

0/11 pts
6. Odd or even?
mandatory

Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n is even|odd” inside the tag BODY
    You must use the option strict_slashes=False in your route definition

guillaume@ubuntu:~/AirBnB_v2$ python3 6-number_odd_or_even.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in Python.

Repo:

    GitHub repository: alx_python
    Directory: python-web_framework
    File: 6-number_odd_or_even.py, templates/6-number_odd_or_even.html

0/11 pts
Score
Project badge

Your score will be updated once you launch the project review.

Please review all the tasks before you start the peer review.
Previous project
Copyright © 2024 ALX, All rights reserved.

WEEK ONE

Introduction to Python Web Development
What is Web Development?
Web development is the process of designing, building, and maintaining websites and web applications that are available on the internet. It utilizes a variety of tools, programming languages, and technologies to create websites that serve various functions and purposes.

Web development primarily consists of two main components:

Front-end development focuses on the visual and interactive elements of a website that users directly interact with. It is also referred to as the ‘client side’ of the application. Front-End Developers create everything you see on a web page, including colors, layout, and navigation etc.  Front-end developers work with programming languages such as Javascript, HTML , CSS and their frameworks like Angular ,react, vue, etc


Back-end development, on the other hand, deals with the server-side functionality of a website. It involves creating the logic and infrastructure that support the website’s functionality, handle data processing, and interact with databases. Back-end developers work with programming languages such as Python, Ruby, Java, or PHP to build the server-side components of a web application.


Why use Python for Web Development?
Python is a popular choice for web development due to several reasons:
Multi-Purpose Programming Language: Python is versatile and can be used in various ways, from web applications to desktop applications, cybersecurity, and scientific calculations.
Database Connectivity: Python simplifies establishing database connectivity and can easily interact with major databases such as Oracle, MySQL, PostgreSQL, etc.
Readability and Simplicity: Python’s syntax is designed to be easy to read and write, emphasizing code readability and maintainability.
Large and Active Community: Python has a vast and active community of developers who contribute to its growth and offer support.
Extensive Libraries and Frameworks: Python offers a rich ecosystem of libraries and frameworks that simplify web development tasks.
Scalability and Performance: Python is known for its scalability and performance, making it suitable for handling high-traffic web applications.
Integration and Compatibility: Python seamlessly integrates with other technologies, making it flexible for web development.
Testing and Debugging: Python offers robust testing frameworks, such as unittest and pytest, which simplify the process of writing and executing tests for web applications.
Rapid Development: Python’s focus on simplicity and productivity enables developers to build web applications quickly.
Wide range of third-party libraries and frameworks that extend Python’s capabilities and offer solutions for various web development needs.

In this course, we are going to look at two popular frameworks: Flask and Django. Both of these frameworks are written in Python and are used for web development.

Flask is a micro web framework also written in Python. It does not include any tools or libraries out of the box, giving you the freedom and flexibility to choose your tools and libraries. This makes Flask a great choice for developers who want to have more control over their project.

On the other hand, Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. 


Python and setting up a development environment
The first step to start developing web applications with Python is to install Python on your computer and set up a development environment. A development environment is a set of tools and configurations that allow you to write, run, debug, and test your code. 

There are many options for setting up a Python development environment, but in this course we will use Visual Studio Code, a free and powerful code editor that supports Python and many other languages.and we will install python from the python official website. 

Install Python 
You can install python from the official documentation Download Python | Python.org.
Choose the right version for your OS and download and install it.

For windows, the recommended way to download python is through using the executable file.

Make sure that you add python to PATH, this will allow us to call python in our terminals without having to reference the full file path of where  python installed.

For Linux
Python 2 and python 3 comes installed by default in most of the linux distros, you can update it by running an update on your os.
For debian/ubuntu based distros you can simply run a 
sudo apt update && sudo apt upgrade 


Ubuntu's default repositories do not contain the latest version of Python, but an open source repository named deadsnakes . We can add this to  this repository to the system’s software source and then update

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update


You can now install the latest version of python in this case python3.12.1

sudo apt install python3.12


This should install python on you computer and you should be able to check the version of python by running

python3.12 --version


By default when you call python in the terminal it always points to python2 since some packages depend on this older version of python. To make python command execute Python 3 in a bash shell, you can create an alias in your ~/.bashrc file Here’s how you can do it:
Open the ~/.bashrc file in a text editor. If you’re in the terminal, you can use the nano or vi editor like so:
nano ~/.bashrc

or
code ~/.bashrc


Add the following line to the file:
alias python=python3.12

This line creates an alias that points python to python3.
Save and close the file. If you’re using nano, you can do this by pressing Ctrl + X, then Y to confirm, and Enter to exit.
To make the changes take effect, you need to source your ~/.bashrc file. You can do this with the following command:
source ~/.bashrc


Now, when you type python in your terminal, it should start Python3.12
Please note that this change is local to your user. The system’s version of python will still point to Python 2. This is important because many system scripts still rely on Python 2, and changing the system’s version of python can break these scripts.
For Macos, Just like Linux, macos come installed with python2 but you can install python 3.12 by installing the executable file.Python Releases for macOS | Python.org

You also change the alias by using the ~/.bash_profile or ~/.zshrc if you are using zsh and repeat the same steps as linux. 

Virtual environments & PIP
It is recommended to use a virtual environment to separate your version of python per project and also to manage your packages. As we continue with python virtual environments will become part of our workflow.
What are Virtual environments? 
A virtual environment is a self-contained Python environment that allows you to isolate dependencies and packages for different projects. 
In a nutshell virtual environments help to manage different instances of python, packages/libraries for different projects. Virtual environments help in avoiding conflicts between different project's dependencies and ensure that you're using the right versions of packages. 
There are a number of tools which include python Venv ( comes with python 3.3+ installation ), Pipenv ( combines Venv and pip ), Virtualenv. 
In this case we are going to use venv as it is already inbuilt in python but all the tools have the same features that we will discuss here. 
Creating and Activating a virtual Environment 
To create a virtual environment, run this command in the terminal 
python -m venv <virtual_environment_name> 

To activate the virtual environment we can use these command 
On windows using git bash 
. <virtual_environment_name>/Scripts/activate 

On windows using cmd or powershell. 
<virtual_environment_name>\Scripts\activate 


Note: For Powershell, you may need to set the Execution Policy if it shows an error 
Set-ExecutionPolicy Unrestricted -Scope Process 


On Linux and Macos using BASH 
. <virtual_environment_name>/bin/activate 

Deactivate the Virtual Environment 
deactivate 




Pip - Python Package Manager 
Pip Pip stands for “Pip Installs Packages”.It is a package-management system used to install and manage software packages written in Python. These packages contain all the files necessary for a module and are published on the Python Package Index (PyPI), a repository of software for the Python programming language. If you have Python version 3.4 or later, pip is included by default

Using pip to Manage Python Packages
Note: Always create virtual environment if you are going to install any pip package 
Installing Packages with Pip 

Install a package
pip install package_name 


Install a Specific Version 
pip install package_name=version_number 


List installed packages 
pip list 


List installed packages in a requirements format
pip freeze 


Creating a requirements.txt file from pip freeze is a common practice in Python development. This file is used to keep track of the Python packages required to run your project. 
Make sure your virtual environment is active and run this command. 
pip freeze > requirements.txt


This will create a requirement.txt file in the current directory which will have the list of the packages installed.


Uninstall Package 
pip uninstall package_name 


Introduction to http requests
At a fundamental level, when you visit a website, your browser makes an HTTP (Hypertext Transfer Protocol.) request to a server. Then that server responds with a resource (an image, video, or the HTML of a web page) -  which your browser then displays for you.
This is HTTP's message-based model. Every HTTP interaction includes a request and a response.
By its nature, HTTP is stateless.
Stateless means that all requests are separate from each other. So each request from your browser must contain enough information on its own for the server to fulfill the request. That also means that each transaction of the message based model of HTTP is processed separately from the others.

URLs
The URL (Uniform Resource Locator) is probably the most known concept of the Web. It is also one of the most important and useful concepts. A URL is a web address used to identify resources on the Web.
The idea of the web is structured around resources. From its beginnings the Web was the platform for sharing text/HTML files, documents, images etc, and as such it can be considered a collection of resources.
Example of an URL

Protocol — Most often they are HTTP  (or HTTPS for a secure version of HTTP).

Other notable protocols are:
File Transfer Protocol (FTP) — is a standard protocol used for transferring files between a client and a server over a network.
Simple Mail Transfer Protocol (SMTP) is a standard for email transmission.

Domain — Name that is used to identify one or more IP addresses where the resource is located.
Path —Specifies the resource location on the server. It uses the same logic as a resource location used on the device where you are reading this article (i.e. /search/cars/VWBeetle.pdf or C:/my cars/VWBeetle.pdf).
Parameters — Additional data used to identify or filter the resource on the server.

Note: When searching for articles and more information about HTTP, you may encounter the term URI (or uniform resource identifier). URI is sometimes being used instead of URL but mostly in formal specifications and by people who want to show off. 😀
HTTP Requests
In HTTP, every request must have an URL address. Additionally, the request needs a method. The four main HTTP methods are:
GET
PUT
POST
DELETE

We will expand more on  these methods, and more, in the HTTP Methods section .
And these methods directly correspond to actions:
Read
Update 
Create 
Delete 

All HTTP messages have one or more headers, followed by an optional message body. The body contains the data that will be sent with the request or the data received with the response.

The first part of every HTTP request holds three items:
Example:
GET /adds/search-result?item=vw+beetle HTTP/1.1
When a URL contains a “?” sign, it means it contains a query. That means it sends parameters of the requested resource.
The first part is a method which tells which HTTP method is used. Most commonly used is the GET method. GET method retrieves a resource from the web server and since GET doesn’t have a message body nothing after the header is needed.
The second part is a requested URL.
The third part is a HTTP version being used. Version 1.1. is the most common version for most browsers, however, version 2.0 is taking over.

There are also some other interesting things in an HTTP request:
Referer header — tells the URL from where the request has originated.
User-Agent header — additional information about the browser being used to generate the request.
Host header — uniquely identifies a host name; it is necessary when multiple web pages are hosted on the same server.
Cookie header — submits additional parameters to the client.

HTTP Responses
Just like in HTTP requests, HTTP responses also consist of three items:
Example:
HTTP/1.1 200 OK
The first part is the HTTP version being used.
The second part is the numeric code of the result for the request.
The third part is a textual description of the second part.

There are some other interesting things in an HTTP response:
Server header — information about which web server software is being used.
Set-Cookie header — issues the cookie to the browser.
Message body — it is common for an HTTP response to hold a message body.
Content-Length header — tells the size of the message body in bytes.
HTTP Methods
The most common methods are GET and POST. But there are a few others, too.
GET —  You use this method to request data from a specified resource where data is not modified it in any way. GET requests do not change the state of resources.
POST — You use this method to send data to a server to create a resource.
PUT — You use this method to update the existing resource on a server by using the content in the body of the request. Think of this as a way to "edit" something.
HEAD —  You use this method the same way you use GET, but with the distinction that the return of a HEAD method should not contain body in the response. But the return will contain the same headers as if GET was used. You use the HEAD method to check whether the resource is present prior to making a GET request.
TRACE — You use this method for diagnostic purposes. The response will contain in its body the exact content of the request message.
OPTIONS — You use this method to describe the communication options (HTTP methods) that are available for the target resource.
PATCH —  You use this method to apply partial modifications to a resource.
DELETE —You use this method to delete the specified resource.
REST
Representational state transfer (REST) is an architecture style where requests and responses contain representations of the current state of the system's resource.

“Regular” way:
http://example.com/search?make=wv&model=beetle
REST-style:
http://example.com/search/vw/beetle

You can learn more about REST here if you're curious.
HTTP Headers
There are three main components that make up the request/response structure. These include:
First line
Headers
Body/Content
We already talked about the first line in HTTP requests and responses, and body function was mentioned too. Now we'll talk about HTTP headers.


The HTTP headers are added after the first line and are defined as name:value pairs separated by a colon. HTTP headers are used to send additional parameters along with the request or response.


As I already said, the body of the message includes the data to be sent with the request or the data received along with the response.
There are different types of headers that are grouped based on their usage into 4 broad categories:
General header — Headers that can be used in both requests and response messages and that are independent of the data being exchanged.
Request header — These headers define parameters for the data requested or parameters that give important information about the client making the request.
Response header — These headers contain information about the incoming response.
Entity header — The entity headers describe the content that makes up the body of the message.

Types of headers

HTTP status codes
Browsing the web, you may have encountered "404 error: not found" pages or "500 errors: server is not responding" pages.These are HTTP status codes.


Every HTTP response message must contain an HTTP status code in its first line, telling us the result of the request.

There are five groups of status codes which are grouped by the first digit:
1xx — Informational.
2xx — The request was successful.
3xx — The client is redirected to a different resource.
4xx — The request contains an error of some kind.
5xx — The server encountered an error fulfilling the request.

Here's a full list of HTTP Status Response Codes and their explanation.
HTTPS (Hypertext Transfer Protocol Secure)
The secure version of HTTP protocol is HyperText Transfer Protocol Secure (HTTPS). HTTPS provides encrypted communication between a browser (client) and the website (server).
In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS) or Secure Sockets Layer (SSL).
The protocol is therefore also often called HTTP over TLS, or HTTP over SSL.
Both the TLS and SSL protocols use an asymmetric encryption system. Asymmetric encryption systems use a public key (encryption key) and a private key (decryption keys) to encrypt a message.
Anyone can use the public key to encrypt a message. However, private keys are secret, and that means that only the intended receiver can decrypt the message.

Example of asymmetric encryption system




SSL/TLS handshake
When you request a HTTPS connection to a website, the website sends its SSL certificate to your browser. That process where your browser and website initiate communication is called the “SSL/TLS handshake.”

The SSL/TLS handshake involves a series of steps where browser and website validate each other and start communication through the SSL/TLS tunnel.
As you probably noticed, when a trusted secure tunnel is used during a HTTPS connection, the green padlock icon is displayed in the browser's address bar.
Example of one of my secure pages
Benefits of HTTPS
The major benefits of a HTTPS are:
Customer information, like credit card numbers and other sensitive information, is encrypted and cannot be intercepted.
Visitors can verify you are a registered business and that you own the domain.
Customers know they are not supposed to visit sites without HTTPS, and therefore, they are more likely to trust and complete purchases from sites that use HTTPS.


Week One Assignment 📝
 Install python on your computer if your haven’t
Create virtual environment and install any package and use of your choice
Breakdown the necessary HTTP request for a blog application, What kind of request does each part of the application do.
Practice some python algorithms to get more familiar with python syntax. (will be shared)












WEEK TWO

Week Two: Introduction to Flask
Understanding Flask framework
Creating a basic Flask project
Handling HTTP requests and responses in Flask



Introduction to Flask
Flask is a Python microframework that provides useful tools and features that make creating web applications in Python easier.  Flask is classified as a microframework because it adheres to a simple philosophy of keeping things simple and lightweight. 

It only provides the core features of a web framework , gives you flexibility on how you handle database abstraction, is highly extensible and has a large compatibility with different versions of python.

Installation
To get started with Flask, you need to  set up your development environment and install flask

Create virtual environment in your project_folder
python -m venv env


Activate virtual environment 
. env/bin/activate 


Install flask
pip install flask


Add flask to requirements.txt
pip freeze > requirements.txt


Open project in vscode
code flaskapp


Creating a  Flask Application
To create a Flask application, you can start by creating  a file python file for example server.py: a then you can import flask and create a simple route. Code example: below.
from flask import Flask
app = Flask(__name__)

# route for "/"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# route for "/about"
@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == '__main__':
    app.run()


To run the application, use the flask command or python -m flask. You need to tell Flask where your application is with the --app option.
flask --app server run

As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app. You also just run the python file 
python server.py 


This launches a very simple builtin server, which is good enough for testing but 


You can now visit http://127.0.0.1:5000/ to view your application. 
If another program is already using port 5000, you’ll see OSError: [Errno 98] or OSError: [WinError 10013] when the server tries to start. You can pass a port number using --port like flask --app server.py run --port 8000

Let us explore what each line does:


from flask import Flask

This line imports the Flask class from the flask module. The Flask class is the main entry point to any Flask web application.
app = Flask(__name__)

Here, we create an instance of the Flask class and assign it to the variable app. The __name__ argument is a special variable in Python, which gets as value the string __main__ when you’re executing the script, and the name of the module when you’re importing it. 

@app.route('/') and @app.route('/about')

These lines are decorators that Flask provides to assign URLs in our app to functions easily. They associate the given URL paths ('/' and '/about') to the respective functions (index() and about()).

def hello_world():
    return 'Hello, World!'

This is a view function. When a user visits the main URL (‘/’), the hello_world function is called and the string ‘Hello, World!’ is returned, which is then displayed on the user’s browser.
When a user visits the root URL ('/'), the index() function displays a welcome message. Visiting '/about' displays information about the site.
if __name__ == '__main__':
    app.run()



This is a conditional that is true if the script was run directly from the Python interpreter. app.run() is executed only if the script is run directly. This launches Flask's built-in web server, which starts listening for incoming HTTP requests.
Debug Mode
The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.
if __name__ == '__main__':
    app.run(debug=True)



We can pass the debug variable app.run method to activate this or we can run the flask app using the --debug option flask --app server run --debug
if __name__ == '__main__':
    app.run(debug=True)


Note: The debug mode should only be used in the development environment and when you deploy your application, you should turn off debug mode as it poses security risks.
Unique URLs / Redirection Behavior
URLS will behave different based on whether they have a trailing slash (/) or not:

Route with a Trailing Slash:
@app.route('/posts/')
def posts():
    return 'The posts page'

Behavior: This route's canonical or standard URL (/posts/) ends with a trailing slash. Conceptually, it's akin to a folder in a file system, implying that accessing /projects (without a trailing slash) should redirect to the standard URL /prosts/.
Accessing /posts  (without trailing slash) would automatically redirect to /posts/ (with trailing slash), maintaining a consistent canonical URL for the project page.

Route without a Trailing Slash:
@app.route('/about')
def about():
    return 'The about page'

Behavior: This route's standard URL (/about) does not have a trailing slash.
 Conceptually, it's akin to the pathname of a file, suggesting that accessing /about/ (with a trailing slash) should not match this route.
 Accessing /about/ (with trailing slash) would result in a 404 "Not Found" error since the route specifically does not include a trailing slash in its definition.

Creating a Flask Project with Dynamic Routes
Flask supports dynamic routes by using variable parts in the URL. These variable parts act as placeholders in the URL, enabling the application to capture and utilize values from the URL dynamically. This feature is particularly useful when building applications that need to handle various inputs or requests for different resources. For example http://12.0.0.1:500/posts/1 , we want to get the post with id of 1, and when we replace 1 with 2, we should get the post of id 2.
Using Variable Parts in URLs:
To create a dynamic route in Flask, we can define variable parts in the URL by enclosing them within < >.
The variable part is specified with a converter type (like string, int, float, path and UUID.) that determines the type of data the variable should match.
Here's an example of a dynamic route for viewing specific blog posts:
from flask import Flask

app = Flask(__name__)

# Define a dynamic route for viewing blog posts by post ID
@app.route('/post/<int:post_id>')
def view_post(post_id):
    # Logic to retrieve and display the blog post with the given post_id
    return f"Viewing Blog Post #{post_id}"


In the route /post/<int:post_id>, <int:post_id> specifies a dynamic part in the URL, indicating that post_id should be an integer.
The view_post() function takes the post_id as an argument and displays the blog post corresponding to that ID. 

URL Building
Flask provides a function url_for()  used for generating URLs dynamically based on endpoint names and associated arguments. Each function is associated with a url for example def about  is related to /about/ url.
Take an example of a user_proflie that accepts a variable username

@app.route('/user/<username>')
def user_profile(username):
    # Logic to display user profile based on username
    return f'profile.html, {username=username}'


We can generate a url using url_for.
from flask import url_for

# Generating a URL for user_profile endpoint with username 'alice'
url = url_for('user_profile', username='alice')
print(url)  # Output: /user/alice


We will look at this further when exploiting templates but the main reasons for using the url_for reverse function are:
Reversing is often more descriptive than hard-coding the URLs.
You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.
URL building handles escaping of special characters transparently.
The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.

Extracting Dynamic Route Values:
When a request is made to a URL with a dynamic part, Flask captures the value of that part and passes it as an argument to the associated view function.
For instance, when a user accesses /post/123, Flask extracts 123 as the value for post_id and passes it to the view_post() function.

Dynamic routes are versatile and allow applications to respond dynamically based on the values present in the URL. They can be used for various purposes such as displaying specific content, accessing resources by ID, or implementing search functionalities.
HTTP Methods
As we have discussed earlier, Web applications use different HTTP methods when accessing URLs. By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods such as GET, POST, PUT, DELETE, etc.

 GET Method
The GET method is used for retrieving data and resources from the server.
@app.route('/articles', methods=['GET'])
def get_articles():
    # Logic to fetch and display articles


POST Method
The POST method is used for sending data to the server to create or update a resource.
@app.route('/articles/create', methods=['POST'])
def create_article():
    # Logic to create a new article



PUT Method

The PUT is used to update or replace an existing resource.
@app.route('/articles/update/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    # Logic to update the article with the given ID


  DELETE Method
The DELETE is used to delete a resource identified by a specific URL.
@app.route('/articles/delete/<int:article_id>', methods=['DELETE'])
    def delete_article(article_id):
        # Logic to delete the article with the given ID


  PATCH Method

PATCH is  Similar to PUT but is used for making partial updates to a resource.
@app.route('/articles/edit/<int:article_id>', methods=['PATCH'])
def edit_article(article_id):
    # Logic to partially update the article with the given ID



 Other HTTP Methods
Flask also supports other HTTP methods such as OPTIONS, HEAD, TRACE, etc., but they might not be as commonly used in web applications.

You can also pass Multiple methods and handle each different in the same route
@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        # Logic to fetch user details
    elif request.method == 'PUT':
        # Logic to update user details
    elif request.method == 'DELETE':
        # Logic to delete user


The route `/user/<int:user_id>` supports multiple HTTP methods, allowing different actions on the user resource.
 Importance of Handling Different HTTP Methods in Flask:
RESTful API Design: Flask allows the creation of RESTful APIs by handling different HTTP methods for CRUD (Create, Read, Update, Delete) operations.
 Flexibility: Different methods allow distinct functionalities for the same URL endpoint.
 Correctness: Adhering to HTTP standards ensures proper interaction with resources.


Handling HTTP Requests and Responses in Flask
At the core of any backend, we want to deal and manage the different types of requests made by clients (such as web browsers or other applications) and generate appropriate responses based on these requests. Flask provides functionalities to access request data and create various types of responses
Handling HTTP requests and responses in Flask involves managing the different types of requests made by clients (such as web browsers or other applications) and generating appropriate responses based on these requests. Flask provides functionalities to access request data and create various types of responses.

The request object 
The request object in Flask provides access to information about incoming HTTP requests, including form data, request headers, query parameters, file uploads, and more. It's a crucial component for handling and processing user input in web applications. 

Let's explore the `request` attributes with examples for different functionalities:
Accessing Request Attributes:
Request Method (request.method):
This attribute holds the HTTP method used in the request (e.g., GET, POST, PUT, DELETE).
from flask import request

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
        # Handle POST request
        pass
    else:
        # Handle GET request
        pass


Accessing Form Data (request.form):
Used to access form data submitted via POST or PUT requests.

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Process the form data


Accessing URL Parameters (request.args):
Fetches query parameters from the URL (e.g., example.com?key=value)
@app.route('/search')
def search():
    search_word = request.args.get('key', '')
    # Process the search word parameter



Accessing JSON Data (request.json):

Used to access JSON data sent in the request body.
@app.route('/json_data', methods=['POST'])
def json_data():
    data = request.json
    # Process JSON data received




Accessing File Uploads (request.files):
Handles file uploads sent as part of a request.
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        # Process the uploaded file
Accessing Cookies (request.cookies):


Retrieves cookies sent with the request.

@app.route('/cookies')
def cookies():
    user_id = request.cookies.get('user_id')
    # Use the user_id retrieved from cookies

A Table of some of the attributes the request Object used to handle different requests
Request Attribute
Description
Use Case
request.method
Holds the HTTP method used in the request (e.g., GET, POST, PUT).
Differentiates between various HTTP methods for request handling.
request.form
Provides access to form data sent via POST or PUT requests.
Processing form submissions; accessing form fields.
request.args
Fetches query parameters from the URL (e.g., example.com?key=value).
Handling URL parameters passed in the query string.
request.json
Accesses JSON data sent in the request body.
Processing JSON data transmitted to the server.
request.files
Handles file uploads sent as part of a request.
Uploading and processing files submitted through forms.
request.cookies
Retrieves cookies sent with the request.
Accessing and using cookies sent by the client.
request.headers
Provides access to the request headers.
Handling various header information like User-Agent.
request.path
Returns the path part of the URL.
Extracting the path to perform specific actions based on the URL route.
request.url
Returns the complete URL of the request.
Obtaining the full URL to perform specific operations based on the request’s URL.
request.endpoint
Holds the endpoint name to which the request was dispatched.
Identifying the endpoint to customize behavior based on the requested route.
request.remote_addr
Retrieves the remote IP address of the client making the request.
Logging or tracking IP addresses for security or analytical purposes.
request.scheme
Returns the URL scheme (e.g., ‘http’, ‘https’) used in the request.
Distinguishing between HTTP and HTTPS requests for different processing logic.
request.full_path
Returns the full path and query string of the request.
Retrieving the complete path including the query string parameters.
request.script_root
Retrieves the root path of the script without the path of the server.
Creating URLs relative to the application root.


 Generating HTTP Responses:
The return value from a view function is automatically converted into a response object for you. If the return value is a string it’s converted into a response object with the string as response body, a 200 OK status code and a text/html mimetype. If the return value is a dict or list, jsonify() is called to produce a response. The logic that Flask applies to converting return values into response objects is as follows:
If a response object of the correct type is returned it’s directly returned from the view.
If it’s a string, a response object is created with that data and the default parameters.
If it’s an iterator or generator returning strings or bytes, it is treated as a streaming response.
If it’s a dict or list, a response object is created using jsonify().
If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form (response, status), (response, headers), or (response, status, headers). The status value will override the status code and headers can be a list or dictionary of additional header values.
If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a response object.

Returning Responses:
 Returning HTML Content: Render HTML content to be displayed in the browser.
@app.route('/')
def index():
    return '<h1>Welcome to my Flask App</h1>'



 Returning JSON Data: Return JSON-formatted data as a response, commonly used for APIs.
from flask import jsonify
@app.route('/api/data')
def get_data():
        data = {'key': 'value'}
        return jsonify(data)

 

Redirecting to Another URL: Redirect the user to a different URL.

from flask import redirect, url_for


@app.route('/old-url')
def old_url():
        return redirect(url_for('new_url'))


If you want to get hold of the resulting response object inside the view you can use the make_response() function
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = "Cookie Set!"
    resp = make_response(response)
    resp.set_cookie('user_id', '123')
    resp.headers['Custom-Header'] = 'Custom Value'
    return resp





Week Two Assignment 📝
Create a new flask application
Implement Logic for a blog application 
Extend the basic Flask app to include multiple routes handling different URLs and HTTP methods.
Implement a route that returns JSON data as a response


WEEK THREE
Week Three: Flask Basics
Configuring routes and views in Flask
Working with templates
Serving static files and understanding request/response objects
Rendering HTML and working with templates
We saw in our previous examples that we can return html in the return function of our route functions but in most cases we want to work with html files. Flask provides a render_template() helper function that allows us to return html files and also allows us to use the Jinja template engine (Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax.). This makes managing HTML much easier by writing your HTML code in .html files as well as using python logic in your HTML code. Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, and anything else
Rendering HTML
from flask import render_template

@app.route("/")
def hello_world():
    return render_template("index.html")



We are returning an html file called index.html, we need to create. Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

Case 1: a module:
/application.py
/templates
    /hello.html


Case 2: a package:
/application
    /__init__.py
    /templates
        /hello.html


We can also define data variables that can be read by jinja in the template. For example
@app.route("/blog")
def blog():
    # Assume blog_posts is a list of dictionaries representing blog posts
    blog_posts = [
        {"id": 1, "title": "First Post", "content": "Content of the first post."},
        {"id": 2, "title": "Second Post", "content": "Content of the second post."}
        # More posts...
    ]
    return render_template("blog.html", posts=blog_posts)


 render_template() function renders an HTML template (blog.html) and passes data to it (posts=blog_posts).
Templating with Jinja
Jinja templates in Flask provide a robust mechanism for creating dynamic and reusable HTML content, allowing developers to craft flexible and maintainable web applications.
A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). A Jinja template doesn’t need to have a specific extension: .html, .xml, or any other extension is just fine.

A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

From the previous example we can  jinja to access the data of posts
<!-- blog.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>Welcome to My Blog!</h1>
    <ul>
        {% for post in posts %}
            <li><a href="/post/{{ post.id }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>


{% for post in posts %} , {{ post.title }} , {{ post.id }} and   {% endfor %} are Jinja2 templating syntax to iterate over posts and display post titles dynamically.

There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:
{% ... %} for Statements, these must have a closing delimiter/tag
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output


Jinja2 also provides various tags that control the logic and structure of templates. Here's a list of commonly used Jinja tags along with their use cases:

Jinja Tag
Use Case
{% if condition %} ... {% endif %}
Implements conditional statements based on a specified condition.
{% for item in iterable %} ... {% endfor %}
Iterates over elements in an iterable (list, dict, etc.) to perform repetitive actions.
{% while condition %} ... {% endwhile %}
Executes a block of code repeatedly while a condition is true.
{% else %} and {% elif condition %}
Provides alternate conditions or branches for {% if %} statements.
{% extends 'base.html' %}
Inherits a parent template for child templates, enabling template inheritance.
{% block block_name %} ... {% endblock %}
Defines sections that can be overridden by child templates extending a base template.
{{ variable }}
Outputs the value of a variable within the template.
{% set variable = value %}
Assigns a value to a variable within the template.
{% comment %} ... {% endcomment %}
Inserts comments within templates that are not rendered in the output.
{% macro name(parameters) %} ... {% endmacro %}
Defines a reusable block of code (macro) that can be called within the template.
{{ name(parameters) }}
Invokes a macro, passing specific arguments if required.
`{{ variable | filter_name }}`
signifies the application of a filter to the variable's value before it's displayed in the template
{% include 'template.html' %}
Includes content from another template within the current template.
{% raw %} ... {% endraw %}
Treats enclosed content as raw text, bypassing Jinja parsing.
{% trans %} ... {% endtrans %}
Marks content for translation to support internationalization.


:
 Template Inheritance:
We can create a base HTML template (base.html) that establishes the fundamental structure shared across multiple pages. This template outlines the overall layout, including sections for the header, navigation links, main content, and footer. Using {% block %} tags, we can define areas where specific content can be inserted or overridden by child templates.
<!-- Base Template (`base.html`): -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %} - My Blog</title>
</head>
<body>
    <header>
        <h1>Welcome to My Blog</h1>
        <!-- Navigation links -->
        <a href="{{ url_for('index') }}">Home</a>
        <a href="{{ url_for('create_post') }}">New Post</a>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
       © 2023 My Blog
    </footer>
</body>




 Child Template (`index.html`, extends `base.html`):
In a child template like index.html, we use the {% extends %} tag to inherit the structure from the base.html template. Within this child template, we override the {% block %} content defined in the base template. For instance, we replace the title block and insert content specific to the index page, such as displaying a list of blog posts.
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <!-- Display list of blog posts -->
    <h2>Latest Posts</h2>
    <ul>
        {% for post in posts %}
            <li><a href="{{ url_for('view_post', post_id=post.id) }}">{{ post.title }}   
                 </a></li>
        {% endfor %}
    </ul>
{% endblock %}


Including snippets
Including Jinja templates within other templates in Flask can be done using the {% include %} tag. This is useful when you have reusable components or snippets of HTML that you want to include across multiple templates. Assume you have a navbar.html file containing the navigation bar HTML
<nav>
    <ul>
        <li><a href="{{ url_for('index') }}">Home</a></li>
        <li><a href="{{ url_for('posts') }}">All Posts</a></li>
        <li><a href="{{ url_for('about') }}">About</a></li>
        <!-- Other navigation items -->
    </ul>
</nav>

Now, you want to include this navigation bar across different pages of your blog application.
For example, in your base.html template (the base layout template used across multiple pages), you can include the navigation bar using the {% include %} tag:
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <!-- Add your CSS and other common head elements -->
</head>
<body>

    {% include 'navbar.html' %}

    <main class="content">
        {% block content %}{% endblock %}
    </main>

    <!-- Other common footer elements -->

</body>
</html>


You can create different snippets  like footers, auth-Messages ,etc
 Template Variables and Control Structures:

We utilize template variables like {{ post.title }}, which are placeholders dynamically replaced with actual content when the template is rendered. Using  control structures like {% if %}, we conditionally display elements based on certain criteria. For example, we conditionally render edit and delete buttons if a user is authenticated, providing different views based on user permissions.

{% extends 'base.html' %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <article>
        <h2>{{ post.title }}</h2>
        <p>Published on: {{ post.date }}</p>
        <p>{{ post.content }}</p>
        <!-- Edit and Delete buttons (if user is authenticated) -->
        {% if user_authenticated %}
            <a href="{{ url_for('edit_post', post_id=post.id) }}">Edit</a>
            <a href="{{ url_for('delete_post', post_id=post.id) }}">Delete</a>
        {% endif %}
    </article>
{% endblock %}



Template Filters and Functions:
We define a custom function in a separate Python file (helpers.py), which we register as a template filter using @app.template_filter. This function formats dates using strftime() and returns the formatted date string

from flask import Flask, render_template
from jinja2 import Markup
import datetime

app = Flask(__name__)

@app.template_filter('format_date')
def format_date(date):
    return date.strftime('%B %d, %Y')

app.jinja_env.globals.update(format_date=format_date)

# Routes and logic for rendering templates...


Within the template (post.html), we can apply the custom date formatting filter using {{ post.date | format_date }}. This filters the post.date variable through our custom format_date filter function, allowing us to display the date in the desired format.
<!-- Usage in Template (`post.html`) -->:

<p>Published on: {{ post.date | format_date }}</p>



Conditional Rendering and Looping:
In the profile.html template, we can implement conditional rendering using {% if %} statements to display different content based on the availability of user information.
<!-- Profile (`profile.html`):-->

{% extends 'base.html' %}

{% block title %}{{ username }}'s Profile{% endblock %}

{% block content %}
    <h2>{{ username }}'s Profile</h2>
    {% if user_info %}
        <p>Email: {{ user_info.email }}</p>
        <p>Joined on: {{ user_info.join_date | format_date }}</p>
        <!-- Other user details -->
    {% else %}
        <p>No profile found for {{ username }}</p>
    {% endif %}
{% endblock %}


Inside templates you also have access to the config, request, session and g [1] objects as well as the url_for() and get_flashed_messages() functions. 
config: Flask's config object holds configuration variables defined in your application. These could include settings for the application, database connections, secret keys, etc.

request: The request object contains information about the current HTTP request, including form data, headers, cookies, etc.

session: The session object allows you to store information across requests for a specific user. It uses cookies to keep track of the session data.

g: The g object (context global) is used to store global variables during a request. It's generally used to pass data between functions during a single request.

url_for(): The url_for() function generates URLs for specific routes in your application. It generates the URL dynamically based on the endpoint.

get_flashed_messages(): This function retrieves flashed messages stored in the session. Flashed messages are typically used to show one-time messages (e.g., success or error messages) to users.
An Example
app.py 
from flask import Flask, render_template, request, session, g, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Accessing config variables
    app.config['APP_NAME'] = 'My Awesome App'
    
    # Accessing request information
    request_method = request.method
    
    # Storing and accessing session data
    session['user'] = 'JohnDoe'
    
    # Storing and retrieving data using g object
    g.some_data = 'Hello, World!'
    
    # Flashing messages
    flash('Welcome to the homepage!')

    return render_template('index.html')


index.html 
<!DOCTYPE html>
<html>
<head>
    <title>{{ config['APP_NAME'] }}</title>
</head>
<body>
    <h1>Welcome to {{ config['APP_NAME'] }}</h1>
    
    <!-- Displaying request information -->
    <p>Request Method: {{ request_method }}</p>
    
    <!-- Accessing session data -->
    {% if session['user'] %}
        <p>Welcome, {{ session['user'] }}!</p>
    {% else %}
        <p>Please log in</p>
    {% endif %}
    
    <!-- Accessing and displaying data from g object -->
    <p>Data from g object: {{ g.some_data }}</p>
    
    <!-- Generating URLs using url_for() -->
    <a href="{{ url_for('index') }}">Home</a>
    <a href="{{ url_for('login') }}">Login</a>
    
    <!-- Displaying flashed messages -->
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                <p>{{ message }}</p>
            {% endfor %}
        {% endif %}
    {% endwith %}
</body>
</html>

Static files
In a Flask web application, static files such as CSS stylesheets, JavaScript files, images, and other resources are served separately from the dynamic content. These files remain constant and are typically used to style the web pages or add interactive elements. Flask provides a built-in way to serve these static files using the static folder within your application directory.

Folder structure
/myapp
    /static
        /css
            styles.css
        /js
            script.js
        /images
            logo.png
    /templates
        index.html
    app.py


Using Static Files in a Template
In your HTML templates (e.g., base.html), you can link these static files using special URL patterns generated by Flask's url_for() function. This function generates the correct URL for a static file based on the folder structure.
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <!-- Linking to the CSS file in the static folder -->
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
    <!-- Including an image from the static/images folder -->
    
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    <!-- Linking to the JavaScript file in the static folder -->
</body>
</html>


Flash Messages
flash and get_flashed_messages are components of Flask's message flashing system, which allows temporary messages to be stored and accessed across requests. These messages are usually used to convey status or error messages to users after a specific action, like logging in, registering, or updating information.
Creating a flash message
from flask import flash

@app.route('/login', methods=['POST'])
def login():
    # Your authentication logic here
    if authentication_successful:
        flash('Login successful!', 'success')
    else:
        flash('Invalid credentials. Please try again.', 'error')



Using Flashed Messages in Templates
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}


get_flashed_messages(with_categories=True): Retrieves flashed messages with their categories.
{% with messages = ...: Assigns the flashed messages to a variable named messages.
{% if messages %}: Checks if there are any flashed messages.
{% for category, message in messages %}: Iterates through each flashed message and its category.
<div class="alert alert-{{ category }}">{{ message }}</div>: Renders each message in an appropriate HTML format (you can customize this to suit your CSS framework).


Week Three Assignment 📝
Use templates for your blog application
Create the different html pages for the different parts of your blog application 
Use the jinja2 to dummy display data for these templates
Add styling in your blog application using static files, you can choose a framework like bootstrap for styling

WEEK FOUR
Week Four: Middleware and Extensions in Flask
Exploring middleware functions and their usage in Flask
Using Flask extensions for various functionalities (e.g., authentication, forms)
Flask Extensions
Flask extensions are additional libraries that enhance the functionality of a Flask application by providing pre-written, reusable components. These extensions cover a wide range of functionalities, from database management to authentication, making it easier for developers to add advanced features to their applications without reinventing the wheel.

Types of Flask Extensions:
Database Management: Examples include Flask-SQLAlchemy, Flask-Migrate for handling databases, and Flask-MongoEngine for MongoDB.
Authentication and Authorization: Flask-Login, Flask-Security for user authentication and authorization.
Form Handling: Flask-WTF for form creation and validation.
RESTful APIs: Flask-RESTful for building REST APIs.
Caching: Flask-Cache for caching data and responses.
File Uploads: Flask-Uploads for handling file uploads.
Testing: Flask-Testing for testing Flask applications.
Admin Panels: Flask-Admin for creating admin interface

These extensions are built to work with each other and don’t have a lot of conflicts and we will be using some of them to make it easier to build our application.
Forms with Flask-WTF
 Flask-WTF is a Flask extension that simplifies the creation and handling of web forms in Flask applications. Flask-WTF simplifies form creation, validation, and rendering in Flask applications. Flask-WTF uses wtforms under the food and makes it easier to use it in flask
We can install flask-wtf 
pip install Flask-WTF


Import and Initialize Flask-WTF in Your Flask App:
Add a secret_key config required to use CSRF.
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key


Create a Form Class using Flask-WTF:
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Post')


Define a Route to Handle Blog Post Creation
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        # Process form data and create a new blog post        
        # Perform further actions (e.g., database operations)
        return redirect(url_for('index'))  # Redirect to the home page after creating the post
    return render_template('create_post.html', form=form)


Create a Template (create_post.html) to Render the Form
<!-- create_post.html -->

    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=40) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>
            {{ form.body.label }}<br>
            {{ form.body(rows=10, cols=40) }}<br>
            {% for error in form.body.errors %}
                <span style="color: red;">{{ error }}</span><br>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>




Adding Classes and other attributes to Flask-WTF Form Fields:
To add CSS classes or custom styling to Flask-WTF you can apply classes directly within the form field definitions or within the HTML templates where you render the form fields. Flask-WTF allows you to specify classes or add custom attributes to form fields.
 Adding Classes Directly to Form Field Definitions:
You can include `render_kw` parameter while defining the form fields to add classes or custom attributes:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', render_kw={"class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


  Applying Classes in HTML Templates:
When rendering the form fields in HTML templates, you can manually add classes:


<!-- using Jinja2 template to render Flask-WTF form fields -->
<form method="POST">
    {{ form.hidden_tag() }}
    <div class="form-group">
        {{ form.name.label }}
        {{ form.name(class="form-control") }}
    </div>
    <div>
        {{ form.submit(class="btn btn-primary") }}
    </div>
</form>



Database with Flask-SQLAlchemy
Flask supports various databases through different extensions like SQLAlchemy (for SQL databases), Flask-SQLAlchemy, Flask-MySQL, Flask-PyMongo (for MongoDB), etc. In our case we are going to focus on mostly SQL databases and the use of Flask-SQLAlchemy as it is a very popular approach for most flask applications.

Installation
pip install Flask-SQLAlchemy



Define Database Models
Create Python classes that represent tables in your database. Each class will be a model mapped to a table in the database and  with its fields mapped to database columns.
# models.py


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # instance of SQLAlchemy to define the models

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.author}', '{self.date_posted}')"




In the example above
We are:- 
Importing SQLAlchemy: from flask_sqlalchemy import SQLAlchemy imports the SQLAlchemy class, enabling integration of SQLAlchemy with Flask.

Creating SQLAlchemy Instance: db = SQLAlchemy() initializes an instance of SQLAlchemy. This instance will manage the interactions between the Flask app and the database.

Defining Model BlogPost:
class BlogPost(db.Model): creates a SQLAlchemy model named BlogPost that inherits from db.Model.
Various db.Column() instances define the fields for the BlogPost model, such as id, title, body, author, and date_posted. These correspond to columns in the database table. nullable=False ensures that the fields cannot be empty.
__repr__ Method: The __repr__ method defines a string representation of the BlogPost object. It returns a formatted string containing the post's title, author, and date_posted

Configure the Database in Flask App:
...
from flask_sqlalchemy import SQLAlchemy

#import db and the Model
from models import db, BlogPost
app = Flask(__name__)
...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_name.db'
# replace db_name with your sqlite database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended to suppress warnings

# Initialize the SQLAlchemy object 'db' with the Flask app
db.init_app(app)

# Create the tables in the database (run this once to create the tables)
with app.app_context():
    db.create_all()

...


To create the tables and use the database we are:- , 

Importing Models: from models import db, BlogPost imports the db instance and the BlogPost model from the models.py file.
Database Configuration: app.config['SQLALCHEMY_DATABASE_URI'] sets the URI for the SQLite database (blog.db), and app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False disables change tracking.
Initializing SQLAlchemy: db.init_app(app) initializes the SQLAlchemy instance (db) with the Flask app.
Creating Database Tables: with app.app_context(): db.create_all() creates the necessary database tables based on the defined models within a Flask application context. We can also use flask migrate to make modifying and updating the database table easy.
Creating data using our form and our database
@app.route('/', methods=['GET', 'POST'])
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost()
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('create_post'))
    return render_template('create_post.html', form=form)


post = BlogPost(): Creates an instance of the BlogPost model. This line initializes a new BlogPost object.
form.populate_obj(post): Populates the post object with data from the form. This method maps the form fields to the corresponding attributes of the post object.
db.session.add(post): Adds the post object (representing a new blog post) to the database session, preparing it to be committed.
db.session.commit(): Commits the changes to the database. This line saves the new blog post to the database.
flash('Post created successfully!', 'success'): Flashes a success message to be displayed on the next rendered page (if applicable) indicating that the post was created successfully.
Database migrations  with Flask-Migrate
As applications evolve, changes to the database schema become necessary, such as adding new tables, modifying existing columns, or creating relationships between tables. Flask-Migrate is an extension that integrates Alembic(Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.) into Flask applications, providing database migration support. 

It allows you to manage changes to your database schema using migrations, keeping your database structure in sync with changes made to your SQLAlchemy models.

Installation
pip install Flask-Migrate


Installation
...

from flask_migrate import Migrate

... 

migrate = Migrate(app, db)


Migration Workflow
Initialization: Run flask db init to create a migrations directory and set up the migration environment.
Migration Generation: After modifying the models, use flask db migrate to generate a migration script based on the changes detected in the models.
Applying Migrations: Execute flask db upgrade to apply the generated migration script, updating the actual database schema.
Downgrading Migrations: If needed, you can revert to a previous state using flask db downgrade (though it's advisable to backup data before downgrades).





Authentication and Authorisation with Flask-Login

Authentication and authorization are fundamental concepts in the realm of data security, playing a crucial role in safeguarding our application

While these two terms are often used interchangeably and are closely related, they refer to distinct concepts.

Authentication involves the process of verifying the identity of users to grant access to a system. For most API, we deal with  login credentials( username, passwords, etc) and other identification means

Authorization, on the other hand, focuses on determining a user's or person's permissions and rights to access specific resources or perform certain actions within our application.  For example, does the logged in user have permissions to edit a certain point of our application

Flask-Login is a Flask extension that provides user session management and authentication support. It helps in managing user sessions, login/logout functionality, and user authentication.

Installation
pip install Flask-Login


Create a User Model
# models.py
...
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


The UserMixin class in Flask-Login is a helper class provided by the Flask-Login extension. It provides default implementations for common methods required for user authentication, making it easier to integrate user models with Flask-Login. 

Flask-Login expects certain methods to be implemented in the user model, such as get_id(), is_authenticated, is_active, and is_anonymous. UserMixin provides default implementations for these methods, so you only need to define the user model specificities (like database columns).

Configure the Flask-login
# app.py
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User

login_manager = LoginManager(app)

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



LoginManager Initialization:

LoginManager is an extension provided by Flask-Login used for managing user sessions and authentication.
In the example, LoginManager is initialized and associated with the Flask application (app) by passing the app object to it.


user_loader Callback:

@login_manager.user_loader is a decorator provided by Flask-Login used to register a function to load users based on their ID. When a user logs in, Flask-Login stores the user's ID in the session. The user_loader callback is used to retrieve the user's information from the database based on this ID.
In this example, the load_user function is defined to query the User model to retrieve the user with the given user_id.

load_user function
This function retrieves the user by querying the database using the User model's query.get() method, filtering by the provided user_id.
The int(user_id) conversion is used assuming the user ID is stored as an integer in the database. Adjust this based on your actual implementation if the ID is stored differently.

An Example 

To create a user registration form using Flask-WTF, you can define a form class using the FlaskForm provided by Flask-WTF. Below is an example of how you can create a simple user registration form with fields for username, password, and email:
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



Usage in a Flask Route
Register Route
# app.py
from flask import Flask, render_template, redirect, url_for
from forms import RegistrationForm, LoginForm
from models import db, User

# other config routes

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user object and add it to the session
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)  # Assuming you have a method to hash and set the password
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login page after successful registration
    return render_template('register.html', form=form)




Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):  # Assuming you have a check_password method
            # Login the user using Flask-Login's login_user method
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to dashboard after login
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)


The templates
Register Template
{% extends 'base.html' %}

{% block title %}Register{% endblock %}

{% block content %}
<form method="POST" action="{{ url_for('register') }}">
    {{ form.csrf_token }}
    <div>
        {{ form.username.label }}<br>
        {{ form.username }}
    </div>
    <div>
        {{ form.email.label }}<br>
        {{ form.email }}
    </div>
    <div>
        {{ form.password.label }}<br>
        {{ form.password }}
    </div>
    <div>
        {{ form.confirm_password.label }}<br>
        {{ form.confirm_password }}
    </div>
    <div>
        {{ form.submit(class="btn btn-primary") }}
    </div>
</form>

{% endblock %}

LOGIN Template
<!-- Login Template -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<form method="POST" action="{{ url_for('login') }}">
        {{ form.csrf_token }}
        <div>
            {{ form.username.label }}<br>
            {{ form.username }}
        </div>
        <div>
            {{ form.password.label }}<br>
            {{ form.password }}
        </div>
        <div>
            {{ form.submit(class="btn btn-primary") }}
        </div>
    </form>

{% endblock %}


Authorization
As we have seen, authorization is giving access to the user to the different parts of the application. We can use the @login_required decorator to protect some routes and these routes will only be accessed when the user logins. 

from flask_login import login_user, logout_user, login_required, current_user
@app.route('/create-post')
@login_required
def dashboard():
    return render_template('create_post.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


Week Four Assignment 📝
Connect your flask application to a database
Implement Authentication ( register and login logic) and authorisation for your routes


WEEK FIVE
Week Five: Modular Applications with Blueprint
As your application grows bigger, you want to start separating the logic in your application and make modular applications for example we may want to move authentication logic , templates , etc to a different module and so on for other 
What is a  Blueprint?
A Blueprint is a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint. 
Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications. Blueprints can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications. A Blueprint object works similarly to a Flask application object ( app = Flask(__name__) ), but it is not actually an application. Rather it is a blueprint of how to construct or extend an application.

Creating a well-organized Flask application using Blueprints becomes crucial as the project expands. For instance, in a blog application, different functionalities like posts, users, and authentication could be separated into individual Blueprints. This separation aids in code maintenance, scalability, and reusability across multiple projects.
Creating a Blueprint
Let’s explore the structure of a small Flask application

blog_app/
|
├── app.py
├── forms.py
├── models.py
├── templates/
└── static/

`

The `app.py` file will contain the application's definition and its views associated with their corresponding routes, the models for the definitions of database associations, templates for templates, static for static file so on and so forth

However, this project layout might not scale effectively with the growth of the application. As code grows, maintaining all the view logic in a single `app.py` becomes challenging. Hence, as your application expands in size or complexity, consider structuring the code differently to ensure maintainability and clarity.

Let's refactor the blog application by using Flask Blueprints to achieve better code organization:

.
├── app.py
├── auth_blueprint.py
├── forms.py
├── models.py
├── posts_blueprint.py
├── static/
└── templates/


We have created posts_blueprint and auth_blueprint which will contain the Blueprint implementation and we will update the `app.py` to contain the Flask Blueprint configuration.
Here's an example implementation of a Flask Blueprint in `posts_blueprint.py`:

from flask import Blueprint

posts_blueprint = Blueprint('posts_blueprint', __name__)
@post_blueprint.route("/posts")
def posts():
    return render_template("posts.html")


This code defines the `posts_blueprint` Flask Blueprint with a view at the route `/posts`  that renders the posts.html template

To use the Flask Blueprint, modify `app.py`:
from flask import Flask
from posts.views import posts

app = Flask(__name__)
app.register_blueprint(post_blueprint)


This modification in `app.py` imports and registers the Flask Blueprint `posts_blueprint` within the application.

Flask Blueprints function similarly to Flask applications, allowing association of resources like static files, templates, and views with routes. However, Blueprints need to be registered in an application to execute their operations.

Organizing our Application Using Flask Blueprints
Consider structuring our blog application using Flask Blueprints to segregate various functionalities like posts, users, and authentication. Below is an example of how you can organize a blog application into different Flask Blueprints:
blog/
│
├── posts/
│   ├── templates/
│   │   └── posts/
│   │      ├── post_list.html
│   │      └── post_detail.html
│   │
│   ├── __init__.py
│   └── posts_blueprint.py
│
├── auth/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   │
│   ├── __init__.py
│   └── auth_blueprint.py
│
├── app.py
└── config.py


Each directory corresponds to a different functionality, such as `posts` for handling blog posts and `users` for managing user-related operations.

Let's look at an example of the `posts_blueprint.py` file within the `posts` directory:

from flask import Blueprint, render_template

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

@posts_blueprint.route('/posts')
def post_list():
    # Retrieve posts from database
    posts = [
      ...
    ]
    return render_template('posts/post_list.html', posts=posts)

@posts_blueprint.route('/posts/<int:post_id>')
def post_detail(post_id):
    # Retrieve post details based on post_id

    post = {'title': f'Post {post_id}', 'content': f'Content for post {post_id}'}
    return render_template('posts/post_detail.html', post=post)



In the `app` file, you'll import and register these Blueprints:

from flask import Flask
from posts.posts_blueprint import posts_blueprint
from auth.auth_blueprint import auth_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint, url_prefix='/blog')
app.register_blueprint(users_blueprint, url_prefix='/auth')

...



With this structure, the `posts` Blueprint handles routes related to blog posts, such as displaying a list of posts and individual post details. Similarly, the `auth` Blueprint manages auth-related functionality, including login, registration, and user profiles.

Flask Blueprints are a powerful tool for organizing and structuring Flask applications, especially as they grow in complexity. This modular approach allows for better code management, scalability, and easier collaboration among team members.

By implementing Flask Blueprints in your blog application, you can effectively manage various functionalities while keeping your codebase organized, maintainable, and conducive to code reuse across multiple projects.
Week Five Assignment 📝
Update your application to use Blueprints
Separate the posts, auth, users, logic, templates, models and forms

WEEK SIX
Week Five: Building RESTful APIs with Flask
Designing and implementing RESTful endpoints in Flask
Handling CRUD operations (GET, POST, PUT/PATCH, DELETE)
Testing APIs using tools like Postman


What is an API?
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.
Application Programming Interfaces hide complexity from developers, extend systems to partners, organize code and make components reusable.
APIs are sometimes thought of as contracts, with documentation that represents an agreement between parties: if one party sends a remote request structured a particular way, this is how the second party’s software will respond.
Brief history
APIs emerged in the early days of computing, well before the personal computer. At the time, an API was typically used as a library for operating systems. The API was almost always local to the systems on which it operated, although it sometimes passed messages between mainframes.
After nearly 30 years, APIs broke out of their local environments. By the early 2000s, they were becoming an important technology for the remote integration of data.
Advantages of APIs
APIs let a product/service communicate with other products/services without having to know how they are implemented. This can simplify app development, saving time and money.
Since APIs simplify how developers integrate new application components into an existing architecture, they help business and IT teams collaborate
When designing new tools and products (or managing existing ones), APIs give flexibility and provide opportunities for innovation
They also simplify design, administration and use
APIs have become so valuable that they comprise a large part of many businesses' revenue. Major companies like Google, eBay, Salesforce.com, Amazon, and Expedia are just a few of the companies that make money from their APIs. The ‘API economy’ refers to this marketplace of APIs
How do APIs work?
APIs are a simplified way to connect infrastructure through cloud-native app development, but they also allow data to be shared with customers and other external users
When you use an application on a mobile phone, the application connects to the internet and sends data to a server
The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone
Your phone’s data is never fully exposed to the server, and likewise the server is never fully exposed to your phone. Instead, each communicates with small packets of data, sharing only what is necessary
The application then interprets that data and presents you with the information you wanted in a readable way. This is what an API is – all of this happens via API


API use case
Example scenario: your small business’ website has a form used to sign clients up for appointments. You want to give clients the ability to automatically create a Google calendar event with the details for that appointment.
API use: the idea is to have your website’s server talk directly to Google’s server with a request to create an event with the given details. The server then receives Google’s response, processes it, and sends back relevant information to the browser, such as a confirmation message to the user. Alternatively, the browser can often send an API request directly to Google’s server, bypassing your server.
How is this Google Calendar’s API different from the API of any other remote server out there? In technical terms, the difference is the format of the request and the response. To render the whole webpage, your browser expects a response in HTML that contains presentational code, while Google Calendar’s API call would just return the data (likely in a format like JSON). If your website’s server is making the API request, then your website’s server is the client (similar to your browser being the client when you use it to navigate to a website). From your users’ perspective, APIs allow them to complete the action without leaving your website.
Approaches to API release policies
Private: the API is only for use internally. This gives companies the most control over their API.
Partner: the API is shared with specific business partners. This can provide additional revenue streams without compromising quality.
Public: the API is available to everyone. This allows third-parties to develop apps that interact with your API and can be a source for innovation.
Public APIs and API integration
APIs are a longstanding concept in computer programming and they have been part of developers’ tool sets for years. Traditionally, APIs were used to connect code components running on the same machine. With the rise of ubiquitous networking, more and more public APIs (sometimes called open APIs) have become available.
Public APIs are outward facing and accessible over the internet, allowing you to write code that interacts with other vendors’ code online; this process is known as API integration. These kinds of code mashups allow users to mix and match functionality from different vendors on their own systems. For instance, if you use the marketing automation software Marketo, you can sync your data there with Salesforce CRM functionality.
‘Open’ or ‘public’ should not be interpreted as meaning ‘free of charge’ in this context. You still need to be a Marketo and Salesforce customer for this to work. However, the availability of these APIs makes integration a much simpler process than it otherwise would be.
Remote APIs
Remote APIs are designed to interact through a communications network. By ‘remote’, this means that the resources being manipulated by the API are somewhere outside the computer making the request.
Since the most widely used communications network is the internet, most APIs are designed based on web standards. Not all remote APIs are web APIs, but it’s fair to assume that web APIs are remote.
Web APIs typically use HTTP for request messages and provide a definition of the structure of response messages. These response messages usually take the form of an XML or JSON file. Both XML and JSON are preferred formats because they present data in a way that’s easy for other apps to manipulate.
The modern API
Over the years, what an ‘API’ is has often described any sort of generic connectivity interface to an application. However, more recently, the modern API has taken on some characteristics that make them valuable and useful:
Modern APIs adhere to standards (typically HTTP and REST) that are developer-friendly, easily accessible and understood broadly
They are treated more like products than code. They are designed for consumption by specific audiences (for example, mobile developers)
Modern APIs are documented, and they are versioned in a way that users can have certain expectations of their maintenance and lifecycle
Since they are much more standardized, they have a much stronger discipline for security and governance
The modern API has its own software development lifecycle (SDLC) of designing, testing, building, managing and versioning
Creating REST API in flask
The easiest way to create an API in Flask is by returning the data from a route as json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'}


This will return a JSON object
{
  "message": "Hello, World!"
}

The JSON response consists of a key-value pair where "message" is the key, and "Hello, World!" is the corresponding value.

Using Flask_restful
Flask-RESTful is an extension for Flask that simplifies the creation of RESTful APIs by providing tools to create routes as resources with HTTP methods (GET, POST, PUT, DELETE) mapped to class methods.

Why Flask-RESTful:
Flask-RESTful provides a clean and organized way to structure API endpoints using resources and HTTP methods.
It allows developers to focus on defining resources and their methods, making the code more readable and maintainable.
It simplifies request parsing, validation, and response handling for RESTful APIs.


W can install flask_restful through pip
pip install flask-restful

Creating an EndPoint. 
Flask_restful uses a class based approach to serve the data to our endpoint and we have to register( add_resource) the api and create an endpoint for it
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')

if __name__ == '__main__':
    app.run(debug=True)


We can now use a tool like postman/insomnia or curl to test our endpoint and it will return the JSON object ( dictionary)
$ curl http://127.0.0.1:5000/api
{"hello": "world"}

Resourceful Routing
The main building block provided by Flask-RESTful are resources. Resources are built on top of Flask pluggable views ( Class Based Views), giving you easy access to multiple HTTP methods just by defining methods on your resource. A basic CRUD resource for a post application (of course) looks like this:
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Dummy data - Replace this with actual database usage
blog_posts = {
    1: {'title': 'First Post', 'content': 'This is the content of the first post'},
    2: {'title': 'Second Post', 'content': 'Content for the second post goes here'}
}

# Parser for handling request data
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the blog post')
parser.add_argument('content', type=str, help='Content of the blog post')

class BlogPosts(Resource):
    def get(self):
        return blog_posts  # Return all blog posts

    def post(self):
        args = parser.parse_args()
        post_id = max(blog_posts.keys()) + 1
        blog_posts[post_id] = {'title': args['title'], 'content': args['content']}
        return blog_posts[post_id], 201  # Return the newly created post with status code 201

class BlogPost(Resource):
    def get(self, post_id):
        return blog_posts.get(post_id)  # Return a specific blog post by ID

    def delete(self, post_id):
        if post_id in blog_posts:
            del blog_posts[post_id]
            return '', 204  # Return empty response with status code 204 for successful deletion
        return 'Blog post not found', 404  # Return 404 if post doesn't exist

api.add_resource(BlogPosts, '/api/posts')  # Endpoint for all blog posts
api.add_resource(BlogPost, '/api/posts/<int:post_id>')  # Endpoint for a specific blog post

if __name__ == '__main__':
    app.run(debug=True)



Details:
GET /api/posts- Retrieves all blog posts.
POST /api/posts - Creates a new blog post.
GET /api/posts/<int:post_id>' - Retrieves a specific blog post by ID.
DELETE /api/posts/<int:post_id>' - Deletes a specific blog post by ID.

We can test our endpoints using Postman, insomnia  or curl ( is a command line tool that enables data exchange between a device and a server through a terminal)

Testing Endpoints with curl
Assuming the Flask app is running on localhost at port 5000, we can use curl commands to interact with the API.

1.  Get all blog posts
curl http://localhost:5000/api/posts

This command sends a GET request to the /api/posts endpoint to retrieve all blog posts.


2. Create a new blog post
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Post", "content": "Content for the new post"}' http://localhost:5000/api/posts

This command sends a POST request to the /blog endpoint to create a new blog post. Replace the JSON data (title and content) as needed.

3. Get a specific blog post by ID
curl http://localhost:5000/api/posts/1

This command sends a GET request to the /blog/1 endpoint to retrieve the blog post with ID 1.

4. Delete a specific blog post by ID
curl -X DELETE http://localhost:5000/api/posts/1

This command sends a DELETE request to the /blog/1 endpoint to delete the blog post with ID 1.
Curl Command Explanation:
-X flag specifies the request method (POST, DELETE, GET, etc.).
-H flag adds a header to the request.
-d flag sends data in the request body in JSON format.

These curl commands simulate HTTP requests to the API endpoints created with Flask-RESTful, allowing you to test the functionality and observe the responses returned by the API. Adjust the endpoint URLs and request payloads according to your specific API design and requirements.

We can now create endpoints that use our database and serve JSON data
Week Six Assignment 📝
Create an API for your blog application
Test your endpoints using tools like postman or insomnia and make sure the endpoints give you the expected data.

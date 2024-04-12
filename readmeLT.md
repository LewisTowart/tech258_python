# Tech 258 Python

<img height="300" src="C:\Users\lewis\Pictures\Techbrain.jpg" width="400"/>

"learning change"

### What is Python? What is the history of Python?

Python is a computer programming language often used to build websites and software, automate tasks, and analyze data.

Python is a widely used general-purpose, high-level programming language. It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation. It was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code.

### Why is Python popular? Why is it particularly popular for DevOps engineers?

Python is a popular language for web and software development because you can create complex, multi-protocol applications while maintaining concise, readable syntax.

Python is also specifically popular for DevOps Engineers for reasons such as...
* Simplistic Syntax
* Versatility
* Extensive Library Support
* Easy to find help and documentation online (Large community)

### What is a virtual environment or venv?????

A Python Virtual Environment is an isolated space where you can work on your Python projects, separately from your system-installed Python. You can set up your own libraries and dependencies without affecting the system Python.

### What is "pip"?

PIP is a package manager for Python packages, or modules

(A package contains all the files you need for a module. Modules are Python code libraries you can include in your project.)

### What is scripting? How is it different to programming?

The theoretical difference between the two is that scripting languages do not require the compilation step.

Scripting is a way of providing instructions to a computer, so you can tell it what to do and when to do it. In comparison, programming is the composition of sequences of instructions which would be used for much larger tasks.

#### Uses of Scripting
- Task Automation: Automate repetitive tasks, such as batch processing of files, generating reports, and performing data manipulations. 
- Glue Code: Stitch together different software systems, such as by combining the output of one program with the input of another or automating the execution of multiple programs in sequence. 
- One-off Tasks: Perform a quick calculation, test a code snippet, and explore data. 
- Dynamic Web: Manipulate web pages, such as by extracting data, filling in forms, and clicking buttons automatically. 
- Task Scheduling: Run a script at a specific time, or on a specific schedule.

#### Uses of Programming
- Application Development: Create everything from simple desktop applications to large-scale enterprise systems. 
- System Programming: Develop operating systems, device drivers, or other low-level system components. 
- Database Programming: Query databases, update data, and develop database applications. 
- Mobile Development: Build native applications for Android and iOS devices.

### What are the base python libraries?


Base Python libraries refer to essential modules and functionalities included in the Python Standard Library. These cover a wide range of tasks such as system operations, mathematical calculations, date/time manipulation, text processing, data serialization, networking, concurrency, command-line parsing, logging, XML processing, and database operations. Examples include os, math, datetime, re, json, urllib, logging, and more.

### What are some of the most popular external libraries?

Some examples I found online include:

- NumPy: For numerical computing with arrays. 
- Pandas: For data manipulation and analysis. 
- Matplotlib: For data visualization.
- Scikit-learn: For machine learning algorithms and tools.
- TensorFlow and PyTorch: For deep learning and neural networks.
- Django and Flask: For web development.
- Beautiful Soup: For web scraping.
- Requests: For making HTTP requests.
- NLTK and Spacy: For natural language processing.
- SQLAlchemy: For interacting with SQL databases.

### Age checker code

````
film_rating = "universal"

if film_rating == "universal":
    print("all age groups can watch this film")
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for "
          "children aged under 12. No one younger than 12 may see a 12A film in a cinema unless "
          "accompanied by an adult.")
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
````
### Code explained
* First part of the code is assigning a value to the variable
* I am then creating the first if statement check to see if the value matches universal
* I then continue the checks with to see if it has been assigned the value pg
* The code continues in a similar way, it is important to note the or section
* For both 12 and 12a values the same message will be printed it is important to reference the variable after using or
* Finish with else to close the if statements for anything that doesn't match the previous values

### Loops

#### What are loops?

A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the
condition is satisfied.

#### What types of loop are there?

For loop
The for loop is used in the case where a programmer needs to execute a part of the code until the given condition is satisfied.

While loop
The while loop is to be used in situations where the number of iterations is unknown at first. The block of statements 
is executed in the while loop until the condition specified in the while loop is satisfied.

(while loops are more suitable when the number of iterations is determined by a condition that may change during execution)

Nested loop
To use one looping statement inside another looping statement.

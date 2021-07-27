# Web Application that displays a To Do List

The application displays the pending tasks and completed tasks. There is an option to add a task, mark a task as completed and delete/remove a task. The tasks have a title and a deadline. The data is stored in SQLite. The tasks are ordered by deadline.

## How to run the program

1. Have Python and SQLite installed. Download and install an IDE for Python. 
2. Install ![Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
3. Open command line and go to the directory of the program and run the comman ```python init_db.py```. A database.db should be created in the directory of the folder. 
4. Run the following commands to start the program 
On Windows:    
    ``` venv\Scripts\activate```
    ```$env:FLASK_APP = "app"```
    ```flask run```
5. On the command line when the link to the program appears (Similar to this: Running on http://127.0.0.1:5000/), click on it. 
6. It will redirect to the page with the application

## Explanation of code

* In the main directory there are three files: **app.py**, **init_db.py** and **schema.sql**. **app.py** contains the code for the web application, **schema.sql** contains the schema of the database and **init_db.py** contains the code to initialise the database. 
* Each entry of a task has a unique ID, a title, a deadline and status represented by number: 0=incomplete and 1=complete. 
* There are three HTML templates used: **index.html**, **base.html** and **displaycompletedtasks.html**.  **index.html** extends the **base.html** and also displays the pending tasks in the order of their deadlines, **base.html** contains the navigation bar and template that will be displayed across the web application and **displaycompletedtasks.html** has the code to display the completed tasks with the option of removing them. 
* One stylesheet is used and its called **style.css** and can be found under **static\css**.
* In **app.py**, we use five different routing: to display pending tasks, to display completed tasks, to delete a pending task, to complete a pending task and to delete a completed task. The tasks are ordered according to their deadline with the help of dictionaries. 

## Technologies Used

Python, Flask, SQLite, HTML, CSS, JavaScript
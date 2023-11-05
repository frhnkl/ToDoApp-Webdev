
# To-Do App Documentation

## 1. Introduction and Background Problem
A project manager needs to see and control his/her staff's work and progress. therefore, he contacted his friend to make him a simple ToDo App to make him able to control and see what his staff do. The solution is a simple To-Do-App named 'Yours To Do'. created with Flask API backend. Users can create an account, log in, add new tasks, delete tasks, edit tasks, and move them to the 'done' part. it can help with your time and activities management

## Objectives
- Create an app where users can register and login
- Create an app where users can add Tasks with names and descriptions of said tasks
- User can move tasks between "ongoing" and "DONE"
- user can edit or delete their tasks
- users can see every task in to-do app

## 3. Installation
- there are some prerequisites that need to be installed before running this app. Those said prerequisites are :
- Flask == 2.3.2
- Flask-Migrate == 4.0.4
- Flask-SQLAlchemy == 3.0.3
- Flask-JWT-Extended == 4.5.2
- those prerequisites are listed in requirement.txt and can be installed using
  ```cmd
  pip install to-requirements.txt
  ```

## 4. Usage Flowchart
![Teks paragraf Anda](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/ee466e40-96ff-4c84-ac22-9e22e979acec)

this is a flowchart for the app. The user starts on the login page. If the user doesn't have an account, the user can click on the registration page to create an account. after logging in, the user will be redirected to the main page where the user can create, edit, or delete tasks.


## 5. Technologies Used
- List the technologies and libraries used, including:
  - Python
  - Flask
  - SQLAlchemy
  - HTML
  - CSS
  - JavaScript

## 6. Project Structure
```txt
.
└── Todoapp/
    ├── app/
    │   ├── auth/
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── frontend/
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── models/
    │   │   ├── blacklist_token.py
    │   │   ├── task.py
    │   │   └── user.py
    │   ├── static/
    │   │   ├── js/
    │   │   │   ├── script-home.js
    │   │   │   ├── script-login.js
    │   │   │   └── script-register.js
    │   │   └── picture/
    │   │       └── bg-auth.jpg
    │   ├── tasks/
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── templates/
    │   │   ├── auth/
    │   │   │   ├── base.html
    │   │   │   ├── login.html
    │   │   │   └── register.html
    │   │   ├── tasks/
    │   │   │   └── index.html
    │   │   └── base.html
    │   └── user/
    │       ├── __init__.py
    │       └── routes.py
    ├── migrations/
    │   └── versions/
    │       └── initial_migration.py
    ├── app.db
    ├── config.py
    └── requirement.txt
```
## 7. Database Schema
![image](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/d821b0a3-ab6f-4c57-b81e-f2bf775c47a8)
- this is the schema that been created using flask migrate in app.db
- there are 3 main tables
- blacklist_token. generated by
```python
  from app.extension import db
  class BlacklistToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)

    def serialize(self): 
        return {
            "id": self.id,
            "jti": self.jti,
        }
  ```
- tasks. generated by :
```python
  from app.extension import db
  class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024))
    status = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship('Users', back_populates = 'tasks')
    def serialize(self): 
        return {
            "id": self.id,
            "title": self.title,
            "description":self.description,
            "status": self.status,
            "user_id":self.user_id
        }
  ```
- users. generated by:
```python
  from app.extension import db
  class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True, nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    tasks = db.relationship('Tasks', back_populates='user')
  def serialize(self): 
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email":self.email,
            "password":self.password
        }
  ```

## 8. User Guide for Deployment
- There are a few steps to deploy To-Do App:
  1. Open cmd and run
     ```cmd
     flask db init
     ```
     to initialize database
  2. run
     ```cmd
     flask db upgrade
     ```
     to make sure to keep it up-to-date
  3. run
     ```cmd
     flask app run
     ```
     to deploy the app. terminal will give you a link to the port that will host the app
  4. enjoy!
## Demonstration
- User start their journey on the login page. if the user doesn't have an account, the user can create one by clicking on the register button.
![todoapp login](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/7e5adf4a-2624-4ecd-a10c-60aa852d66ec)
- If the user clicks on the register button, the user will be redirected to the register page
![regis page](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/bab7f140-062a-4afd-bc8a-48598aa3f4e9)
- The user has to fill out the form, and if it is successful, a success message will appear
![regis success](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/5f0dd538-f504-4161-972a-bc73b95c6c56)
- if something error, in this case, the name already exists, an error pop-up will appear
![fail regis](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/260169fb-47f9-4f86-85bd-053bc52161f9)
- after logging in, the user will be redirected to the main page
![main page](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/5262afd4-d0c4-4211-ad13-d51e40f0f23e)
- user can create a new task
![create new task](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/a3183497-d346-470a-8fe0-066f8bc88983)
- The user needs to fill in both the title and description. if not, this kind of message will appear
![fail creating task](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/b2560614-4296-46bb-ac5f-f68aeaf785d5)
- if the task is created, it will be updated on the main page
  ![task created](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/d9dd9291-948e-4f4a-a612-30747aa2d951)
- user can also edit their task
  ![edit task](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/fc091102-202b-42bc-b909-9ba0caec357c)
- if the user success in editing their task, an edited version will appear on the page
  ![task edited](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/17a26c03-98b5-48c4-8150-1d5ad02dcf09)
- user can drag their task to "Done" if they completed the task
  ![task dragged to done](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/8e2c8c69-6802-4d98-86d4-ebcd47bd0a06)
- user can also delete tasks, this is a picture before a user deletes a task
  ![task before delete](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/0a4b7297-3a81-4875-9d4d-6addbcb36691)
- deleting task
  ![deleting task](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/753e5950-5eea-432a-9e03-1b6bdc9312ec)
- after a task is deleted, the said task will be removed from the page
  ![task deleted](https://github.com/frhnkl/ToDoApp-Webdev/assets/125452431/84e11b93-f968-4769-a682-2d9e8ab0ab3a)

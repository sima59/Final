# Growth

This is the application to save the data of the a person from the birth till 20 years old and shows them in bar chart to help parents see the status of the kids growth.I like to have a avrage growth of each year and compare with the child growth according to it's gender but my Flask programming ability is too limited to do this. I'm begginer in Flask and will work on my project to improve it.

The datbase name is Growth It has 
ID
First name 
Last name
URL
head size
hight
weight
age 
gender 
date- add
date- modify

It let the user to add ,delete and modify data and sort them according to the age
The application doesn't show result for age more than 20 or less than 0 


We have:
Domain: I have commands,events and models under my domain. Models have a class of Growth.Event has some classes to add ,delete and list data.In .    Event and commands are reflect each others.
        -**Commands**: commands also I have some classes to add ,delete and list growth information
        -**events**: Event has some classes to add ,delete and list data.In . Event and commands are reflect each others.
        -**Models**
adapter: it is actually implementation of the service layer.Adapter is pulled from domain.Shows how this work is going to be happend 
        -**orm.py**
        -**repository**
Service Layer:
        -**Handler**: (Service Layer)Shows how you can ask for a work. This is where the commands and unit of work combine to cause the event to be handle. Everytime when we do some thing it is the place where the action handle  
        -**Messagebus**:Is the list of commands and events and causes them execute. It's like a dictionary and has concept of each commands or events
        -**Unit_of_work**:(Service Layer)Shows how you can ask for a work .It has a fake repository for testing 

API:
        -**flaskapi**
        -**view**
Boostrap




At a basic level, the architecture is designed with a layered strategy to include the following common/typical elements:

- **Presentation Layer** (will be a module called Growth.py here)
- **Business Logic Layer** (will be a module called commands.py here)
- **Presistence Layer** (will be a module called database.py here)





The [DB Browser for SQLite](https://sqlitebrowser.org/) tool will be useful to inspect the data and manage the database file.  [SQLiteStudio](https://sqlitestudio.pl/features/) is another alternative that would accomplish the same thing.

The initial database wil consist of a table called `Growth`:

```sql
CREATE TABLE IF NOT EXISTS Growth
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    Lname   TEXT NOT NULL,
    url TEXT NOT NULL,
    head real,
    weight real,
    hight real,
    age int,
    gender TEXT,
    notes TEXT,
    date_added TEXT NOT NULL
);
```


# SQLAlchemy 1.3.x to 1.4.x

Some things about SQLAlchemy have changed, making the APP code somewhat different.  This repohas been refactored to use 1.4.x.
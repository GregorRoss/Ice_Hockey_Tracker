
# **Project Ice Hockey Tracker**


## *1.Set Up*

- First, you will need to ensure that you have a database called hockey.

```sh
dropdb hockey
createdb hockey
```

- Once you have created the database, you will need to run the hockey SQL file against it to create the tables.

```sh
psql -d hockey -f ./db/hockey.sql
```

- Once you have created the tables you then need to run the console.py file to populate the tables with the data that will help to run the application.

'''sh
python3 console.py
'''
- now that you have the database populated and fully up and running you can run the Flask web server to get things up and running. from the Ice_hockey_tracker folder start flask from the terminal screen.

'''sh
flask run
'''




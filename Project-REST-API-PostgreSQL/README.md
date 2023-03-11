# Connect PostgreSQL through RESTAPI

PreRequisite:

Signup in: `https://www.elephantsql.com/` to use free PostgreSQL Server.

Install `Postman Tool` to POST and Get Queries

Steps:

1. Initiate and Activate the Virtual Enviroment.

```BASH
python3 -m venv venv && . venv/bin/activate 
```

2. Install requirements Modules

```PYTHON
pip install -r requirements.txt
```

3. Update `.flaskenv` as below:

```YAML
FLASK_APP=app
FLASK_DEBUG=True

```


5. Start the Application

```
flask run
```

6. Run Following POST Query in POSTMAN to create new user

<img src="./Images/Postman_User.JPG"  width="100%" height="100%">


7. Run Following POST Query in POSTMAN to add items in user

<img src="./Images/Postman_Item.JPG"  width="100%" height="100%">

8. Login to `elephantsql` to verify the Entries in DataBase

<img src="./Images/elephantsql_query_User.JPG"  width="100%" height="100%">

9. To Chek the ITEMS Details:

<img src="./Images/elephantsql_query_Userid_5.JPG"  width="100%" height="100%">

<img src="./Images/elephantsql_query_Items.JPG"  width="100%" height="100%">



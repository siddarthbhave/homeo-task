# Covid Bed Booking

  

1. `git pull` this repo

2. start any python virtual environment,  ```py -m venv env```

3. Install all pip packages,  ```pip install -r requirements.txt```

4. Run app,  ```flask run```

  <br>

*Note: Change the `MONGO_URI` on line 10 and connect with your MongoDB database having some pre-exisiting data in it. If not it check out data.json for some dummy data*

  

## Use of APIs

**GET '/'** -> Home route. Initializes database

**GET '/find/{bedId}'** -> Send valid Bed Id. Returns all data regarding that particular bed

**POST '/update/{bedId}'** -> Send valid Bed Id and data to update respective fields. You can send any data in any order and not all fields are compulsory to be sent. Updates the user.

**POST '/add'** -> Send all required data. Adds the data send as a new user

**DELETE '/delete/{bedId}'** -> Send valid Bed Id to be deleted. Deleted that particular Bed Id entry

**GET '/get_all'** -> Gets the whole list of all beds occupied.

**GET '/filter?arg1=value1&arg2=value2'** -> Gets data based on filter used. Send request with query string arguments with parameters `arg1` and `arg2`. `arg1` takes values of any key (for eg., `"name","id","criticalLevel"` for any field in document) and `arg2` takes values of values to be queried (for eg., `1,"James",5` or any key-value in document ) respectively. Example for a valid query string: `'/filter?arg1=name&arg2=James'` given that `"name":"James"` exists in the document.
<br>
Update and Add new routes also check for pre-existence of the data
- If data exists already, then it won't add, tells user to change data
 - If data doesn't exists already, then it won't update, tells user to
   change data

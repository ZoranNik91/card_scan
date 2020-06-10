# Card Scan for arrival and departure employees

## API

```
/api 
```

Get all data for every user for a specific date

**Method:** GET  
**Query params:** 

| Property | Value | Example |
| --- | --- | --- |
| `date` | `yyyy-mm-dd` | `/api?date=2019-10-23` |

```
/api/card_id
```

Check if a user exists.  
Writes to database the arrival timestamp or departure timestamp accordingly.  

**Method:** POST  
**Request data:** 

| Property | Value | Example |
| --- | --- | --- |
| `card_id` |  (Number) | `1112223334` |

**Response data:** 

| Property | Value | Description |
| --- | --- | --- |
| `status` | `"error" | "success"` |  |
| `message` | (a status message) |  |
| `user` | `None | Object` | Returns the User data |


```
/api/register
```

Insert user into database.  

**Method:** POST  
**Request data:**  

| Property | Value | Example |
| --- | --- | --- |
| `name` |  (String) | `Zoran` |
| `surname` |  (String) | `Nikolic` |
| `email` |  (String) | `zoran@gmail.com` |
| `phone` |  (String) | `63942015` |
| `card_id` |  (Number) | `1112223334` |

**Response data:** 

| Property | Value | Description |
| --- | --- | --- |
| `message` | (Insertion error/succcess message) |  |


## CLI

Run in terminal arrival.py to see how it works. (In our case we input card ID from the terminal but in real life the employees scan the card trought the scanner).

```
python arrival.py
```

Adding one argument next to the arrival.py will show all users loged in on that date.

```
python arrival.py 2019-10-24
```
If the argument of the date is not added terminal will ask the user for the card Id, the date format must be te same like in the example above in other case will be a Traceback.

# JWT token login system

### Installation
Copy from source
```bash
git clone https://github.com/onlinegxd/assignment3py
```

### Usage

```python
import json
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import make_response
import jwt
from datetime import datetime, timedelta
from flask.json import jsonify
```

### Examples

There're three possible ways to login

Already created accounts
| id | username | password | token |
| -- | -------- | -------- | ----- |
| 1  |  admin   | password |       |
| 2  |  user    |   pass   |       |
| 3  |  guest   | guestpass|       |

Usage examples:

(/login) - After a successful login, a token will be saved into database and remains until 15 minutes pass or re-login
![image](https://user-images.githubusercontent.com/80266425/139131153-a1bc640a-1591-47c6-ac3e-468c6cdd2ea5.png)
![image2](https://user-images.githubusercontent.com/80266425/139131380-5b69d1f7-52b5-4225-95fc-69681c63fcc8.png)
(/protected) - Decodes given token and verifies user
![image3](https://user-images.githubusercontent.com/80266425/139131408-fd037751-dd5a-4900-a591-97e795089ae3.png)

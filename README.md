## 1. Getting Started:
- cd MongoDB 
- docker compose build --no-cache   
- docker compose up

a. **Compass would be available in:**
    http://0.0.0.0:28081/ <br>
    (login/password: admin/root)

b. **Flask CRUD APP would be accessible through:**
    http://localhost:5000/


## 2. Testing API:

#####    Testing add user: 

    curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Rock Lee",
    "email": "rockLee@example.com",
    "pwd": "password123"
    }' http://localhost:5000/add

#####    Testing Delete User:

    curl -X DELETE http://localhost:5000/delete/<USER-ID>

  ##### Testing UPDATE User:

    curl -X PUT -H "Content-Type: application/json" -d '{
    "_id": "<USER-ID>",
    "name": "",
    "email": "",
    "pwd": ""
    }' http://localhost:5000/update

  ##### Testing get ALL Users:

    curl http://localhost:5000/users

  ##### Testing get user by specific ID:

    curl http://localhost:5000/user/<USER-ID>

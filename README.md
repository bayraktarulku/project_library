# project_library

Project is a written in Python.

## API References

### User Create
```http
POST /api/user
{
    "username": "user",
    "password": "user",
    "email": "user@project.net",
    "is_admin": 1,
    "is_active": 1
}
```

### User Delete
```http
DELETE /api/user?id=1

```

### User Change Password
```http
PUT /api/user

{
    "username": "user",
    "password": "user",
    "new_password": "root",
    "email": "user@project.net"
}
```

### Author Create
```http
POST /api/author
{
    "fullname": "Tess Gerritsen"
}
```

### Author Delete
```http
DELETE /api/user?id=1

```

### Type Create
```http
POST /api/type
{
    "name": "Detective"
}
```

### Type Delete
```http
DELETE /api/type?id=1

```


### Test Script
```text
  ### test_script ###
```

![test_script]( ### ADDED TEST SCRIPT ###)

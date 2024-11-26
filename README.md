---
title: README

---

Funny Paw: A Pet Owner and Pet Sitter Matching Platform
---

###  1. Description
--
**Author** : 
**YU-HSIN HUANG**, CHIA-HSUAN CHOU, YA-CHUN  LI, YAO-YU CHU, TZU-YU CHEN

--
**Date**: 2024-06-10

--
**Course**: NCCU (Taiwan) DBMS 2024 winter

--
**Project Description**: This project aims to create a web platform where pet owners can find suitable sitters to care for their pets, and pet sitters can connect with families in need of pet care services.


### 2. Technologies Used

**Frontend**：HTML, CSS, jinjat

**Backend**：Flask(python)

**Database**：MySQL

### 3.Functions implementations

* User authentication (Login/Registration for owners and sitters).
* Search functionality to find pet sitters by location or service type.
* Profile management for sitters and owners, including editing their personal info, viewing current orders.
* Booking system for pet care services.
* Reviews and ratings for sitters and owners.


### 4. Setup Instructions
* Install dependencies:
```
pip install flask-wtf
pip install wtforms
pip install email_validator
pip install flask_bcrypt
pip install flask_login
pip install flask_sqlalchemy
pip install PyMySQL
```
* Set up the database:
>After creating a schema in MySQL, should first change the password and the schema name in the following command in the __init__.py file
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourPassword@localhost/schema'
```
> The commands in the model.py file include all the setup for the database. To set up the database in MySQL directly through Python, follow the commands below.

```
from Petservice.models import db
from Petservice import app
app.app_context().push()
db.create_all()
from Petservice.models import Reservation, Fostercare, Walk, Review_owner, Review_sitter, Petsitter, Owner, Pet
```

* Run the development server:
```
python run.py
```

### 5. Contributors

| Teammates | Department | Contribution |
|-----------|------------|--------------|
| **YU-HSIN HUANG** | **Department of Statistics** | **Backend: Owner and sitter review, Owner order result, Sitter order information, Filter sitters, Filter results, Frontend HTML structure** |
| CHIA-HSUAN CHOU | Department of Statistics | Backend: Role selection, Pet sitter and owner registration/login, Filter sitters, Filter results, Book sitters, Frontend HTML structure|
| YAO-YU CHU | Department of Business Management | Backend: Edit profile, Owner and sitter comments, Frontend HTML structure |
| YA-CHUN  LI | Department of Advertising | Backend: Order history, Frontend HTML structure |
| TZU-YU CHEN | Department of Accounting  | Overall website design |
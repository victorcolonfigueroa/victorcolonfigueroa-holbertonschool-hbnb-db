```
data models to work as SQLAlchemy ORM classes while maintaining
compatibility with the DataManager interface.
Ensure the application can dynamically switch between the existing file-based system and the new database-backed system based on configuration.
```


Requirements:
- SQLAlchemy Integration: Incorporate SQLAlchemy to manage database interactions.
- Model Adaptation: Convert existing models to use SQLAlchemy’s ORM features, including the newly added fields (password and is_admin) needed for authentication and authorization.
- Flexible Persistence Switching: Enable seamless switching between file-based and database persistence modes using environment configuration.

Instructions:

- Update Project Dependencies:

- Ensure SQLAlchemy and Flask-SQLAlchemy are included in your project dependencies.
- Add these to your requirements.txt to manage installations efficiently.
- Initialize SQLAlchemy in Your Flask

Application:

- Configure your Flask app to use SQLAlchemy, initially connecting to a SQLite database for development purposes.

Example configuration:

```
 from flask_sqlalchemy import SQLAlchemy

 app = Flask(__name__)
 app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
 db = SQLAlchemy(app)
```

Refactor Existing Models to Extend

SQLAlchemy:

- Modify your data models to extend from db.Model, SQLAlchemy’s declarative base, ensuring they implement the methods defined by your DataManager interface.

- Define attributes using SQLAlchemy’s column types and relationships.
Example for a User model:

```
 class User(db.Model):
     id = db.Column(db.String(36), primary_key=True)
     email = db.Column(db.String(120), unique=True, nullable=False)
     password = db.Column(db.String(128), nullable=False)  # Ensure secure storage
     is_admin = db.Column(db.Boolean, default=False)
     created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
     updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
```

Enhance DataManager to Handle Both Persistence Types:

- Adjust the DataManager to manage both file-based and database interactions, possibly using an environment variable to switch between the modes.

- Implement conditional logic within the DataManager methods to direct queries to the appropriate storage type based on the configuration.

Example of conditional persistence logic:

```
 class DataManager:
     def save_user(self, user):
         if app.config['USE_DATABASE']:
             db.session.add(user)
             db.session.commit()
         else:
             # Implement file-based save logic
             pass
```

Testing and Validation:

- Develop comprehensive tests to ensure that both the database interactions via SQLAlchemy and the fallback to file-based operations function as expected.
- Test CRUD operations, relationship management, and the dynamic switching mechanism to verify full system integrity.

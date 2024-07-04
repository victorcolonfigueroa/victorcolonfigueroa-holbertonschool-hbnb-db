<<<<<<< Updated upstream
from flask_sqlalchemy import SQLAlchemy
from .base import Base

db = SQLAlchemy(model_class=Base)
=======
"""  """
from flask_sqlalchemy import SQLAlchemy
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    db = SQLAlchemy(app)
>>>>>>> Stashed changes

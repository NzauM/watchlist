from flask import Flask
from .config import DevConfig
'''
Import the DevConfig subclass 
'''


#Initializing application
app = Flask(__name__)


#Setting up configuration
app.config.from_object(DevConfig)
'''
Import the app.config.from
-object() method to set up configuration
We pass the DevConfig subclass as the prameters
'''



from app import views

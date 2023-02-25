from flask import Flask
from routes import install_routes
from model.pickle import PickledModel
import pickle5 as pickle


# Create Flask app
app = Flask(__name__)

# Load model and save to app config
app.config['MODEL'] = PickledModel('model/calliope.pickle')

# Install routes
install_routes(app)

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)

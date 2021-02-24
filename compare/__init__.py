from flask import Flask
from compare.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from compare import routes
from flask import Flask

app = Flask(__name__)
app.secret_key = "1234"

import controllers.index
import controllers.hello
import controllers.subject

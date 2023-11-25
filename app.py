from flask import Flask

app = Flask(__name__)
app.debug = True

import controllers.index
import controllers.hello
import controllers.subject

# import controllers.individual_task.index

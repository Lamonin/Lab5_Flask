import constants
from app import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    html = render_template(
        'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        len=len
    )

    return html

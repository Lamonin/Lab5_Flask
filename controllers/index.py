import constants
from app import app
from flask import render_template, request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    values_filled = False
    if request.method == 'POST':
        values_filled = True

    name = request.values.get('username', '')
    gender = request.values.get('gender', '')
    program_id = request.values.get('program', 0)
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'index.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        program_list=constants.programs,
        subjects_select=subjects_select,
        subject_list=constants.subjects,
        values_filled=values_filled,
        len=len
    )

    return html


@app.route('/clear', methods=['GET'])
def clear():
    return redirect(url_for('index'))

import numpy as np
from app import app
from flask import render_template, request


ops = [
    {
        "chkd_name": "сумму",
        "res_name": "Сумма векторов",
        "calc_func": lambda v1, v2: (v1 + v2).tolist()
    },
    {
        "chkd_name": "векторное произведение",
        "res_name": "Векторное произведение",
        "calc_func": lambda v1, v2: np.cross(v1, v2).tolist()
    },
    {
        "chkd_name": "скалярное произведение",
        "res_name": "Скалярное произведение",
        "calc_func": lambda v1, v2: np.dot(v1, v2)
    },
    {
        "chkd_name": "угол между векторами",
        "res_name": "Угол между векторами",
        "calc_func": lambda v1, v2: np.degrees(angle_between(v1, v2))
    }
]


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


@app.route('/', methods=['GET', 'POST'])
def index():
    vector_calculated = False

    vector_size = int(request.values.get('vector_size', 2))
    selected_ops_idx = [int(i) for i in request.values.getlist('vector_ops')]

    v1 = [0 for _ in range(vector_size)]
    v2 = [0 for _ in range(vector_size)]
    for i in range(vector_size):
        v1[i] = float(request.values.get(f'vector_1_{i}', 0))
        v2[i] = float(request.values.get(f'vector_2_{i}', 0))

    calc_res = []

    if request.method == 'POST':
        if 'vector_calculate' in request.form:
            v1np: np.ndarray = np.array(v1)
            v2np: np.ndarray = np.array(v2)

            for i in selected_ops_idx:
                try:
                    calc_res.append(ops[i]['calc_func'](v1np, v2np))
                except:
                    calc_res.append("неопределенно")

            vector_calculated = True
        elif 'vector_clear_values' in request.form:
            v1 = [0.0 for _ in v1]
            v2 = [0.0 for _ in v2]

    return render_template(
        'individual_task/index.html',
        vector_size=vector_size,
        v1=v1,
        v2=v2,
        ops=ops,
        selected_ops_idx=selected_ops_idx,
        vector_calculated=vector_calculated,
        calc_res=calc_res,
        len=len
    )

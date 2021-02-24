from compare import app
from compare.forms import inputForm
from flask import render_template, flash

@app.route("/", methods=["GET", "POST"])
# @app.route("/index", methods=["GET", "POST"])
def index():
    input_data = inputForm()
    if input_data.validate_on_submit():
        original = [ line.rstrip() for line in input_data.original_list.data.split("\n") ]
        change = [ line.rstrip() for line in input_data.change_list.data.split("\n")]
        transformed_original = [ name.rsplit(" ", 1) for name in original ]
        transformed_change = [ name.rsplit(" ", 1) for name in change ]

        lastname_dup = {}
        for name_ori in transformed_original:
            for name_cha in transformed_change:
                if name_ori[0] == name_cha[0]:
                    lastname_dup[" ".join(name_ori)] = " ".join(name_cha)

        result = []
        for item in lastname_dup.items():
            name_ori = item[0].rsplit(" ", 1)[1]
            name_cha = item[1].rsplit(" ", 1)[1]
            name_length = len(name_ori) if len(name_ori) < len(name_cha) else len(name_cha)
            counter = 0
            for a, b in zip(name_ori, name_cha):
                if a == b:
                    counter += 1
            if counter/name_length >= 0.5:
                result.append([item[0], item[1]])

        for item in result:
            if item[0] in original:
                original.remove(item[0])
            if item[1] in change:
                change.remove(item[1])

        result.append([original, change])

        return render_template("result.html", result=result, isinstance=isinstance, str=str)

    return render_template("index.html", input_data=input_data)
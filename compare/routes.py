from compare import app
from compare.forms import inputForm
from flask import render_template, flash


def firstname_matches(name01: str, name02: str):
    name_length = len(name01) if len(name01) <= len(name02) else len(name02)
    counter =0
    for a, b in zip(name01, name02):
        if a == b:
            counter += 1
    if counter/name_length >= 0.8:
        return True
    else:
        return False


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    input_data = inputForm()
    if input_data.validate_on_submit():
        original = [ line.rstrip() for line in input_data.original_list.data.split("\n") ]
        change = [ line.rstrip() for line in input_data.change_list.data.split("\n")]
        no_change = set(original) & set(change)

        original = list(set(original) ^ no_change)
        change = list(set(change) ^ no_change)
        transformed_original = [ name.rsplit(" ", 1) for name in original ]
        transformed_change = [ name.rsplit(" ", 1) for name in change ]

        name_match = {}
        for name_ori in transformed_original:
            for name_cha in transformed_change:
                if name_ori[0] == name_cha[0] and firstname_matches(name_ori[1], name_cha[1]):
                    name_match[" ".join(name_ori)] = " ".join(name_cha)
                    transformed_change.remove(name_cha)

        for item in name_match.items():
            if item[0] in original:
                original.remove(item[0])
            if item[1] in change:
                change.remove(item[1])

        return render_template("result.html", no_change=no_change, original=original, change=change, name_match=name_match)

    return render_template("index.html", input_data=input_data)
from flask import Flask, render_template, request
from model import InputForm
from numpy import *
from test_compute import *

app = Flask(__name__)


@app.route('/hw4', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        a = form.formula.data                   # String
        b = form.N.data                         # Float
        c = form.independent_variable.data      # String
        d = form.xMin.data                      # Float
        e = form.xMax.data                      # Float
        f = form.yMin.data                      # Float
        g = form.yMax.data                      # Float
        h = form.degree_of_approximation.data   # Float
        i = form.eCurves.data                   # Select
        j = form.legend_loc.data                # Select

        result = compute(a, c, b, d, e, f, g, i, j)

        result_2 = latexSeries(a, c, b, h)

    else:
        result = None
        result_2 = None

    return render_template("view_plain.html", form=form, result=result, result_2=result_2)


if __name__ == '__main__':
    app.run(debug=True)
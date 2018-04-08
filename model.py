import wtforms as wtf
from wtforms import Form, FloatField, validators, StringField, IntegerField, SelectField


class InputForm(Form):
    # string field for fomula
    formula = StringField('note', validators=[validators.InputRequired()])
    # string field for independent var
    independent_variable = StringField('note', validators=[validators.InputRequired()])
    # xMin
    xMin = FloatField(validators=[validators.InputRequired()])
    # xMax
    xMax = FloatField(validators=[validators.InputRequired()])
    # yMin
    yMin = FloatField(validators=[validators.InputRequired()])
    # yMax
    yMax = FloatField(validators=[validators.InputRequired()])
    # float field for deg of approximation
    degree_of_approximation = IntegerField(validators=[validators.InputRequired()])
    # int field for N
    N = FloatField(validators=[validators.InputRequired()])
    # Erase all curves
    eCurves = SelectField(label='', choices=[('yes', 'Yes'),
                                                 ('no', 'No')])
    # Legened location
    legend_loc = SelectField(label='', choices=[('top right', 'Top Right'),
                                                 ('bottom right', 'Bottom Right'),
                                                ('top left', 'Top Left'),
                                                ('bottom left', 'Bottom Left')])

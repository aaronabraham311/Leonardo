from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Form to create sliders for spending type
class sliderForm(FlaskForm):
    income = IntegerField("Income: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_1 = IntegerField("Value 1: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_2 = IntegerField("Value 2: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_3 = IntegerField("Value 3: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_4 = IntegerField("Value 4: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_5 = IntegerField("Value 5: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_6 = IntegerField("Value 6: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    submit = SubmitField('Submit values')
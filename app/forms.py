from flask_wtf import FlaskForm
from wtforms import DecimaRangelField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Form to create sliders for spending type
class sliderForm(FlaskForm):
    slider_value_1 = DecimalRangeField("Value 1: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_value_2 = DecimalRangeField("Value 2: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_value_3 = DecimalRangeField("Value 3: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_value_4 = DecimalRangeField("Value 4: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    slider_value_5 = DecimalRangeField("Value 5: ", validators = [DataRequired(), NumberRange(min = 0, max = 100)])
    submit = SubmitField('Submit values')
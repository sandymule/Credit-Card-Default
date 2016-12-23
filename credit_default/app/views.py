import logging
import json

import pandas as pd
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

from . import app, estimator, target_names

logger = logging.getLogger('app')

class PredictForm(Form):
    """Fields for Predict"""
    # sepal_length = fields.DecimalField('Sepal Length:', places=2, validators=[Required()])
    # sepal_width = fields.DecimalField('Sepal Width:', places=2, validators=[Required()])
    # petal_length = fields.DecimalField('Petal Length:', places=2, validators=[Required()])
    # petal_width = fields.DecimalField('Petal Width:', places=2, validators=[Required()])
    Limit_bal = fields.DecimalField('Limit Balance:', places=2, validators=[Required()])
    Gender_list = [(1, "Male"), (2, "Female")]
    Gender = fields.SelectField("Gender", choices=Gender_list, coerce=int)
    Education_list = [(1, "Graduate school"), (2, "College"), (3, "High school"), (4, "Less than high school")]
    Education = fields.SelectField("Education", choices=Education_list, coerce=int)
    Marriage_list = [(1, "Married"), (2, "Single"), (3, "Separated, Divorced, or Widowed")]
    Marriage = fields.SelectField("Marriage", choices=Marriage_list, coerce=int)
    Age= fields.DecimalField('Age:', places=2, validators=[Required()])
    Percent_1_monthago = fields.DecimalField('Percent Paid 1 Month Ago:', places=2, validators=[Required()])
    Percent_2_monthago = fields.DecimalField('Percent Paid 2 Months Ago:', places=2, validators=[Required()])
    Percent_3_monthago = fields.DecimalField('Percent Paid 3 Months Ago:', places=2, validators=[Required()])
    Percent_4_monthago = fields.DecimalField('Percent Paid 4 Months Ago:', places=2, validators=[Required()])
    Percent_5_monthago = fields.DecimalField('Percent Paid 5 Months Ago:', places=2, validators=[Required()])
    Percent_6_monthago = fields.DecimalField('Percent Paid 6 Months Ago:', places=2, validators=[Required()])

    submit = fields.SubmitField('Submit')

@app.route('/',methods=('GET','POST'))
def predict():
    return render_template('homepage.html')

@app.route('/visualize',methods=('GET','POST'))
def visualize():
    datastuff = []


    """Index page"""
    form = PredictForm()
    # predicted_iris = None
    result = None

    if form.validate_on_submit():
        # store the submitted values

        submitted_data = form.data

        # Retrieve values from form
        # sepal_length = float(submitted_data['sepal_length'])
        # sepal_width = float(submitted_data['sepal_width'])
        # petal_length = float(submitted_data['petal_length'])
        # petal_width = float(submitted_data['petal_width'])
        Limit_bal = float(submitted_data['Limit_bal'])
        Gender = float(submitted_data['Gender'])
        Education = float(submitted_data['Education'])
        Marriage = float(submitted_data['Marriage'])
        Age = float(submitted_data['Age'])
        Percent_1_monthago = float(submitted_data['Percent_1_monthago'])
        Percent_2_monthago = float(submitted_data['Percent_2_monthago'])
        Percent_3_monthago = float(submitted_data['Percent_3_monthago'])
        Percent_4_monthago = float(submitted_data['Percent_4_monthago'])
        Percent_5_monthago = float(submitted_data['Percent_5_monthago'])
        Percent_6_monthago = float(submitted_data['Percent_6_monthago'])

        # Create array from values
        # flower_instance = [sepal_length, sepal_width, petal_length, petal_width]
        default_instance = [Limit_bal, Gender, Education, Marriage, Age,
        Percent_1_monthago, Percent_2_monthago, Percent_3_monthago,
        Percent_4_monthago, Percent_5_monthago, Percent_6_monthago]
        # my_prediction = estimator.predict(flower_instance)
        result = estimator.predict(default_instance)[0] # Target Predicted

        df = pd.DataFrame([{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    }
])


        datastuff = df.to_json(orient="records")
    else:
        print (form.data)

    return render_template('visualize.html',
        form=form,
        # prediction=predicted_iris
        prediction=result, data=datastuff)




@app.route('/predict', methods=('GET', 'POST'))
def index():

    datastuff = []


    """Index page"""
    form = PredictForm()
    # predicted_iris = None
    result = None

    if form.validate_on_submit():
        # store the submitted values

        submitted_data = form.data

        # Retrieve values from form
        # sepal_length = float(submitted_data['sepal_length'])
        # sepal_width = float(submitted_data['sepal_width'])
        # petal_length = float(submitted_data['petal_length'])
        # petal_width = float(submitted_data['petal_width'])
        Limit_bal = float(submitted_data['Limit_bal'])
        Gender = float(submitted_data['Gender'])
        Education = float(submitted_data['Education'])
        Marriage = float(submitted_data['Marriage'])
        Age = float(submitted_data['Age'])
        Percent_1_monthago = float(submitted_data['Percent_1_monthago'])
        Percent_2_monthago = float(submitted_data['Percent_2_monthago'])
        Percent_3_monthago = float(submitted_data['Percent_3_monthago'])
        Percent_4_monthago = float(submitted_data['Percent_4_monthago'])
        Percent_5_monthago = float(submitted_data['Percent_5_monthago'])
        Percent_6_monthago = float(submitted_data['Percent_6_monthago'])

        # Create array from values
        # flower_instance = [sepal_length, sepal_width, petal_length, petal_width]
        default_instance = [Limit_bal, Gender, Education, Marriage, Age,
        Percent_1_monthago, Percent_2_monthago, Percent_3_monthago,
        Percent_4_monthago, Percent_5_monthago, Percent_6_monthago]
        # my_prediction = estimator.predict(flower_instance)
        result = estimator.predict(default_instance)[0] # Target Predicted

        df = pd.DataFrame([{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Over 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Over 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Over 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Over 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Over 4%", "Payment 6 Less Than 5%"]
    },{
        "name": "Payment 6 Over 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Over 5%"]
    },{
        "name": "Payment 6 Less Than 5%",
        "taxonomy": ["Payment 1 Under 0%", "Payment 2 Under 1%", "Payment 3 Under 2%", "Payment 4 Under 3%", "Payment 5 Under 4%", "Payment 6 Less Than 5%"]
    }
])





        datastuff = df.to_json(orient="records")
    else:
        print (form.data)

    return render_template('predict.html',
        form=form,
        # prediction=predicted_iris
        prediction=result, data=datastuff)

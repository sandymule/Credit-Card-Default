# old code from iris example
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.datasets import load_iris
# from sklearn.externals import joblib

#import all the needed imports
import numpy as np
import pandas as pd
import os
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.learning_curve import learning_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# old code from iris example for reference
# if __name__ == "__main__":
#         # Load Iris Data
#         iris_data = load_iris()
#         features = iris_data.data
#         feature_names = iris_data.feature_names
#         target = iris_data.target
#         target_names = iris_data.target_names
#
#         knn = KNeighborsClassifier(n_neighbors=3)  # replace with your own ML model here
#         knn.fit(features, target)
#
#         joblib.dump(knn, 'models/iris_model.pkl')
if __name__ == "__main__":
    #load data
    df = pd.read_csv('default_of_credit_card_clients.csv')
    df = df.dropna()
    df = df.drop('ID', axis = 1)
    df['default payment next month'] = df['default payment next month'].replace(to_replace=0, value="Paid")
    df['default payment next month'] = df['default payment next month'].replace(to_replace=1, value="Default")
    df['LIMIT_BAL'] = df['LIMIT_BAL']/1000

    #makes the percentage columns I was talking about - pct paid 1 is 1 month ago, pct paid 2 is 2 months ago, etc.
    def percent_maker(df):
        for i in range(1,7):
            df[('pct_paid_{}'.format(i))] = df[('PAY_AMT{}'.format(i))] / df[('BILL_AMT{}'.format(i))]
    percent_maker(df)

    #replaces null and infinite values
    df = df.replace({None:0, np.inf:1})

    #new X features for modeling...
    features = df[['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE','pct_paid_1', 'pct_paid_2', 'pct_paid_3',
       'pct_paid_4', 'pct_paid_5', 'pct_paid_6']]
    feature_names = list(features.columns.values)
    target = df['default payment next month']
    target_names = ["Paid", "Default"]

    # run randomforest on data we have
    RF = RandomForestClassifier()
    RF.fit(features, target)
    joblib.dump(RF, 'models/credit_model.pkl')

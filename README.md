# cv_prediction_app

Project objective: to create an application for assessing the risk of cardiovascular diseases (binary classification).
The basic metric in this project is roc_auc.
At the first stage (EDA), the indicators of age, weight, height, pressure were adjusted, and the indicators were also analyzed for multicollinearity. An additional, the body mass index was introduced as new feature.
At the second stage, scaling was carried out, hyperparameters were selected and metrics were evaluated.
At the third stage, the model with the largest metric was selected (an additional metrics was evaluated on test data and important features was identified).
On the fourth stage, the application was created using streamlit.

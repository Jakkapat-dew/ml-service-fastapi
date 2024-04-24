import pandas as pd
from fastapi import UploadFile

# ----------
class Regression():
    def __init__(self, model_conf:RegressionConf, data:Dataset):
        # input
        self.data = data
        self.X = self.data.df[self.data.df_X_columns]
        self.y = self.data.df[self.data.df_y_columns]
        
        # model
        def select_model(self, model_conf:RegressionConf):
            if model_conf.model == "ordinary":
                return linear_model.LinearRegression()
            elif model_conf.model == "lasso":
                return linear_model.Lasso(alpha = model_conf.alpha)
            elif model_conf.model == "ridge":
                return linear_model.Ridge(alpha=model_conf.alpha)        
        self.model = select_model(model_conf)
        self.coef = None
        
        # result
        self.predicted = None
        self.r2_score = None
        self.rmse = None
    
    def train(self):
        self.model.fit(self.X, self.y)
        self.coef = self.model.coef_
        return
    
    def predict(self, x):
        self.predicted = self.model.predict(x) 
        return self.predicted
        
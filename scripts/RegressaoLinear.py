import numpy as np

class RegressaoLinear():

    def __init__(self):
        pass
    
    def fit(self, X, Y):

        try:
            X_ = np.insert(X, 0, 1, axis=1)

            self.X = X_
            self.Y = Y
            self.Beta = np.linalg.inv(X_.transpose() @ X_) @ (X_.transpose() @ Y)
            return self
        
        except Exception as error:
            return print(f"ERROR: {error}")


    
    def predict(self, X_pred):
        try:
            X_pred = np.insert(X_pred, 0, 1, axis=1)
    
            return X_pred @ self.Beta
        
        except Exception as error:
            return print(f"ERROR: {error}")     

    def coef(self):
        try:
        
            return print(["B" + str(i) + f" = {round(j, 2)}" for i, j in enumerate(self.fit())])
        
        except Exception as error:
            return print(f"ERROR: {error}")

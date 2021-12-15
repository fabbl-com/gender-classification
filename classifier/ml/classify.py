import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pickle
from .extract_features import extract_features
import os

base = os.path.dirname(__file__)

original_dataset = pickle.load(open(os.path.join(base, "out", "original_dataset.pkl"), "rb"))
model_rf = pickle.load(open(os.path.join(base, "out", "RandomForestClassifier.sav"), "rb"))
model_gbc = pickle.load(open(os.path.join(base, "out", "GradientBoostingClassifier.sav"), "rb"))
model_svc = pickle.load(open(os.path.join(base, "out", "rbfSVM.sav"), "rb"))

def classify(path):
    test_dataset = extract_features(path)
    appended_dataset=original_dataset.append(test_dataset)
    X = appended_dataset.iloc[:,:].values
    imputer = SimpleImputer(missing_values=0, strategy='most_frequent')
    imputer = imputer.fit(X[:,:])
    X[:, :] = imputer.transform(X[:, :])
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    X_test = np.array(X[-1])
    X_test = X_test.reshape(1, 111)
    y_pred_rf = model_rf.predict(X_test)
    y_pred_gbc = model_gbc.predict(X_test)
    y_pred_svc = model_svc.predict(X_test)
    
    result = {
      "rf": y_pred_rf,
      "gbc": y_pred_gbc,
      "svc": y_pred_svc
    }
    
    return result
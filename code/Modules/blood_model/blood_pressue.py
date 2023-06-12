import joblib
import numpy as np

def predict_blood_pressure(num):
    model2 = joblib.load(r"C:/Users/princ/PycharmProjects/EmoReg/Modules/blood_model/emorecmodel.pickle")
    input_arr2 = np.array([int(num)])
    result2 = model2.predict([input_arr2])
    if (result2 == "Happy"):
        result2 = "positive"
    else:
        result2 = "negative"
    return result2

#print('Pulse rate: ' + predict_blood_pressure(20))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score
from predictions.models import userHistory, usersModel


class DiabetisPrediction():
    def __init__(self):
        self.data = pd.read_csv("predictions\\data\\diabetes.csv")
        self.rfc = GradientBoostingClassifier()

    def addUserHistory(self,data, user_id, prediction):
        HISTORY = usersModel.objects.get(id = user_id)
        predict = "Not Diabetic"
        if prediction == 1:
            predict = "Diabetic"

        if HISTORY:
            HISTORY.userhistory_set.create(
                preg = data[0],
                glucose = data[1],
                BP = data[2],
                insulin = data[3],
                BMI = data[4],
                DPF = data[5],
                age = data[6],
                prediction = predict
            )

    def dataProcessing(self):
        self.data = self.data.drop("SkinThickness", axis = 1)
        self.data.loc[self.data.DiabetesPedigreeFunction >= 0.5, "DiabetesPedigreeFunction"] = 1
        self.data.loc[self.data.DiabetesPedigreeFunction < 0.5, "DiabetesPedigreeFunction"] = 0
        X =  self.data.drop("Outcome", axis=1)
        Y = self.data["Outcome"]
        return X, Y

    def createModel(self):
        X,Y = self.dataProcessing()
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42)
        self.rfc.fit(self.X_train, self.Y_train)

    def predict(self,POST, user_id):
        columns =[
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age"
        ]
        data = [
            int(POST["data[preganancies]"]),
            int(POST["data[glucose]"]),
            int(POST["data[bp]"]),
            int(POST["data[insulin]"]),
            float(POST["data[BMI]"]),
            int(POST["data[DiabetesPedigreeFunction]"]),
            int(POST["data[age]"]),   
        ]
        print(self.rfc.score(self.X_test, self.Y_test))

        y_pred = self.rfc.predict(self.X_test)
        report = classification_report(y_true = self.Y_test, y_pred = y_pred, output_dict = True)
        x_test = pd.DataFrame([data], columns=columns)
        predictions = self.rfc.predict(x_test)


        self.addUserHistory(data, user_id, predictions[0])

        return (predictions[0], report["0"])

import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import numpy as np

class StudentPerformacePrediction():

    def __init__(self):
        self.Std_Per_Pred_model = None
        self.Columns_data = None
        self.feature_count = None

    def load_data(self):
        # Load model
        with open(r"artifacts\Std_Perf_Pred.pkl", "rb") as f:
            self.Std_Per_Pred_model = pickle.load(f)

        # Load columns data
        with open(r"artifacts\Std_Perf_Pred_Columns_data.json", "r") as f:
            self.Columns_data = json.load(f)

        # Use model's feature count (more reliable)
        self.feature_count = self.Std_Per_Pred_model.n_features_in_

    def get_std_perf_pre(self, Gender, AttendanceRate, StudyHoursPerWeek, PreviousGrade, ExtracurricularActivities, ParentalSupport):
        self.load_data()

        # Convert categorical variables using the mappings
        Gender = self.Columns_data["Gender"].get(Gender, -1)
        ParentalSupport = self.Columns_data["ParentalSupport"].get(ParentalSupport, -1)

        if Gender == -1 or ParentalSupport == -1:
            raise ValueError("One or more categorical features are not found in Columns_data")

        # Handle numerical variables
        AttendanceRate = float(AttendanceRate)
        AttendanceRate = np.sqrt(AttendanceRate)
        ExtracurricularActivities = float(ExtracurricularActivities)

        # Prepare test array with correct values
        test_array = np.zeros((1, self.feature_count))
        test_array[0, 0] = Gender
        test_array[0, 1] = AttendanceRate
        test_array[0, 2] = StudyHoursPerWeek
        test_array[0, 3] = PreviousGrade
        test_array[0, 4] = ExtracurricularActivities
        test_array[0, 5] = ParentalSupport

        # Predict performance
        Std_pred_per = np.around(self.Std_Per_Pred_model.predict(test_array)[0])
        return Std_pred_per

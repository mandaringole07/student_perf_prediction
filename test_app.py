from flask import Flask, render_template, request, jsonify
from test_utlis import StudentPerformacePrediction

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/performanceprediction", methods=["POST"])
def performanceprediction():
    data = request.form

    Gender = data.get("Gender")
    AttendanceRate = data.get("AttendanceRate")
    StudyHoursPerWeek = data.get("StudyHoursPerWeek")
    PreviousGrade = data.get("PreviousGrade")
    ExtracurricularActivities = data.get("ExtracurricularActivities")
    ParentalSupport = data.get("ParentalSupport")

    std_pred_perf = StudentPerformacePrediction()
    try:
        predict_perf = std_pred_perf.get_std_perf_pre(
            Gender, AttendanceRate, StudyHoursPerWeek, PreviousGrade, ExtracurricularActivities, ParentalSupport
        )
        return jsonify({"Student_Performance_Prediction": predict_perf})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8090)

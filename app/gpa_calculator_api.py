from flask import Flask, request, jsonify

app = Flask(__name__)


def calculate_gpa(grades):
    grade_points = {
        "A+": 0.7,
        "A": 1.0,
        "A-": 1.3,
        "B+": 1.7,
        "B": 2.0,
        "B-": 2.3,
        "C+": 2.7,
        "C": 3.0,
        "C-": 3.3,
        "D+": 3.7,
        "D": 4.0,
        "D-": 4.3,
        "F": 5.0,
    }
    total_credit_hours = 0
    total_grade_points = 0

    for course in grades:
        credit_hours, grade = course
        if grade in grade_points and credit_hours > 0:
            total_credit_hours += credit_hours
            total_grade_points += grade_points[grade] * credit_hours


    if total_credit_hours == 0:
        return 0.0, "F"  # Return 0 GPA if no valid courses are provided

    gpa = round(total_grade_points / total_credit_hours, 2)
    # Map GPA to German scale
    german_scale = {
        0.7: "A+",
        1.0: "A",
        1.3: "A-",
        1.7: "B+",
        2.0: "B",
        2.3: "B-",
        2.7: "C+",
        3.0: "C",
        3.3: "C-",
        3.7: "D+",
        4.0: "D",
        4.3: "D-",
        5.0: "F"
    }
    
    gpa_german_scale = min(german_scale, key=lambda x: abs(x - gpa))
    letter_grade = german_scale[gpa_german_scale]

    return gpa, letter_grade


@app.route("/calculate_gpa", methods=["POST"])
def calculate_gpa_api():
    try:
        data = request.get_json()
        grades = data["grades"]
        gpa, letter_grade = calculate_gpa(grades)
        print(f'gpa: {gpa}, letter_grade: {letter_grade}')
        response = {"gpa": gpa, "letter_grade": letter_grade}
        return jsonify(response), 200
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return jsonify({"error": error_message}), 400


if __name__ == "__main__":
    app.run(debug=True)

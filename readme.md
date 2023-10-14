# GPA Calculator API

This API calculates GPA (Grade Point Average) based on a given list of course grades. The API accepts input in the form of a JSON payload through Postman, calculates the GPA using the German grading scale, and returns the GPA along with the corresponding letter grade.

## API Endpoint

- **Endpoint:** `/calculate_gpa`
- **Method:** POST
- **Request Payload Format:**
  ```json
  {
      "grades": [
          [6, "A"],
          [4, "B+"],
          [3, "A+"]
      ]
  }
  ```
- Each course grade is represented as a tuple containing credit hours (an integer) and a grade (a string).


## GPA Calculation Details
The GPA is calculated using the following steps:
    1. Input Validation:
        - Invalid courses (negative credit hours or grades not in the grading scale) are ignored.
        - If no valid courses are provided, the GPA is 0.0 and the letter grade is "F".

    2. Grade Points Mapping:
        - Each valid grade is mapped to a corresponding grade point according
          to the German grading scale.

    3. GPA Calculation:
        - Total grade points are calculated by multiplying grade points with credit hours for each valid course.
        - Total credit hours are the sum of credit hours for all valid courses.
        - GPA is calculated by dividing total grade points by total credit hours, rounded to two decimal places.

    4. Letter Grade Mapping:
        - GPA is mapped to the nearest letter grade in the German grading scale.
        - Letter grade is returned in parentheses with the calculated GPA 

## Usage Instructions (Postman)

1. Open Postman.

2. Set the request type to POST.

3. Enter the API endpoint: http://localhost:5000/calculate_gpa

4. In the Body tab, select raw and choose JSON (application/json).

5. Enter your grades data in the specified format
    Example:
    ```
    {
        "grades": [
            [6, "A"],
            [4, "B+"],
            [3, "A+"]
        ]
    }

    ```
6. Click Send to calculate the GPA.


## Response
The API will respond with the calculated GPA and letter grade:
```{
    "gpa": 1.77,
    "letter_grade": "(B+)"
}
```

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gpa-calculator-api

2. Create a virtual environment (optional but recommended):
    ```
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:   ```venv\Scripts\activate```
    - On macOS and Linux: ```source venv/bin/activate```

4. Install the required packages: ```pip install -r requirements.txt```

5. Run the Flask application: ```python gpa_calculator_api.py```


# The API will be accessible at http://localhost:5000/calculate_gpa.
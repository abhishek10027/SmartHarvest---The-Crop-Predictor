from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved GaussianNB model
model = joblib.load('gaussian_nb_model.pkl')

# Define feature columns
feature_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

@app.route('/')
def index():
    """Render the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and predict crop."""
    try:
        # Get input values from the form
        input_data = {feature: float(request.form[feature]) for feature in feature_columns}

        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data])

        # Predict using the model
        prediction = model.predict(input_df)[0]  # Extract the single prediction result

        # Render the result page with the prediction
        return render_template(
            'result.html',
            result_text=f"The recommended crop is: {prediction}"
        )
    except Exception as e:
        # Handle errors (e.g., invalid inputs)
        return render_template('index.html', error=f"Error: {str(e)}")

@app.route('/back', methods=['GET'])
def back():
    """Handle navigation back to the input form."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

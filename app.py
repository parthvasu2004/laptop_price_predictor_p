from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

app = Flask(__name__)

# Load the model
with open('pipe.pkl', 'rb') as file:
    pipe = pickle.load(file)
df = pd.read_pickle('df.pkl')

# Define the expected columns based on the training data
expected_columns = pipe.named_steps['preprocessor'].transformers_[1][2].tolist() + pipe.named_steps['preprocessor'].transformers_[0][2].tolist()

@app.route('/')
def home():
    return render_template('index.html', companies=df['Company'].unique(), types=df['TypeName'].unique(), cpus=df['Cpu brand'].unique(), gpus=df['Gpu brand'].unique(), oss=df['os'].unique())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        company = request.form['company']
        type = request.form['type']
        ram = int(request.form['ram'])
        weight = request.form['weight']
        touchscreen = request.form['touchscreen']
        ips = request.form['ips']
        screen_size = request.form['screen_size']
        resolution = request.form['resolution']
        cpu = request.form['cpu']
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        gpu = request.form['gpu']
        os = request.form['os']

        # Ensure all required inputs are provided and properly converted
        if not weight:
            weight = 0.0
        else:
            weight = float(weight)

        if not screen_size:
            screen_size = 0.0
        else:
            screen_size = float(screen_size)

        # Query preprocessing
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        # Create the query array
        query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
        query = query.reshape(1, -1)
        
        # Ensure the query is a DataFrame for the pipeline to process
        query_df = pd.DataFrame(query, columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'Ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

        # Ensure all expected columns are present
        for col in expected_columns:
            if col not in query_df.columns:
                query_df[col] = 0  # Or some appropriate default value

        # Make the prediction
        prediction = pipe.predict(query_df)[0]
        predicted_price = int(np.exp(prediction))

        return render_template('index.html', prediction_text=f"The predicted price of this configuration is ₹{predicted_price}", companies=df['Company'].unique(), types=df['TypeName'].unique(), cpus=df['Cpu brand'].unique(), gpus=df['Gpu brand'].unique(), oss=df['os'].unique())
    except KeyError as e:
        return f"KeyError: {str(e)}"
    except Exception as e:
        return f"Exception: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

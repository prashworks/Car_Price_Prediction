# Car_Price_Prediction

🚀 Project Pipeline (Step‑by‑Step)
1. Data Collection (01_data_collection.ipynb)

Import required libraries

Load the raw CSV file into a pandas DataFrame

2. Data Cleaning (02_data_cleaning.ipynb)

Remove duplicates

Handle missing values

Correct wrong data types

Save cleaned dataset

3. Exploratory Data Analysis (03_eda.ipynb)

Describe data

Plot distributions

Correlation analysis

Understand key insights

4. Feature Engineering (04_feature_engineering.ipynb)

Select final features

Drop unnecessary columns

Encode categorical variables

Scale numerical columns (if required)

5. Model Building (05_model_building.ipynb)

Load ML‑ready dataset

Split into train/test

Train ML algorithms (Random Forest or others)

Evaluate model accuracy

Save the trained model as .pkl

🖥️ Flask Web Application
app.py

Loads the trained ML model

Creates a Flask server

Accepts user input from HTML form

Returns predicted price

HTML Template (templates/car_price_prediction.html)

User interface (input fields for car details)

Sends data to /predict route

⚙️ How to Run the Project
1. Install required libraries
pip install -r requirements.txt

(If you don't have a requirements file, install Flask, Pandas, NumPy, Scikit‑Learn.)

2. Run the Flask App
python app.py

Then open:

http://127.0.0.1:5000/
📊 Machine Learning Model

Trained using Random Forest Regressor

Takes features such as:

Car model

Year

KM driven

Fuel type

Transmission

Owner type

Outputs predicted price

📦 Output

Accurate price prediction based on trained dataset

Fully functional Flask web app for real‑time prediction

🙌 Author

Prash – Machine Learning & Web Development Enthusiast

Feel free to improve the project, add new features, or build a better UI!

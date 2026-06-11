# CodeAlpha - Car Price Prediction using Machine Learning
## Project Overview
This project predicts the selling price of a car using Machine Learning techniques. The model is trained on historical car data and can estimate car prices based on features such as year, fuel type, transmission type, present price, and kilometers driven.
## Dataset
The dataset contains information about cars including:
* Car Name
* Year
* Selling Price
* Present Price
* Driven Kilometers
* Fuel Type
* Selling Type
* Transmission
* Owner
## Technologies Used
* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
## Machine Learning Algorithm
* Random Forest Regressor
## Project Workflow
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Price Prediction
6. Model Evaluation
7. Data Visualization
## Results
The model achieved:
* Mean Absolute Error (MAE): 0.597
* R² Score: 0.964
This indicates excellent prediction accuracy.
## Visualization
The project includes an Actual vs Predicted Car Price graph to evaluate model performance.
## How to Run the Project
### Install Dependencies
pip install -r requirements.txt
### Run the Project
python main.py
## Project Structure

CAR_PRICE_PREDICTION/
│
├── data/
│   └── car data.csv
│
├── visuals/
│   └── prediction_graph.png
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
## Author
Rakshitha
## Internship
CodeAlpha Data Science Internship

# Crop-Recommendation-System
Fundamentals of AI and ML Project

Name: Mohit Nagar

Reg. no: 25BAI11366
## Overview of the Project
This is a Machine Learning system that predicts the best crop to plant based on soil and environmental data. Using a Random Forest Classification model, the system analyzes 7 key factors: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, Soil pH, and Rainfall. The model learns patterns from agricultural data to help farmers make data-driven decisions, reducing the risk of crop failure and maximizing yield.

## Features
1. Multi-Factor Analysis: Trains on 7 parameters (N, P, K, Temp, Humidity, pH, Rainfall) to provide accurate results.

2. Real-Time Predictions: Predicts from 22 different crop types (e.g., Rice, Maize, Coffee, Cotton) based on user input.

3. High Accuracy: Utilizes the Random Forest algorithm to ensure stable and reliable classifications.

4. Interactive CLI: Users can manually input their soil details into the terminal to get an instant recommendation.

5. Data Persistence: Uses a structured CSV dataset (Crop_recommendation.csv) for training and evaluation.

6. Robust Documentation: Includes a clear folder structure and requirement files for easy deployment.

## Technologies/Tools Used
1. Language: Python 3.8+

2. ML Core: Scikit-Learn (Random Forest Classifier)

3. Data Handling: Pandas

4. Environment: VS Code / Terminal

## Steps to Install & Run the Project
1. Environment Setup: Ensure Python 3.8+, Pandas, and Scikit-Learn are installed.

2. File Organization: Ensure Crop-Recommendation-Code.py and Crop_recommendation.csv are in the Code folder.

3. Run the Project: Open your terminal, navigate to the /Code directory.

4. Execution: The model trains automatically on the provided CSV and prompts the user for soil data.

## Instructions for Testing
1. Run the Script: Verify that the "Model Trained Successfully" message appears in the terminal.

2. Test Rice Prediction: Input high values (N: 90, P: 42, K: 43, Rain: 200) — the model should return RICE.

3. Test Grapes Prediction: Input high Potassium and Phosphorus (K: 200, P: 130) — the model should return GRAPES.

4. Verify Error Handling: Ensure the script runs without crashing if the CSV is present in the correct folder.

5. Check Output: View Output_screenshot.png in the repository to compare your results with the sample run.

6. Evaluate: Check the accuracy score printed in the console to ensure it meets course requirements (>90%).


import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. LOAD THE DATA
try:
    df = pd.read_csv('Crop_Data.csv')
    print("Data loaded successfully from CSV!")
except FileNotFoundError:
    print("Error: Could not find 'Crop_Data.csv'. Make sure the file is in the same folder.")
    exit()

# 2. PREPARE THE BRAIN (The Model)
X = df.drop('label', axis=1) # The inputs (N, P, K, etc.)
y = df['label']              # The output (The Crop Name)

# Create and train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# 3. INTERACTIVE SECTION
print("\n--- Welcome to the Farmer's Assistant ---")
print("Please enter the following soil details:")

# We use float(input()) so the user can type in numbers
n = float(input("Nitrogen (N): "))
p = float(input("Phosphorus (P): "))
k = float(input("Potassium (K): "))
temp = float(input("Temperature (in °C): "))
hum = float(input("Humidity (in %): "))
ph = float(input("Soil pH level: "))
rain = float(input("Average Rainfall (in mm): "))

# The AI makes a prediction based on what you typed
new_data = [[n, p, k, temp, hum, ph, rain]]
prediction = model.predict(new_data)

print("-" * 40)
print(f"RESULT: You should plant {prediction[0].upper()} for the best yield!")
print("-" * 40)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta

# Read the CSV file
data = pd.read_csv('stock_data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data based on the 'Date' column in ascending order
data = data.sort_values(by='Date')

# Calculate the number of days between each date and the minimum date
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# Split the data into features (X) and target variable (y)
X = data['Days'].values.reshape(-1, 1)
y = data['Price'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Calculate the number of days for the next month
current_date = data['Date'].max()
next_month_date = current_date + timedelta(days=30)
next_month_days = (next_month_date - data['Date'].min()).days

# Predict the stock price for the next month
next_month_price = model.predict([[next_month_days]])

print("Predicted stock price for the next month:", next_month_price[0])

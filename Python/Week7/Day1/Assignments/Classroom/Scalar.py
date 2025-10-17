from sklearn preprocessing import MinMaxScaler import numpy as np
# Sample training data
X_train = np.array([[1, 2], [3, 4], [5, 6]])
# Create a StandardScaler instance
scaler = MinMaxScaler()
print ("Fit", scaler fit(X_train))
print("Mean", scaler.mean_)
print("Transform", scaler. transform(X_train))
# Apply fit_transform to the training data
X_train_scaled = scaler. fit_transform(_train)
print("Original Training Data: \n", X_train)
print("Scaled Training Data: \n", X_train_scaled)
22
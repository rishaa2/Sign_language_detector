import pickle
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import train_test_split

# Load the model
model_path = 'C:/Users/risha/Documents/PROJECTS/Sign detection using Python/model.p'
data_path = 'C:/Users/risha/Documents/PROJECTS/Sign detection using Python/data.pickle'

# Load the model
model_dict = pickle.load(open(model_path, 'rb'))
model = model_dict['model']

# Load the data
data_dict = pickle.load(open(data_path, 'rb'))
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split the data for testing
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Predict using the model
y_predict = model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_predict, y_test) * 100
print(f'Accuracy: {accuracy:.2f}%')

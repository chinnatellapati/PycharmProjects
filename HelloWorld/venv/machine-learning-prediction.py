# we need to write this code on Jupyter browser shell.
# After buiding a model , we need to measure it's accurcy. If results are not accurate, we need to chnage the algorithm or clean input dataset
#To measure accuracy - First we need to split the dataset into training and testing
# More data we train our model , cleaner the data we will get better results . If our data incomplete, null, our model learn bad patterns


import pandas as pd
from sklearn.tree import DecisionTreeClasifier
from sklearn.model_selection import train_split_test
from sklean.matrix import accuracy_score


music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['dender'])
y = music_data['gender']
X_train, X_test, y_train,y_test = train_split_test(X,y, test_size=0.2) # This function return a tuple, we can unpack into 4 variables
music_data


model = DecisionTreeClasifier()
model.fit(X_train,y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
score





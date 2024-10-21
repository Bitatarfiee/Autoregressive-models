#Nonlinear AR model

def create_lagged_sequences(y, p):
    # Number of training data points
    n = y.shape[0] # <COMPLETE THIS LINE>
    # Construct the regression matrix
    Phi = np.zeros((n-p,p))               
    for j in range(p):
        #Phi[:,j] =y[p-j-1:n-j] # <COMPLETE THIS LINE>
        Phi[:,j] =y[p-j-1:n-j-1] # <COMPLETE THIS LINE>
    return Phi
        

Phi_train = create_lagged_sequences(train, p)  
#print(X_train.shape)
NAR = MLPRegressor(hidden_layer_sizes=(10,), activation='relu', solver='adam', max_iter=1000, random_state=41, 
                   learning_rate_init=0.01) 
yy = train[p:] 
model=NAR.fit(Phi_train,yy)

Phi_test = create_lagged_sequences(detrended_data, p)
y_predict=model.predict(Phi_test)

Year = data["Year"]
# Selecting corresponding Year
train_Year = Year[:tp]
valid_Year = Year[tp:]

y_train_pred= y_predict[:len(train) - p]
y_valid_pred = y_predict[len(train) - p:]
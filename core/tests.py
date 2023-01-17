from django.test import TestCase

#importing required libraries 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

#computing the accuracy of the model performance
acc_train_lr2 = lr2.score(X1_train, y1_train)
acc_test_lr2 = lr2.score(X1_test, y1_test)

#computing root mean squared error 
print("Linear Regression Ridge: Accuracy on training Data: {:.3f}".format(acc_train_lr2))
print("Linear Regression Ridge: Accuracy on test Data: {:.3f}".format(acc_test_lr2))
print('\nLinear Regression Ridge: The RMSE of the training set is:',np.sqrt(mean_squared_error(y1_train,y_train_lr2)))
print('Linear Regression Ridge: The RMSE of the testing set is:',np.sqrt(mean_squared_error(y1_test,y_test_lr2)))
print('\nLinear Regression Ridge: The MAE of the training set is:',mean_absolute_error(y1_train,y_train_lr2))
print('Linear Regression Ridge: The MAE of the testing set is:',mean_absolute_error(y1_test,y_test_lr2))
print('\nLinear Regression Ridge: The MSE of the training set is:',mean_squared_error(y1_train,y_train_lr2))
print('Linear Regression Ridge: The MSE of the testing set is:',mean_squared_error(y1_test,y_test_lr2))
print('\nLinear Regression Ridge: The R Squared (R2) of the testing set is:',r2_score(y1_train,y_train_lr2))
print('Linear Regression Ridge: The R Squared (R2) of the testing set is:',r2_score(y1_test,y_test_lr2))

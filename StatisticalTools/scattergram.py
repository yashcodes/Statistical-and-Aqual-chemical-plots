import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as metrics
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

def linear_regression(data_fn):
	
	reader = pd.read_csv(data_fn)

	x_name = reader.iloc[:, 0].name
	y_name = reader.iloc[:, 1].name 

	data_X = reader.iloc[:, 0].values
	data_y = reader.iloc[:, 1].values

	# Create linear regression object
	regr = linear_model.LinearRegression()

	# Train the model using the training sets
	regr.fit(data_X.reshape(-1,1), data_y)

	# Make predictions using the testing set
	data_y_pred = regr.predict(data_X.reshape(-1,1))

	# Writing Summary
	explained_variance=metrics.explained_variance_score(data_y, data_y_pred)
	mean_absolute_error=metrics.mean_absolute_error(data_y, data_y_pred)
	mse = metrics.mean_squared_error(data_y, data_y_pred) 
	mean_squared_log_error = metrics.mean_squared_log_error(data_y, data_y_pred)
	median_absolute_error=metrics.median_absolute_error(data_y, data_y_pred)

	f = open("summary_lin_reg.txt", "w+")
	f.write('Summary of Linear Regression model:\n\n')
	f.write('      Number of data values............... %s\n'%(str(len(data_X))))
	f.write('      Coefficients........................ %s\n'%(str(regr.coef_)))
	f.write('      Intercept........................... %s\n'%(str(regr.intercept_)))
	f.write('      explained_variance.................. %s\n'%(str(explained_variance)))
	f.write('      Mean squared log error............ %s\n'% (str(round(mean_squared_log_error,4))))
	f.write('      Coefficient of determination(r2).... %.2f\n'% r2_score(data_y, data_y_pred))
	f.write('      Mean absolute error (MAE)........... %s\n' %(str(round(mean_absolute_error,4))))
	f.write('      Mean square error (MSE)............. %s\n' %(str(round(mse,4))))
	f.write('      Root mean square error (RMSE)....... %s\n' %(str(round(np.sqrt(mse),4))))
	f.close()

	plt.scatter(data_X, data_y,  color='r')
	plt.plot(data_X, data_y_pred, color='black')
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.title('Scattergram')

	plt.grid(True, which = "both")	
	plt.show()

	return
	

def poly_regression(data_fn, degree = 2):

	reader = pd.read_csv(data_fn)

	x_name = reader.iloc[:, 0].name
	y_name = reader.iloc[:, 1].name 

	data_X = reader.iloc[:, 0].values
	data_y = reader.iloc[:, 1].values

	poly_reg = PolynomialFeatures(degree = degree)
	X_poly = poly_reg.fit_transform(data_X.reshape(-1, 1))

	model = LinearRegression()
	model.fit(X_poly, data_y)

	data_y_pred = model.predict(X_poly)

	
	# Writing Summary
	explained_variance=metrics.explained_variance_score(data_y, data_y_pred)
	mean_absolute_error=metrics.mean_absolute_error(data_y, data_y_pred)
	mse = metrics.mean_squared_error(data_y, data_y_pred) 
	mean_squared_log_error = metrics.mean_squared_log_error(data_y, data_y_pred)
	median_absolute_error=metrics.median_absolute_error(data_y, data_y_pred)

	f = open("summary_poly_reg.txt", "w+")
	f.write('Summary of Polynomial Regression of order %s model:\n\n' %(str(degree)))
	f.write('      Number of data values............... %s\n'%(str(len(data_X))))
	f.write('      explained_variance.................. %s\n'%(str(explained_variance)))
	f.write('      Mean squareded log error............ %s\n'% (str(round(mean_squared_log_error,4))))
	f.write('      Coefficient of determination(r2).... %.2f\n'% r2_score(data_y, data_y_pred))
	f.write('      Mean absolute error (MAE)........... %s\n' %(str(round(mean_absolute_error,4))))
	f.write('      Mean square error (MSE)............. %s\n' %(str(round(mse,4))))
	f.write('      Root mean sqaure error (RMSE)....... %s\n' %(str(round(np.sqrt(mse),4))))
	f.close()

	plt.scatter(data_X, data_y, color='red')
	plt.plot(data_X, data_y_pred, color='blue')
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.title('Scattergram')
	plt.show()
	return
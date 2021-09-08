import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def excel_plotter(excel_file,sheet):
	data = pd.read_excel(excel_file, sheet_name=sheet,header= None, skiprows=1)
	data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)']



	t = data['Time (s)']
	x = data['Gyroscope x (rad/s)']
	y = data['Gyroscope y (rad/s)']
	z = data['Gyroscope z (rad/s)']

	plt.plot(t, x, 'g--', label = 'x-axis' )
	plt.plot(t, y, 'b--', label = 'y-axis')
	plt.plot(t, z, 'r--', label= 'z-axis')

	plt.legend(loc ='upper left')
	plt.xlabel('Time (s)')
	plt.ylabel('Angular velocity (rad/s)')
	plt.grid()
	plt.show()



'''excel_file = 'z_axis.xls'
z_data = pd.read_excel(excel_file, sheet_name=2,header= None,skiprows=1)
z_data.columns = ['Time (s)', 'Gyroscope x (rad/s)','Gyroscope y (rad/s)', 'Gyroscope z (rad/s)','Absolute (rad/s)']



t = z_data['Time (s)']
x = z_data['Gyroscope x (rad/s)']
y = z_data['Gyroscope y (rad/s)']
z = z_data['Gyroscope z (rad/s)']

plt.plot(t, x, 'g--', label = 'x-axis' )
plt.plot(t, y, 'b--', label = 'y-axis')
plt.plot(t, z, 'r--', label= 'z-axis')

plt.legend(loc ='upper left')
plt.xlabel('Time (s)')
plt.ylabel('Angular velocity (rad/s)')
plt.show()'''




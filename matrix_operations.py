import numpy as np 
from math import cos , sin
# Projection matrix
projection = np.array([
	[1 , 0 , 0 ],
	[0 , 1 , 0 ],
	[0 , 0 , 0 ],
	[0 , 0 , 0 ]
])
# Rotation matrix. Will implement a better rotation matrix and projection matrix math later
def rotate(rotation , point):

	# Rotate x 
	r_x = np.array([
		[1 , 0 , 0],
		[0 , cos(rotation[0]) , -sin(rotation[0]) ],
		[0 , sin(rotation[0]) , cos(rotation[0])]
	])
	# Rotate y
	r_y = np.array([
		[cos(rotation[1]) , 0 , sin(rotation[1])],
		[0 , 0 , 0],
		[-sin(rotation[1]) , 0 , cos(rotation[1])]
	])
	# Rotate z 
	r_z = np.array(
		[
			[cos(rotation[2]) , -sin(rotation[2]) , 0],
			[sin(rotation[2]) , cos(rotation[2]) , 0],
			[0 , 0 , 1]
		]
	)
	new_point = np.dot(r_x, point)
	new_point = np.dot(r_y , new_point)
	new_point = np.dot(r_z , new_point)
	return new_point
# function for translating the point in 3D space.(Poorly implemented. Will add more math later )
def translate_point(translation , point):
	new_point = point.copy()
	new_point[0] += translation[0]
	new_point[1] += translation[1]
	new_point[2] += translation[2]
	return new_point
# Function for projecting the points in the mesh. will implement in a better manner later
def project(point):
	try:
		return np.dot(projection , point)
	except:
		print(point)

def rotate_x(rotation , point):
	# Rotate x 
	r_x = np.array([
		[1 , 0 , 0],
		[0 , cos(rotation[0]) , -sin(rotation[0]) ],
		[0 , sin(rotation[0]) , cos(rotation[0])]
	])
	new_point = np.dot(r_x, point)
	return new_point

def rotate_y(rotation , point):
	# Rotate x 
	r_y = np.array([
		[cos(rotation[1]) , 0 , sin(rotation[1])],
		[0 , 1 , 0],
		[-sin(rotation[1]) , 0 , cos(rotation[1])]
	])
	new_point = np.dot(r_y, point)
	return new_point

def rotate_z(rotation , point):
	# Rotate z 
	r_z = np.array(
		[
			[cos(rotation[2]) , -sin(rotation[2]) , 0],
			[sin(rotation[2]) , cos(rotation[2]) , 0],
			[0 , 0 , 1]
		]
	)
	new_point = np.dot(r_z , point)
	return new_point
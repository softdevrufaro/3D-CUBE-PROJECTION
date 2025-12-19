import pygame as pg  
import numpy as np
from settings import * 
from matrix_operations import *

class cube: 
	def __init__(self , position , size):
		self.position = position
		self.size = size
		self.mesh ={
			"A":np.multiply(np.array([0 , 0 , 0]) , self.size),
			"B":np.multiply(np.array([0 , 1 , 0]) , self.size),
			"C":np.multiply(np.array([1 , 1 , 0]) , self.size),
			"D":np.multiply(np.array([1 , 0 , 0]) , self.size),
			"E":np.multiply(np.array([1 , 1 , 1]) , self.size),
			"F":np.multiply(np.array([1 , 0 , 1]) , self.size),
			"G":np.multiply(np.array([0 , 0 , 1]) , self.size),
			"H":np.multiply(np.array([0 , 1 , 1]) , self.size) 
		}
		self.vertices = {
			"i":[self.mesh["A"] , self.mesh["B"]],
			"ii":[self.mesh["B"] , self.mesh["C"]],
			"iii":[self.mesh["C"] , self.mesh["D"]],
			"iv":[self.mesh["D"] , self.mesh["A"]],
			"v":[self.mesh["G"] , self.mesh["H"]],
			"vi":[self.mesh["H"] , self.mesh["E"]],
			"vii":[self.mesh["E"] , self.mesh["F"]],
			"viii":[self.mesh["F"] , self.mesh["G"]],
			"ix":[self.mesh["A"] , self.mesh["G"]] , 
			"x":[self.mesh["B"] , self.mesh["H"]] , 
			"xi":[self.mesh["C"] , self.mesh["E"]],
			"xii":[self.mesh["D"] , self.mesh["F"]]
		}
		self.rotation = [0 , 0 , 0]
	# The function that will draw the cube on the screen
	def display(self , screen):
		# fetching the projection data first
		projection = self.prepare_projection()
		for key in projection[0].keys():
			point1 = projection[0][key][0]
			point2 = projection[0][key][1]
			# translating the vertice points
			# first point
			point1[0] += self.position[0]
			point1[1] += self.position[1]
			point1[2] += self.position[2]
			# Second point
			point2[0] += self.position[0]
			point2[1] += self.position[1]
			point2[2] += self.position[2]
			# Drawing the vertices
			pg.draw.line(screen , white , (point1[0] , point1[1]) , (point2[0] , point2[1]))
		for key in projection[1].keys():
			point = projection[1][key]
			# Was running into errors thus why i decided to calculate translation like this. will fix at a later date
			point[0] += self.position[0]
			point[1] += self.position[1]
			point[2] += self.position[2]
			pg.draw.circle(screen , red , (point[0] ,point[1]) ,3)
	
	# The function to prepare the projection data 
	def prepare_projection(self):
		# Usually players will only see the vertices but for this project i will display the corners and the vertices of the cube as well
		vertice_projection = {}
		nodes_projection = {}
		for key in self.vertices.keys():
			point1 = self.vertices[key][0]
			point2 = self.vertices[key][1]
			# Applying rotations ot the points 
			# First point
			point1 = rotate_x(self.rotation , point1)
			point1 = rotate_y(self.rotation , point1)
			point1 = rotate_z(self.rotation , point1)
			#Second point
			point2 = rotate_x(self.rotation , point2)
			point2 = rotate_y(self.rotation , point2)
			point2 = rotate_z(self.rotation , point2)
			#Adding the new vertice as a proper projection vertice
			vertice_projection[key] = [np.dot(projection , point1) , np.dot(projection,point2)]
		for key in self.mesh.keys():
			point = self.mesh[key]
			point = rotate_x(self.rotation , point)
			point = rotate_y(self.rotation , point)
			point = rotate_z(self.rotation , point)
			nodes_projection[key] = np.dot(projection , point)
		return (vertice_projection , nodes_projection) 
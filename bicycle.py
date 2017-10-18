import math
import numpy as np

# page 9: bike benchmark
# page 21: coefficient equations
# page 62: simplified bike benchmark

class Bike:
	def __init__(self):
		self.w = 1.02
		self.c = 0.08
		self.l = math.pi / 10.0
		self.g = 9.81

		self.rR = 0.3
		self.mR = 2.0

		self.IRxx = 0.0603
		self.IRyy = 0.12

		self.xB = 0.3
		self.zB = -0.9
		self.mB = 85.0

		self.IBxx = 9.2
		self.IBxz = 2.4
		self.IByy = 11
		self.IBzz = 2.8

		self.xH = 0.9
		self.zH = -0.7
		self.mH = 4.0

		self.IHxx = 0.05892
		self.IHxz = -0.00756
		self.IHyy = 0.06
		self.IHzz = 0.00708

		self.rF = 0.35
		self.mF = 3.0

		self.IFxx = 0.1405
		self.IFyy = 0.28

	def set_coeffs(self):
		mT = self.mR + self.mB + self.mH + self.mF

		x_coords = np.array([self.xB, self.xH, self.w])
		x_masses = np.array([self.mB, self.mH, self.mF])

		z_coords = np.array([-self.rR, self.zB, self.zH, -self.rF])
		z_masses = np.concatenate([self.mR], x_masses)

		xT = np.dot(x_coords, x_masses) / mT
		zT = np.dot(z_coords, z_masses) / mT

		ITxx = np.sum([self.IRxx, self.IBxx, self.IHxx, self.IFxx]) + \
		       np.dot(z_masses, z_coords ** 2)
		ITxz = self.IBxz + self.IHxz - \
		       np.sum(x_coords * x_masses * z_coords[1:])

		IRzz = IRxx
		IFzz = IFxx
		ITzz = IRzz + IFzz + self.IBzz + self.IHzz + \
		       np.dot(x_masses, x_coords ** 2)

		x_masses_f = x_masses[1:]
		x_coords_f = x_coords[1:]
		z_coords_f = z_coords[1:]

		mA = np.sum(x_masses_f)
		xA = np.dot(x_coords_f, x_masses_f) / mA
		zA = np.dot(z_coords_f, x_masses_f) / mA

		IAxx = self.IHxx + self.IFxx + \
		       np.dot(x_masses_f, (z_coords_f - zA) ** 2)
		IAxz = self.IHxz - np.sum()
import math
origin = [7,5]
#pts = [[2, 3], [5, 2], [4, 1], [3.5, 1], [1, 2], [2, 1], [3, 1], [3, 3], [4, 3]]
def clockwiseangle_and_distance(point):
	refvec = [0,1]
	# Vector between point and the origin: v = p - o
	vector = [point[0]-origin[0], point[1]-origin[1]]
	# Length of vector: ||v||
	lenvector = math.hypot(vector[0], vector[1])
	# If length is zero there is no angle
	if lenvector == 0:
		return -math.pi, 0
	# Normalize vector: v/||v||
	normalized = [vector[0]/lenvector, vector[1]/lenvector]
	dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
	diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
	angle = math.atan2(diffprod, dotprod)
	# Negative angles represent counter-clockwise angles so we need to subtract them
	# from 2*pi (360 degrees)
	if angle < 0:
		return 2*math.pi+angle, lenvector
	# I return first the angle because that's the primary sorting criterium
	# but if two vectors have the same angle then the shorter distance should come first.
	return angle, lenvector

def main():
	pts=[[35, 45], [30, 30], [45, 45], [50, 30], [35, 20], [45, 20]]
	origin=pts[0]
	pts=order(pts,origin)
	print(pts)

def order(pts,origin):
	a=sorted(pts, key=clockwiseangle_and_distance)
	return a

if __name__=='__main__':
	main()
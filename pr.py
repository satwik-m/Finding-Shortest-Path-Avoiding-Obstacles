from quickhull import *
import order
from project import *

def main():
	#Obstacles=[ [ [5,20,25,20,15,5,10,10] , [ 0,0,20,30,30,25,20,5] ] , [ [15,25,20] , [45,45,65]] ,
	#[ [35,40,45,50,45,35,30] , [20,30,20,30,45,45,30]] ]
	Obstacles=[ [[5,10,15,13,10,8],[15,20,15,25,30,25]] , [[ 14,30,30,20,14],[30,30,60,50,70]] ,
	[ [35,45,40,35] , [15,15,30,25]]]
	#Obstacles= [ ]
	o=len(Obstacles)
	global origin
	s=[0,0]
	d=[60,60]
	x=[]
	y=[]
	#n=int(input("enter no of points:"))
	convexhull = [[] for i in range(o)]
	print('Convex polygons of the obstacles : ')
	for i in range(o):
		x=Obstacles[i][0]
		y=Obstacles[i][1]
		convexhull[i]=quickhull(x,y)
		#print(convexhull[i])
		order.origin=convexhull[i][0]
		convexhull[i]=order.order(convexhull[i],order.origin)
		print(convexhull[i])

	l=convexhull
	#G=makegraph(convexhull)
	v,e=0,0
	S=(0,0)
	D=(60,60)
	for i in range(len(l)):
		for j in range(len(l[i])):
			l[i][j]=tuple(l[i][j])
	VG=vgraph()
	VG.findEdges(l,S,D)
	for i in VG.adj:
		v+=1
		for j in VG.adj[i]:
			e+=1
	#print(v,e)
	L=AdjLst(v,e)
	d={}
	c=0
	for i in VG.adj:
		d[i]=c
		c+=1
	#l=[[None,None] for i in range(v)]
	c=0
	#d=sorted(d,key=lambda x :x[1])
	#for i in d:
		#print(d[i])
	for i in d:
		#l[c][0]=i[0]
		#l[c][1]=i[1]
		L.head[d[i]].x=i[0]
		L.head[d[i]].y=i[1]

	for i in d:
		for j in VG.adj[i]:
			L.form(d[i],d[j])

	for i in range(len(L.head)):
		if(L.head[i].x == S[0] and L.head[i].y == S[1]):
			s=L.head[i].value

	for i in range(len(L.head)):
		if (L.head[i].x == D[0] and L.head[i].y == D[1]):
			d = L.head[i].value

	if s<v:
		L.head[s].dist=0
		L.Dijkstra(s)
		L.printlst(d)
	else:
		print("vertex doesnot exist in given graph")
		

if __name__ == '__main__':
	main()
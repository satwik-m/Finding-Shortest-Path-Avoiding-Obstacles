def differ(s,p,r,q,spr,convexhull):
	x1=p[0]
	x2=r[0]
	y1=p[1]
	y2=r[1]
	for i in range(len(s)):
		x=q[0]
		y=q[1]
		if (x-x1)*(y2-y1)-(y-y1)*(x2-x1) > 0:
			x=s[i][0]
			y=s[i][1]
			if (x-x1)*(y2-y1)-(y-y1)*(x2-x1) <0:
				spr.append([x,y])
		elif (x-x1)*(y2-y1)-(y-y1)*(x2-x1) < 0:
			x=s[i][0]
			y=s[i][1]
			if (x-x1)*(y2-y1)-(y-y1)*(x2-x1) > 0:
				spr.append([x,y])


def findhull(s,convexhull,p,q):
	if len(s)==0:
		return
	num=p[1]-q[1]
	den=p[0]-q[0]
	if den==0:
		c =  p[0]
		max = 0
		r = [0, 0]
		for i in range(len(s)):
			if abs(s[i][0] - c) >= max:
				r[0] = s[i][0]
				r[1] = s[i][1]
				max = s[i][0]- c

	else:
		m=num/den
		c=p[1]-m*p[0]
		max=0
		r=[0,0]
		for i in range(len(s)):
			if abs(m*s[i][0]-s[i][1]+c) >= max:
				r[0]=s[i][0]
				r[1]=s[i][1]
				max=abs(m*s[i][0]-s[i][1]+c)

	#print(r)
	convexhull.append([r[0],r[1]])
	spr=[ ]
	sqr=[ ]
	differ(s,p,r,q,spr,convexhull)
	differ(s,q,r,p,sqr,convexhull)
	findhull(spr,convexhull,p,r)
	findhull(sqr,convexhull,q,r)


def quickhull(x,y):
	n=len(x)
	if n==0:
		return
	convexhull = []

	minkey=0
	maxkey=0
	min=x[0]
	max=x[0]
	for i in range(n):
		if x[i] == min:
			if y[i]<=y[minkey]:
				min =x[i]
				minkey=i
		if x[i] == max:
			if y[i]<=y[maxkey]:
				max =x[i]
				maxkey=i
		if x[i] > max:
			max =x[i]
			maxkey=i
		if x[i] <min:
			min =x[i]
			minkey=i
	convexhull.append([x[minkey],y[minkey]])
	convexhull.append([x[maxkey],y[maxkey]])
	s1=[]
	s2=[]
	num=convexhull[0][1]-convexhull[1][1]
	den=convexhull[0][0]-convexhull[1][0]
	p=[ convexhull[0][0],convexhull[0][1]]
	q=[ convexhull[1][0],convexhull[1][1]]
	if den!=0:
		m=num/den
		c=p[1]-(m * p[0])

		for i in range(len(x)):
			if (m*x[i]-y[i]+c)>0:
				s2.append([x[i],y[i]])
			elif((m*x[i]-y[i]+c)<0):
				s1.append([x[i],y[i]])
	else:
		m=float('inf')
		c=-p[0]

		for i in range(len(x)):
			if (x[i]+c)>0:
				s2.append([x[i],y[i]])
			elif((x[i]+c)<0):
				s1.append([x[i],y[i]])

	#print(s1,s2)
	findhull(s1,convexhull,p,q)
	findhull(s2,convexhull,p,q)
	return convexhull

def main():
	#x=[7,10,10,7]
	#y=[3,3,5,5]
	x=[ 14,30,30,20,14]
	y=[30,30,60,50,70]
	#n=int(input("enter no of points:"))
	ch=quickhull(x,y)
	print(ch)

if __name__ == '__main__':
	main()
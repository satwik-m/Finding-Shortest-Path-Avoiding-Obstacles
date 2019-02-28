# Finding-Shortest-Path-Avoiding-Obstacles

![visibilitygraph](https://user-images.githubusercontent.com/31380861/53540708-a1caa680-3b3c-11e9-9c70-f733bbc3ab26.png)

* All the files are to be put in the same directory and run.
* The project is to find the shortest possible path avoiding a given a set of obstacles in the plane.
* We first form the convex hulls of all the obstacles given to us. This is done with the quickhull.py file. 
* We use the order.py file to order the vertices obtained from the quickhull.py file which are fed into project.py file. 
* This file function is to form the visibility graph taking the obtained convex hulls.
* Now , we apply Dijkstra's over the visibility graph and then obtain the shortest path from a given source to a destination.

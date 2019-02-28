# Finding-Shortest-Path-Avoiding-Obstacles
All the files are to be put in the same directory and run.

![Test Image 2](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiF4r2Xwd3gAhUJL48KHVmNDssQjRx6BAgBEAU&url=http%3A%2F%2Fwww.gamasutra.com%2Fblogs%2FMattKlingensmith%2F20130907%2F199787%2FOverview_of_Motion_Planning.php&psig=AOvVaw0gAmR2lFeBG0Hu76FJp2eP&ust=1551411693080163)

* The project is to find the shortest possible path avoiding a given a set of obstacles in the plane.
* We first form the convex hulls of all the obstacles given to us. This is done with the quickhull.py file. 
* We use the order.py file to order the vertices obtained from the quickhull.py file which are fed into project.py file. 
* This file function is to form the visibility graph taking the obtained convex hulls.
* Now , we apply Dijkstra's over the visibility graph and then obtain the shortest path from a given source to a destination.

###create a randomwalk class to generate randomwalk!
#create a class of random set of points to determine which direction to talk
#take 5000 random walks in different directions
from random import choice
class Randomwalk():

    def __init__(self, points):
        self.points = points
#START AT ORIGIN!!
        self.x_points = [0]
        self.y_points = [0]
#function takes 50000 random walks in different directions and adds to x_points/y_points lists
        
    def fill_walk(self):
        num = 0
        while num < self.points:
            #-1 is left, 0 no move, and 1 is move right
            x_point = choice([-1,1])
            #number of steps to move left or right
            x_choice = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_point * x_choice

            #-1 is down, 0 at origin, and 1 is up
            y_point = choice([-1,1])
            #number of steps to move up and down!
            y_choice = choice([0,1,2,3,4,5,6,7,8])
            y_step = y_point * y_choice

            #skip if both x and y positions are at 0 and don't add them to list!
            if ((x_step == 0) and (y_step == 0)):
                continue
            #add the next x_step/y_step to last value (self.x_points[-1]) stored in x_points and y_points
#START BY ADDING THE ORIGIN POINT TO X_STEP/Y_STEP!!
# plt.axes().get_xaxis().set_visible(False)
#>>> plt.axes().get_yaxis().set_visisble(False)
#IF YOU DON'T ADD TO X_STEP, IT'LL ONLY PRINT FROM -4 TO 4 AND NOT DIFF VALUES!
            next_x = self.x_points[-1] + x_step
            next_y = self.y_points[-1] + y_step
            self.x_points.append(next_x)
            self.y_points.append(next_y)
            num = num + 1
        print (self.x_points)
        print (self.y_points)

game = Randomwalk(1000)
game.fill_walk()
##get rid of the axes and the names
##plt.axes().get_xaxis().set_visible(False)
##plt.axes().get_yaxis().set_visisble(False)

##num_points = list(range(1,5001,1))
###COLOR THE POINTS IN ORDER through the gradient according to num_points!
##plt.scatter(walk_path.x_points, walk_path.y_points, c=num_points, cmap=plt.cm.Blues, edgecolor='None', s=15)
##plt.show()
##
##sample = Randomwalk()
##sample.fill_walk()

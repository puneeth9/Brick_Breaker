Startup:
At the start bricks are arranged in 5 rows of which some are breakable(whose color dependes on their strength) and unbreakable(white colour) . Breakable bricks of strength >=5 are of blue colour , strength = 4 are green in colour , strength = 3 are yellow in colour,strength = 2 are red in colour,strength = 1 are black in colour.A brick breaks once its strength is 0.
Movement:
Use A and D keys to move the paddle to left and right respectively . Press spacebar to release the ball initially . 
Collisions:
The collisions of ball with the brick and wall are handled by reversing the directions of the ball in respective directions . Velocity of ball in the horizontal direction after paddle collision depends on the place where it hit the paddle . 
OOPS Concepts:
Inheritance:A common class Common_object is Inherited by every object
Polymorphism:Some methods in Powerup class are overrided by the children of Powerup class i.e.. Expand,Shrink,...
Encapsulation:Class and Object implementation is used everywhere
Abstraction:All variable are private and the variable which are need to be accesed by some objects are accesed by some getter and setter functions
Score increases if it hits a breakable brick
Powerups:
Expand: Expands the paddle
Shrink: Shrinks the paddle
Fast Ball : Increases the speed of the ball
Thru Ball: Breaks all the bricks(Even unbreakable) on collision.
Paddle Grab:Paddle grabs the ball on its collision with the ball
# Brick_Breaker

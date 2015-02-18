from swampy.World import World
import copy


class Rectangle( object ):
    """Represents a Rectangle.

    Attribute: lower-left corner, upper-right cornner, color.
    """


class Point( object ):
    """Represents a Point with 2-D space.

    Attribute: [x,y]
    """


class Circle( object ):
    """Represents a Circle.

    Attribute: the cordinate pair of the center, radius, color.
    """


class Triangle( object ):
    """Represents a Triangle.

    Attribute: three corners, color.
    """


class Trapezoidal( object ):
    """Represents a Trapezoidal.

    Attribute: four corners, color.
    """


def draw_rectangle( canv, rect ):
    """Draws a representation of the Rectangle on the Canvas.
    """
    bbox = [rect.lower_left_corner, rect.lower_right_corner]
    canv.rectangle( bbox, ootlone = None, fill = rect.color )


def draw_point( canv, point ):
    """Draws a representation of the Point on the Canvas.
    """
    canv.circle( point, 0, outline = None )


def draw_circle( canv, circle ):
    """Draws a representation of the Circles on the canvas.
    """
    canvas.circle( circle.circle_center, circle.radius, fill = circle.color )


def draw_flag_of_czech():
    """Draws the national flag of the Czech Republic.
    """
    canvas = world.ca( width = 500, height = 500, background = 'white' )
    triangle = Triangle()
    triangle.point1 = [-150, -100]
    triangle.point2 = [-25, 0]
    triangle.point3 = [-150, 100]
    triangle.color = 'DodgerBlue4'
    draw_triangle( canvas, triangle )

    trapezoidal = Trapezoidal()
    trapezoidal.point1 = [-150, -100]
    trapezoidal.point2 = [150, -100]
    trapezoidal.point3 = [150, 0]
    trapezoidal.point4 = [-25, 0]
    trapezoidal.color = 'red'
    draw_trapezoidal( canvas, trapezoidal )


def draw_polygon( canv, points, color ):
    """Draws a representation of the polygon on the canvas.
    """
    canv.polygon( points, fill = color )


def draw_triangle( canv, triangle ):
    """Draws a representation of the Triangle on the canvas.
    """
    draw_polygon( canv, [triangle.point1, triangle.point2,
        triangle.point3], triangle.color )


def draw_trapezoidal( canv, trapezoidal ):
    """Draws a representation of the trapezoidal on the canvas.
    """
    points = [trapezoidal.point1, trapezoidal.point2,
            trapezoidal.point3, trapezoidal.point4]
    draw_polygon( canv, points, trapezoidal.color )


world = World()

canvas = world.ca( width = 500, height = 500, background = 'white' )

#bbox = [[-150, -100], [150, 100]]
rect = Rectangle()
rect.lower_left_corner = Point()
rect.lower_left_corner = [-150, -100]
rect.lower_right_corner = Point()
rect.lower_right_corner = [150, 100]
rect.color = 'green4'
draw_rectangle( canvas, rect )

point = Point()
point = [-25, 0]
draw_point( canvas, point )

circle = Circle()
circle.circle_center = copy.copy( point )
circle.radius = 70
circle.color = 'red'
draw_circle( canvas, circle )

draw_flag_of_czech()
#canvas.rectangle( bbox, outline = 'black', width = 2, fill = 'green4' )
#canvas.circle( [-25, 0], 70, outline = None, fill = 'red' )
world.mainloop()

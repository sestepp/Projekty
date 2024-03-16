from re import error
from model.interface import IMoveValidator, IWorldMap
from model.core import Vector2d, MoveDirection
from model.animal import Animal
from model.view import MapVisualizer
from model.interface import IMoveValidator

class WorldMap(IWorldMap, IMoveValidator):
    def __init__(self):
        self.animals: dict[Vector2d, Animal] = {}

    def move(self, animal: Animal, direction: MoveDirection) -> None:
        forward_position = animal.position.add(animal.orientation.toUnitVector())
        backward_position = animal.position.subtract(animal.orientation.toUnitVector())
        
        if direction == MoveDirection.RIGHT or direction == MoveDirection.LEFT:
            animal.move(direction, True)
            
        elif animal.position in self.animals and direction == MoveDirection.FORWARD and forward_position not in self.animals and self.canMoveTo(forward_position):
            self.animals[forward_position] = self.animals.pop(animal.position)
            animal.position = forward_position
            return None
        
        elif animal.position in self.animals and direction == MoveDirection.BACKWARD and backward_position not in self.animals and self.canMoveTo(backward_position):
            self.animals[backward_position] = self.animals.pop(animal.position)
            animal.position = backward_position
            return None
        
        else:
            return None
        
    def place(self, animal: Animal):
        try:
            if self.canMoveTo(animal.position):
                self.animals[animal.position] = animal
                return True
            else:
                raise PositionAlreadyOccupiedError(animal.position)
        except PositionAlreadyOccupiedError:
            return (f'{PositionAlreadyOccupiedError(animal.position)}')
        
    def isOccupied(self, position: Vector2d) -> bool:
        if self.animals.get(position) is not None:
            return True
        else:
            return False

    def objectAt(self, position: Vector2d) -> Animal | None:
        if self.isOccupied(position):
            return self.animals[position]
        else:
            return None
    
class RectangularMap(WorldMap):
    def __init__(self, width, height):
        self.animals: dict[Vector2d, Animal] = {}
        self.width = width
        self.height = height
    
    def canMoveTo(self, position: Vector2d) -> bool:
        if position.precedes(Vector2d(self.width, self.height)) and position.follows(Vector2d(0, 0)) and self.animals.get(position) is None:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return MapVisualizer(self).draw(Vector2d(0, 0), Vector2d(self.width, self.height))
    
class InfiniteMap(WorldMap):
    def __init__(self):
        self.animals: dict[Vector2d, Animal] = {}
        self.right_x = None
        self.right_y= None
        self.left_x = None
        self.left_y = None
        
    def canMoveTo(self, position: Vector2d) -> bool:
        if self.animals.get(position) is None:
            if self.right_x == None and self.right_y == None:
                self.right_x = position.x
                self.right_y = position.y
                self.left_x = position.x
                self.left_y = position.y
            elif self.right_x and self.right_y:
                upperRight = position.upperRight(Vector2d(self.right_x, self.right_y))
                lowerLeft = position.lowerLeft(Vector2d(self.left_x, self.left_y))
                self.right_x = upperRight.x
                self.right_y = upperRight.y
                self.left_x = lowerLeft.x
                self.left_y = lowerLeft.y
            return True
        else:
            return False
        
    def __str__(self) -> str:
        left_x = min(self.animals, key=lambda v: v.x).x if self.animals else 0
        left_y = min(self.animals, key=lambda v: v.y).y if self.animals else 0
        right_x = max(self.animals, key=lambda v: v.x).x if self.animals else 0
        right_y = max(self.animals, key=lambda v: v.y).y if self.animals else 0

        return MapVisualizer(self).draw(Vector2d(left_x, left_y), Vector2d(right_x, right_y))
    
    
class PositionAlreadyOccupiedError(error):
    def __init__(self, position: Vector2d) -> None:
        self.position = position
    
    def __str__(self) -> str:
        return str(f'{self.position} is already occupied')
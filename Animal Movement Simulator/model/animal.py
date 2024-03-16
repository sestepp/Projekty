# from typing_extensions import Self
# import sys
# from enum import Enum
from model.core import Vector2d, MapDirection, MoveDirection
from model.interface import IMoveValidator

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation
        
    def __str__(self) -> str:
        return self.orientation.value
    
    def __repr__(self) -> str:
        return str(self)
    
    def isAt(self, position: Vector2d) -> bool:
        if self.position == position:
            return True
        
    def move(self, direction: MoveDirection, validator: IMoveValidator) -> None:
        def forward(position, orientation):
            new_position = position.add(orientation.toUnitVector())
            return new_position.precedes(Vector2d(4, 4)) and new_position.follows(Vector2d(0, 0)), new_position, orientation

        def backward(position, orientation):
            new_position = position.subtract(orientation.toUnitVector())
            return new_position.precedes(Vector2d(4, 4)) and new_position.follows(Vector2d(0, 0)), new_position, orientation

        def right(position, orientation):
            return True, position, orientation.next()

        def left(position, orientation):
            return True, position, orientation.previous()

        actions = {
            MoveDirection.FORWARD: forward,
            MoveDirection.BACKWARD: backward,
            MoveDirection.RIGHT: right,
            MoveDirection.LEFT: left
            }

        valid, new_position, new_orientation = actions[direction](self.position, self.orientation)
        if valid: self.position, self.orientation = new_position, new_orientation
                
    # def move(self, direction: MoveDirection, validator: IMoveValidator) -> None:
    #     if direction == MoveDirection.FORWARD:
    #         if self.position.add(self.orientation.toUnitVector()).precedes(Vector2d(4, 4)) and self.position.add(self.orientation.toUnitVector()).follows(Vector2d(0, 0)):
    #             self.position = self.position.add(self.orientation.toUnitVector())
    #     elif direction == MoveDirection.BACKWARD:
    #         if self.position.subtract(self.orientation.toUnitVector()).precedes(Vector2d(4, 4)) and self.position.subtract(self.orientation.toUnitVector()).follows(Vector2d(0, 0)):
    #             self.position = self.position.subtract(self.orientation.toUnitVector())
    #     elif direction == MoveDirection.RIGHT:
    #         self.orientation = self.orientation.next()
    #     elif direction == MoveDirection.LEFT:
    #         self.orientation = self.orientation.previous()
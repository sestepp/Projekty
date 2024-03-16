from enum import Enum
from functools import wraps

def log(funkcja):
    @wraps(funkcja)
    def wew(*args, **kwargs):
        #Wypisuje wartości wektora, o jakie przesuwają się strzałki
        # print('Nazwa kwalifikowana: ', funkcja.__qualname__)
        # print('Argumenty: ', *args)
        return funkcja(*args, **kwargs)
    return wew

def log_to(nazwa):
    def dekorator(funkcja):
        @wraps(funkcja)
        def wew(*args, **kwargs):
            argi = ' '.join(str(arg) for arg in args)
            plik = open(nazwa, 'a')
            plik.write(f'{funkcja.__qualname__} | {argi}\n')
            return funkcja(*args, **kwargs)
        return wew
    return dekorator

class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    @property
    @log_to('dziennik.txt')
    @log
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def tupla(self):
        return "({},{})".format(self.__x, self.__y)
    
    def __str__(self):
        return self.tupla
    
    def precedes(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            if self.x <= other_Vector2d.x and self.y <= other_Vector2d.y:
                return True
            else:
                return False
            
    def follows(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            if self.x >= other_Vector2d.x and self.y >= other_Vector2d.y:
                return True
            else:
                return False

    @log
    @log_to('dziennik.txt')
    def add(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            new_Vector2d = Vector2d(self.__x + other_Vector2d.__x, self.y + other_Vector2d.y)
            return new_Vector2d
        
    def subtract(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            new_Vector2d = Vector2d(self.x - other_Vector2d.x, self.y - other_Vector2d.y)
            return new_Vector2d
    
    def upperRight(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            new_Vector2d = Vector2d(self.x if self.x > other_Vector2d.x else other_Vector2d.x, self.y if self.y > other_Vector2d.y else other_Vector2d.y)
            return new_Vector2d
        
    def lowerLeft(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            new_Vector2d = Vector2d(self.x if self.x < other_Vector2d.x else other_Vector2d.x, self.y if self.y < other_Vector2d.y else other_Vector2d.y)
            return new_Vector2d
    
    def opposite(self):
        new_Vector2d = Vector2d(-self.x, -self.y)
        return new_Vector2d
    
    def __eq__(self, other_Vector2d):
        if isinstance(other_Vector2d, Vector2d):
            return self.x == other_Vector2d.x and self.y == other_Vector2d.y

    def __hash__(self):
        return hash(self.x)
        
class MoveDirection(Enum):
    FORWARD = 'f'
    BACKWARD = 'b'
    LEFT = 'l'
    RIGHT = 'r'

class MapDirection(Enum):
    NORTH = '\u2191' # ↑
    EAST = '\u2192'  # →
    SOUTH = '\u2193' # ↓
    WEST = '\u2190' # ←
    
    def __str__(self) -> str:
        return self.value
    
    def next(self):
        if self.name == 'EAST':
            self = self.SOUTH
        elif self.name == 'SOUTH':
            self = self.WEST
        elif self.name == 'WEST':
            self = self.NORTH
        elif self.name == 'NORTH':
            self = self.EAST
        return self
    
    def previous(self):
        if self.name == 'EAST':
            self = self.NORTH
        elif self.name == 'NORTH':
            self = self.WEST
        elif self.name == 'WEST':
            self = self.SOUTH
        elif self.name == 'SOUTH':
            self = self.EAST
        return self
    
    def toUnitVector(self) -> Vector2d:
        new_Vector2d = Vector2d(0, 0)
        
        if self.name == 'EAST':
            new_Vector2d = Vector2d(1, 0)
        elif self.name == 'NORTH':
            new_Vector2d = Vector2d(0, 1)
        elif self.name == 'WEST':
            new_Vector2d = Vector2d(-1, 0)
        elif self.name == 'SOUTH':
            new_Vector2d = Vector2d(0, -1)
            
        return new_Vector2d

v1=Vector2d(2,2)
v2=v1.add(Vector2d(1,1))
v1.x
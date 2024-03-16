"""
Autor: Stanisław Polak
Data utworzenia: 22-10-2023
Data modyfikacji: 22-10-2023
Wersja: 1.0
Opis: Testy integracyjne klasy "Animal".
"""      

import pytest
from model.core import MapDirection, Vector2d, MoveDirection
from model.map import RectangularMap
from model.animal import Animal
# from model.interface import IMoveValidator

@pytest.fixture
def rectangular_map_2_2():
    yield RectangularMap(2, 2)

@pytest.fixture
def animal():
    # Tutaj kod, który, w przypadku modułu 'unittest', umieścilibyśmy w metodzie 'setUp()'  
    yield Animal(Vector2d(2, 2))  # Dane, które mają być testowane
    # Tutaj kod, który, w przypadku modułu 'unittest', umieścilibyśmy w metodzie 'tearDown()'


def test_Animal_isAt(animal: Animal):
    assert animal.isAt(Vector2d(2, 2))
    
    
def test_Animal_print(animal: Animal):
    assert str(animal) == "↑"


def test_Animal_move_north(animal: Animal):
    assert animal.orientation == MapDirection.NORTH
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 4))
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 4))
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 3))


def test_Animal_move_south(animal: Animal):
    assert animal.orientation == MapDirection.NORTH
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 0))
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 0))
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(2, 1))


def test_Animal_move_east(animal: Animal):
    animal.move(MoveDirection.RIGHT, rectangular_map_2_2)
    assert animal.orientation == MapDirection.EAST
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(4, 2))
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(4, 2))
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(3, 2))


def test_Animal_move_west(animal: Animal):
    animal.move(MoveDirection.LEFT, rectangular_map_2_2)
    assert animal.orientation == MapDirection.WEST
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(0, 2))
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    animal.move(MoveDirection.FORWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(0, 2))
    animal.move(MoveDirection.BACKWARD, rectangular_map_2_2)
    assert animal.isAt(Vector2d(1, 2))
    

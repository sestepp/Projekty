import sys
import os
from typing import List
from model.interface import IWorldMap
from model.core import MoveDirection, Vector2d # Import bezwzględny
from model.animal import Animal
import time

class OptionsParser:
    @staticmethod
    def parse(args):
        enum_values = list(map(lambda x: x.value, MoveDirection))
        value_list = list(map(lambda arg: MoveDirection(arg) if arg in enum_values else exit(f'{arg} is not legal move specification'), args))
        # value_list = []
        # for arg in args:
        #     try:
        #         value_list.append(MoveDirection(arg))
        #     except ValueError:
        #         exit(f'{arg} is not legal move specification')
        return value_list

class Simulation:
    def __init__(self, directions: List[MoveDirection], positions: List[Vector2d], arg: IWorldMap) -> None:
        self.directions = directions
        self.positions = positions
        Simulation.animals = []
        Simulation.arg = arg
        
        for animal_position in self.positions:
            animal = Animal(animal_position)
            if Simulation.arg.place(animal):
                Simulation.animals.append(animal)
        
    def run(self) -> None:
        i = 0
        print(Simulation.arg)
        time.sleep(0.5)
        os.system('cls')
        for act in self.directions:
            Simulation.arg.move(Simulation.animals[i], act)
            print(Simulation.arg)
            time.sleep(0.2)
            os.system('cls')
            i += 1
            if i == len(Simulation.animals):
                i = 0
        else:
            print(Simulation.arg)
            time.sleep(0.5)
            i += 1 
            if i == len(Simulation.animals):
                i = 0
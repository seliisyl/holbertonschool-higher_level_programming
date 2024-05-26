#!/usr/bin/env python3
"""
    Class file for ABC class.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Definition of an abstract method sound """

    @abstractmethod
    def sound(self):
        """ The abstract method has no body """
        pass


class Dog(Animal):
    """ Implementation of the sound method for the Dog class """

    def sound(self):
        """ Make a sound of the dog. """
        return "Bark"


class Cat(Animal):
    """ Sub class for a Cat Animal. """
    def sound(self):
        """ Make a sound of the cat. """
        return "Meow"

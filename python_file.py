import pandas as pd
import numpy as np
import sklearn
import PIL

class Example:
    def __init__(self):
        print("Instance Created")
      
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

    def local2Function(self):
        print("This is a local function")

    def newfunc(self):
        print("This is a new function")

    def anotherNewFunc(self):
        print("This is another new function")

    def another3NewFunc(self):
        print("This is a third new function")
        
    def anotherAnotherNewFunc(self):
        print("This is another new function")        

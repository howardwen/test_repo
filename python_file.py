import pandas as pd
import numpy as np

class Example:
    def __init__(self):
        print("Instance Created")
      
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

    def newfunc(self):
        print("This is a new function")

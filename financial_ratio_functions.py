import pandas as pd
import numpy as np 


##Liquidity - Current Ratio
def liquidity_current_ratio(Curr_Assets, Curr_Liabilities):
    current_ratio = Curr_Assets / Curr_Liabilities 
    return current_ratio
#result = liquidity_current_ratio(numerator, denominator)

##Liquidity - Acid Test Ratio 

def liquidity_acid_test_ratio(Curr_Assets, Curr_Liabilities, Inventory ):
    acid_test_ratio = (Curr_Assets - Inventory)/Curr_Liabilities
    return acid_test_ratio


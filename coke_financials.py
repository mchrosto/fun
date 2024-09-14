#Version 1.0
#Name:Matthew Chrostowski 





#########################################################################################################
#Dev Notes: Will need to make a dimensional table for the indiviudal financial ratios - will need an id, 



##########################################################################################################
import pandas as pd
import yfinance as yf
from financial_ratio_functions import *

#pulling my companies financial information 
ticker = yf.Ticker("COKE")

#pulling all statements and breaking them up between annual and quarterly

#annual
a_income = ticker.financials
a_balance = ticker.balance_sheet
a_cash_flow = ticker.cashflow

#quarterly 
q_income = ticker.quarterly_financials
q_balance = ticker.quarterly_balance_sheet
q_cash_flow = ticker.quarterly_cashflow

#all financials
all_fin = [a_income, a_balance, a_cash_flow, q_income, q_balance, q_cash_flow]


## Reset index, make date field it's own column for future time series analysis, 
##
def df_clean(all_fin):
    df_reset = all_fin.reset_index()
    df_reset.rename(columns={"index": "Statement_Date"}, inplace=True)
    df_flipped = df_reset.T
    df_flipped.columns = df_flipped.iloc[0]
    df_flipped = df_flipped[1:]
    return df_flipped


#use a for loop to consolidate this - it would look much better 
a_income_cl = df_clean(a_income)
a_balance_cl = df_clean(a_balance)
a_cash_flow_cl = df_clean(a_cash_flow)
q_income_cl = df_clean(q_income) 
q_balance_cl = df_clean(q_balance)
q_cash_flow_cl = df_clean(q_cash_flow) 


#a_balance_cl.to_csv('annual_balance_sheet.csv', index=True)

#all_fin_cl = [a_income_cl, a_balance_cl, a_cash_flow_cl, q_income_cl, q_balance_cl, q_cash_flow_cl]
#combine the quarterly data and annual data into 2 distinct dataframes - i think technically would be a concat

a_stmts = pd.concat([a_income_cl, a_balance_cl, a_cash_flow_cl], axis=1)
q_stmts = pd.concat([q_income_cl, q_balance_cl, q_cash_flow_cl], axis=1)
 
# a_stmts.to_csv('annual_statements.csv', index=True )
# q_stmts.to_csv('quarterly_statements.csv', index=True )


# kpi_search = a_income_cl.columns[a_income_cl.columns.str.contains('Current')]
# print(kpi_search)


### add the column to df within the function?? and the liquidity current ratio function into the big function # make this a real tansformation 
a_stmts['Current Ratio'] = a_stmts.apply(lambda row: liquidity_current_ratio(row['Current Assets'], row['Current Liabilities']), axis=1)
q_stmts['Current Ratio'] = q_stmts.apply(lambda row: liquidity_current_ratio(row['Current Assets'], row['Current Liabilities']), axis=1)
a_stmts['Acid Test Ratio'] = a_stmts.apply(lambda row: liquidity_acid_test_ratio(row['Current Assets'], row['Current Liabilities'], row['Inventory']), axis=1)
q_stmts['Acid Test Ratio'] = q_stmts.apply(lambda row: liquidity_acid_test_ratio(row['Current Assets'], row['Current Liabilities'], row['Inventory']), axis=1)


print(q_stmts)





# fast_info = ticker.fast_info

# day_high = fast_info.day_high
# open = fast_info.open
# #print(open)



# #print(type(balance_sheet)) it's a dataframe


# #print(bs_head)



# #print(balance_sheet)




import pandas as pd
import numpy as np

# Data from stock data valuation.csv
data = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\data\stocks data valuation.csv")
df = pd.DataFrame(data)

# Current assumptions:
#   1) Prices of stocks are given
#   2) Target prices(stock values) of stocks are given
#   3) Scoring of the criteria from Investor point of view
#   4) Conservative approach is taken:
#       if it is not enough information then test get score 0
#   5) Price per Earnings ratio is given


# First Valuation Test: if stock undervalued. Price vs Target Price

def First_Valuation_Test():
    # Convert to numeric
    # If any values in the column cannot be converted to numeric format,
    #   they will be replaced with NaN (Not a Number)
    df["Stock Price"] = pd.to_numeric(df["Stock Price"], errors="coerce")
    df["Price Target"] = pd.to_numeric(df["Price Target"], errors="coerce")

    value1 = df["Stock Price"]
    value2 = df["Price Target"]
    price_diff = value2/value1 - 1

    # Create new columns for the results
    df["Valuation"] = None
    df["PT Diff in %"] = None
    df["Score"] = None

    # Check if Target Price above Stock Price
    # If yes, then assigned "Underpriced" and score "1"
    df.loc[price_diff > 0, "Valuation"] = "Underpriced"
    df.loc[price_diff > 0, "PT Diff in %"] = (price_diff*100).round(2)
    df.loc[price_diff > 0, "Score"] = 1

    # If target Price below Stock Price
    # Then assigned "Overpriced" and score "0"
    df.loc[price_diff <= 0, "Valuation"] = "Overpriced"
    df.loc[price_diff <= 0, "PT Diff in %"] = (price_diff*100).round(2)
    df.loc[price_diff <= 0, "Score"] = 0

    # Replace NaN in columns with "N/A"
    # If score column has "None" then it will be replaced with 0
    df["Price Target"] = df["Price Target"].fillna("N/A")
    df["PT Diff in %"] = df["PT Diff in %"].fillna("N/A")
    df["Valuation"] = df["Valuation"].fillna("N/A")
    df["Score"] = df["Score"].fillna(0)

    Valuation_Test1 = pd.DataFrame(df)
    return (Valuation_Test1)


# The output of the first valuation test
result = First_Valuation_Test()
print(result.to_string(index=False))

# Second Valuation Test: if share price significantly below its Fair Value (FV)
# Price Target Difference ( PT Diff) will be compared to 20% - assigned bench mark
# If Price of share is underpriced >20% of its FV then 1 will be assigned as score


def Second_Valuation_Test():
    # Convert to numeric
    # If any values in the column cannot be converted to numeric format,
    #   they will be replaced with NaN (Not a Number)
    df["PT Diff in %"] = pd.to_numeric(df["PT Diff in %"], errors="coerce")

    # Create new columns for the results
    df["Valuation1"] = None
    df["Score1"] = None
    df["PT Diff in % Absolute"] = df["PT Diff in %"].abs()

    # If Price of share is underpriced >20% of its FV then 1 will be assigned as score
    df.loc[df["PT Diff in % Absolute"] > 20, "Valuation1"] = "Significantly"
    df.loc[df["PT Diff in % Absolute"] > 20, "Score1"] = 1
    df.loc[df["PT Diff in % Absolute"] <= 20, "Valuation1"] = "Slightly"
    df.loc[df["PT Diff in % Absolute"] <= 20, "Score1"] = 0

    # If score column has "None" then it will be replaced with 0
    df["Score1"] = df["Score1"].fillna(0)

    Second_Valuation_Test = pd.DataFrame(df)
    return (Second_Valuation_Test)


# The output of the second valuation test
result1 = Second_Valuation_Test()
print(result1.to_string(index=False))


# Third Valuation Test:Benjamin Graham's Formula
# If the stock price is below V in the formula below then 1 assigned as score
# V = sqrt(22.5 * E * B)
#   V represents the intrinsic value of the stock
#   E is the company's earnings per share (EPS) over the past 12 months
#   B is the company's book value per share

def Third_Valuation_Test():

    df["BG_Value"] = None
    df["Score2"] = None

    # 22.5 is Graham's multiplier
    # It can be increased or reduced which depends on Investor risk level
    df["BG_Value"] = np.sqrt(22.5*df["EPS"]*(df["Equity"]/df["Shares Out"]))

    # If the stock price is below Benjamin Graham's value
    #   then 1 assigned as score
    df.loc[df["Stock Price"] < df["BG_Value"], "Score2"] = 1
    df.loc[df["Stock Price"] >= df["BG_Value"], "Score2"] = 0

    # If score column has "None" then it will be replaced with 0
    df["Score2"] = df["Score2"].fillna(0)

    return (df)


# The output of the third valuation test
result2 = Third_Valuation_Test()
print(result2.to_string(index=False))


# Fourth Valuation Test: Price per Earnings (PE ratio) compare to market avg
# If PE ratio is above market avg then 1 assigned as score
def Fourth_Valuation_Test():

    df["Score3"] = None

    # To find market average
    df["PE_Market_avg"] = df["PE Ratio"].mean()

    df.loc[df["PE Ratio"] > df["PE_Market_avg"], "Score3"] = 1
    df.loc[df["PE Ratio"] <= df["PE_Market_avg"], "Score3"] = 0

    # If score column has "None" then it will be replaced with 0
    df["Score3"] = df["Score3"].fillna(0)

    return (df)


# The output of the fourth valuation test
result3 = Fourth_Valuation_Test()
print(result3.to_string(index=False))

# Fifth Valuation Test: Price per Earnings (PE ratio) compare to industry avg


def Fifth_Valuation_Test():

    df["Score4"] = None

    # To find industry average
    # Group by "Industry" and selects the "PE Ratio"
    # Then, transform("mean") calculates the mean  for each group and assigns the result to each corresponding row
    df["PE_Industry_group_avg"] = df.groupby(
        "Industry")["PE Ratio"].transform('mean')

    df.loc[df["PE Ratio"] > df["PE_Industry_group_avg"], "Score4"] = 1
    df.loc[df["PE Ratio"] <= df["PE_Market_avg"], "Score4"] = 0

    # If score column has "None" then it will be replaced with 0
    df["Score4"] = df["Score4"].fillna(0)

    return (df)


# The output of the fourth valuation test
result4 = Fifth_Valuation_Test()
print(result4.to_string(index=False))

# To save the output
df.to_csv(r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Valuation_output.csv", index=False)

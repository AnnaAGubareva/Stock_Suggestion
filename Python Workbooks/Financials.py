import pandas as pd
import numpy as np
data1 = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\data\stocks data financials.csv")
df1 = pd.DataFrame(data1)

# Current assumptions:
#   1) Scoring of the criteria from Investor point of view
#   2) Conservative approach is taken:
#       if it is not enough information then test get score 0
#   3) Operation Income is given
#

# First Financial Test
# If Operation income of the company positive then test get score 1


def First_Financial_Test():

    # Convert to numeric
    # If any values in the column cannot be converted to numeric format,
    #   they will be replaced with NaN (Not a Number)
    df1["Op. Income"] = pd.to_numeric(df1["Op. Income"], errors="coerce")

    df1["FScore1"] = None

    df1.loc[df1["Op. Income"] > 0, "FScore1"] = 1
    df1.loc[df1["Op. Income"] <= 0, "FScore1"] = 0

    df1["FScore1"] = df1["FScore1"].fillna(0)

    return (df1)


# The output of the first financial test
result1 = First_Financial_Test()
# To a string representation without the index column
print(result1.to_string(index=False))

# Second Financial Test
# If short term assets greater than short term liabilities
# then test gets score 1


def Second_Financial_Test():
    df1["Current Ratio"] = pd.to_numeric(df1["Current Ratio"], errors="coerce")

    df1["FScore2"] = None

    df1.loc[df1["Current Ratio"] > 1, "FScore2"] = 1
    df1.loc[df1["Current Ratio"] <= 1, "FScore2"] = 0

    df1["FScore2"] = df1["FScore2"].fillna(0)
    return (df1)


# The output of the second financial test
result2 = Second_Financial_Test()
# To a string representation without the index column
print(result2.to_string(index=False))

# Third Financial Test
# Evaluate debt-to-equity ratio based on industry average
# If debt-to-equity ratio below industry average then test gets score 1


def Third_Financial_Test():
    df1["Debt / Equity"] = pd.to_numeric(df1["Debt / Equity"], errors="coerce")

    df1["FScore3"] = None

    df1["DE_Industry_group_avg"] = df1.groupby(
        "Industry")["Debt / Equity"].transform("mean")

    df1.loc[df1["Debt / Equity"] > df1["DE_Industry_group_avg"], "FScore3"] = 0
    df1.loc[df1["Debt / Equity"] <= df1["DE_Industry_group_avg"], "FScore3"] = 1

    # If score column has "None" then it will be replaced with 0
    df1["FScore3"] = df1["FScore3"].fillna(0)

    return (df1)


# The output of the third valuation test
result3 = Third_Financial_Test()
print(result3.to_string(index=False))

# Fourth Financial Test
# Evaluate Debt-to-Equity (D/E) ratio based on market average
# If D/E ratio is below market average then test gets score 1


def Fourth_Financial_Test():

    df1["FScore4"] = None
    df1["DE_Market_avg"] = df1["Debt / Equity"].mean()

    df1.loc[df1["Debt / Equity"] < df1["DE_Market_avg"], "FScore4"] = 1
    df1.loc[df1["Debt / Equity"] >= df1["DE_Market_avg"], "FScore4"] = 0

    df1["FScore4"] = df1["FScore4"].fillna(0)

    return (df1)


result4 = Fourth_Financial_Test()
print(result4.to_string(index=False))

# Evaluate if Earnings per share (EPS) grows over years
# If EPS growth  3 years is lower than EPS growth 5 years,
#   and EPS growth for this year is positive then test gets score 1


def Fifth_Financial_Test():

    df1["FScore5"] = None

    df1.loc[(df1["EPS Growth 3Y"] < df1["EPS Growth 5Y"]), "FScore5"] = 1
    df1.loc[df1["EPS Growth 3Y"] >= df1["EPS Growth 5Y"], "FScore5"] = 0

    df1["FScore5"] = df1["FScore5"].fillna(0)

    return (df1)


result5 = Fifth_Financial_Test()
print(result5.to_string(index=False))

# To save the output
df1.to_csv(r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Financial_output.csv", index=False)

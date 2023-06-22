import pandas as pd
import numpy as np
data2 = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\data\stocks data performance.csv")

df2 = pd.DataFrame(data2)
# First Performance Test
# If EPS Growth 5Y for company is higher than industry avg
#   then test scores 1


def First_Performance_Test():

    df2["PScore1"] = None
    df2["EPS Growth 5Y"] = pd.to_numeric(
        data2["EPS Growth 5Y"].str.replace('%', ''), errors='coerce')

    df2["EPS_Industry_group_avg"] = df2.groupby(
        "Industry")["EPS Growth 5Y"].transform("mean")

    df2.loc[df2["EPS Growth 5Y"] > df2["EPS_Industry_group_avg"], "PScore1"] = 1
    df2.loc[df2["EPS Growth 5Y"] <=
            df2["EPS_Industry_group_avg"], "PScore1"] = 0

    df2["PScore1"] = df2["PScore1"].fillna(0)

    return (df2[["EPS Growth 5Y", "EPS_Industry_group_avg", "Industry", "PScore1"]].head(10))


result1 = First_Performance_Test()
print(result1.to_string(index=False))


# Second Performance Test
# If EPS Growth 5Y for company is higher than market avg
#   then test scores 1
def Second_Performance_Test():

    df2["PScore2"] = None
    df2["EPS Growth 5Y"] = pd.to_numeric(
        data2["EPS Growth 5Y"].str.replace('%', ''), errors='coerce')

    df2["EPS_Market_avg"] = df2["EPS Growth 5Y"].mean()

    df2.loc[df2["EPS Growth 5Y"] > df2["EPS_Market_avg"], "PScore2"] = 1
    df2.loc[df2["EPS Growth 5Y"] <=
            df2["EPS_Market_avg"], "PScore2"] = 0

    df2["PScore2"] = df2["PScore2"].fillna(0)

    return (df2)


result2 = Second_Performance_Test()
print(result2.to_string(index=False))

# Third Performance Test
# If company Revenue Growth during last 5 years above industry avg
#   then the test scores 1


def Third_Performance_Test():
    df2["PScore3"] = None
    df2["Rev. Growth 5Y"] = pd.to_numeric(
        data2["Rev. Growth 5Y"].str.replace('%', ''), errors='coerce')

    df2["Rev_Industry_group_avg"] = df2.groupby(
        "Industry")["Rev. Growth 5Y"].transform("mean")

    df2.loc[df2["Rev. Growth 5Y"] >
            df2["Rev_Industry_group_avg"], "PScore3"] = 1
    df2.loc[df2["Rev. Growth 5Y"] <=
            df2["Rev_Industry_group_avg"], "PScore3"] = 0

    df2["PScore3"] = df2["PScore3"].fillna(0)

    return (df2)


result3 = Third_Performance_Test()
print(result3.to_string(index=False))


# Fourth Performance Test
# If company revenue growth during last 5 years above market avg
#   then the test scores 1

def Fourth_Performance_Test():
    df2["PScore4"] = None

    df2["Rev_Market_avg"] = df2["Rev. Growth 5Y"].mean()

    df2.loc[df2["Rev. Growth 5Y"] >
            df2["Rev_Market_avg"], "PScore4"] = 1
    df2.loc[df2["Rev. Growth 5Y"] <=
            df2["Rev_Market_avg"], "PScore4"] = 0

    df2["PScore4"] = df2["PScore4"].fillna(0)

    return (df2)


result4 = Fourth_Performance_Test()
print(result4.to_string(index=False))


# Fifth Performance Test
# If Return On Equity is above 20% - nominal bench mark
#    then test scores 1

def Fifth_Performance_Test():

    df2["PScore5"] = None

    df2["ROE"] = pd.to_numeric(
        df2["ROE"].str.replace('%', ''), errors='coerce')

    df2.loc[df2["ROE"] > 20, "PScore5"] = 1
    df2.loc[df2["ROE"] <= 20, "PScore5"] = 0

    df2["PScore5"] = df2["PScore5"].fillna(0)

    return (df2[["ROE",  "PScore5"]].head(30))


result5 = Fifth_Performance_Test()
print(result5.to_string(index=False))

# To save the output
df2.to_csv(r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Performance_output.csv", index=False)

# Sixth Performance Test
# If Return on Asset is above industry avg
#    then test scores 1

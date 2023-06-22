import pandas as pd

Valuation = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Valuation_output.csv")
Performance = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Performance_output.csv")
Financial = pd.read_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Financial_output.csv")


# Valuation


# To create new column with Valuation total score
Valuation["Valuation_total_score"] = Valuation[[
    "Score", "Score1", "Score2", "Score3", "Score4"]].sum(axis=1)

# Specific columns from Valuation csv
Valuation_columns = Valuation[["Symbol", "Company Name",
                               "Stock Price", "Price Target", "PT Diff in %", "Score", "Valuation",
                              "Valuation1", "PT Diff in % Absolute", "Score1",
                               "BG_Value", "Score2",
                               "PE Ratio", "PE_Market_avg", "Score3",
                               "Industry", "PE_Industry_group_avg", "Score4",
                               "Valuation_total_score"
                               ]]


# Columns into DataFrame
Valuation_df = pd.DataFrame(Valuation_columns)


# Performance


# To create new column with Performance total score
Performance["Performance_total_score"] = Performance[[
    "PScore1", "PScore2", "PScore3", "PScore4", "PScore5"]].sum(axis=1)

# Specific columns from Performance csv
Performance_columns = Performance[["Symbol", "Company Name",
                                   "EPS Growth 5Y", "EPS_Industry_group_avg", "PScore1",
                                   "EPS_Market_avg", "PScore2",
                                   "Industry", "Rev. Growth 5Y", "Rev_Industry_group_avg", "PScore3",
                                   "Rev_Market_avg", "PScore4",
                                   "ROE", "PScore5",
                                   "Performance_total_score"
                                   ]]

Performance_df = pd.DataFrame(Performance_columns)


# Financial

# To create new column with Financial total score
Financial["Financial_total_score"] = Financial[[
    "FScore1", "FScore2", "FScore3", "FScore4", "FScore5"]].sum(axis=1)

# Specific columns from Financial csv
Financial_columns = Financial[["Symbol", "Company Name",
                               "Op. Income", "FScore1",
                               "Current Ratio", "FScore2",
                               "Industry", "Debt / Equity", "DE_Industry_group_avg", "FScore3",
                               "DE_Market_avg", "FScore4",
                               "EPS Growth 3Y", "EPS Growth 5Y", "FScore5",
                               "Financial_total_score"
                               ]]

Financial_df = pd.DataFrame(Financial_columns)

# To create merged DataFrame
Merged_3df = pd.concat([Valuation_df, Performance_df, Financial_df], axis=1)
Merged_3df["Total_Score"] = Merged_3df[["Valuation_total_score",
                                        "Performance_total_score", "Financial_total_score",]].sum(axis=1)

# To assign max score: 3 test * 5 questions in each = 15
Merged_3df["Max_Score"] = 15

Merged_3df["Stock_Score_Ratio (%)"] = (Merged_3df["Total_Score"] /
                                       Merged_3df["Max_Score"] * 100).round(2)


# To save the output
Valuation_df.to_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Valuation_columns.csv", index=False)
Performance_df.to_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Performance_columns.csv", index=False)
Financial_df.to_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Financial_columns.csv", index=False)
Merged_3df.to_csv(
    r"C:\Users\annaa\OneDrive\Desktop\LightHouseLabs Data Immerse\Final project\Output\Merged_3df.csv", index=False)

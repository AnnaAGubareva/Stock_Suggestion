# Stock Suggestion for Investor

* Welcome to the Socks for Investors project! 
* This repository aims to provide suggestions for stocks based on their performance in three categories of tests: performance test, financial test, and valuation test. 
* By analyzing stocks using these tests, we can recommend the top-performing stocks to potential investors.

## Introduction

* As an investor, it can be challenging to identify the best stocks to invest in. 
* This project aims to simplify the process by evaluating stocks using three different categories of tests: performance test, financial test, and valuation test. 
* Each test consists of five questions, and the stock that scores the highest in all three categories will be suggested to investors.
* Stocks score process from the Investor point of you. Also, "safe" approoch is taken, which means I stock evaluation equal to the market then stock will score "0".
* If there is not enough data avalable for the test to be perform than test will score "0".
* Total categories for test: 3
* Total number of questions per each category: 5 ( will be increased over time)
* The highest posible score for stock is "15"

## Performance test

* The performance test evaluates how well a stock has performed over a given period. 
* It considers factors such as historical returns, volatility, and risk-adjusted performance. 
* The five questions used to assess a stock's performance are as follows:

* 1) Is stock Earnings Per Growth (EPG) ratio is higher than industry average? If it is higher, then stock score "1".
* 2) If EPS Growth 5Y for company is higher than market avgerage? If yes, the stock scores "1".
* 3) If company Revenue Growth during last 5 years is above industry average? If yes, the stock scores "1".
* 4) If company Revenue Growth during last 5 years is above market average? If yes, the stock scores "1". 
* 5) If Return On Equity is above 20% - nominal bench mark? If yes, the stock scores "1".

## Valuation test

* 1) If stock market price is undervalued compare to stock intrinsic value, then the stock scores "1".
* 2) If stock market price is over/under priced more than 20% - bench mark. If so, then the stock will score "0".
* 3) If stock market price is undervalued compare to stock intrinsic value using Benjamin Graham's Formula. If so the stock will score "1".
* 4) If Price per Earnings (PE ratio) is above  market avg? If so, stock will score "1".
* 5) If Price per Earning ratio is above industry avg? If so, stock will score "1"

## Company Financial test

* 1) If Operation income of the company positive then stock get score "1".
* 2) If short term assets greater than short term liabilities? If so, then stock get score "1".
* 3) If debt-to-equity ratio below industry average then stock gets score "1".
* 4) If D/E ratio is below market average then stock gets score "1".
* 5) If EPS growth  3 years is lower than EPS growth 5 years.If so, then stock gets score "1".

## File navigation
### Data folder
* Cointains all extracted files from https://stockanalysis.com/. Data was extracted on June 16, 2023 ( after market closure) 

### Output folder

* Contains files saved after functions ( stock tests) were performed in Python

### Python Workbooks

* Python code for running tests

### Tableau workbook and dashboard

* Tableau workbook and dashboard
* link to Tableau Public  https://public.tableau.com/app/profile/anna.gubareva/viz/StockSuggestion/Dashboard?publish=yes

#### How to use Tableau dashboard

* When dashboard is opened it is automaticaly alredy filtered to top 15 stocks which score the most ( refer to left container "Overall score")
* You can select stock from "Overall score" chart or you can use filters to navigate to stock which you are interested.
* Charts on the right from filters will be updated automaticaly after you select stock and/or filters.

## Coming soon!

* I planning to automated data extraction and it will be updated weekly.
* Also, I am planing to increase amounts of test for each category to score stock more reliably.
* I am planning to transfer this dashbord to online space to make more intaractive and uptodate.


## Contributing
* Contributions to this project are always welcome. If you have any suggestions or would like to add new features, please fork the repository and create a pull request. 
* I appreciate your contributions and feedback.

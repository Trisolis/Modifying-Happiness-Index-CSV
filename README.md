A command-line tool for loading, filtering, and analyzing the data of 2015's 'World Happiness Report' as a CSV.

## Features:
- Reverting to the original CSV from a working copy
- Sorting by column (ascending or descending)
- Filter (by one or more variables, syntax given by program)
- Aggregate (mean/median/sum of a chosen column)
- Correlate (calculate correlation between two columns w/ clear English explanation)
- Display (prints current dataframe out)
- Export (saves modified/working CSV to your system)

## Setup:
1. git clone ...
2. cd project
3. python -m venv venv
4. source venv/Scripts/activate
5. pip install -r requirements.txt
6. python main.py
7. Run!

## Dataset: 
https://www.kaggle.com/datasets/unsdsn/world-happiness
Using 2015's data

## Example Usage:

```
--- Data Modifier Menu ---
1) Reset to original data
2) Sort
3) Filter
4) Aggregate (mean/median/sum)
5) Correlate
6) Display current data
7) Show columns
8) Export CSV
9) Quit
Enter your choice: 3
Available columns:  ['Country', 'Region', 'Happiness Rank', 'Happiness Score', 'Standard Error', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']
Enter condition(s), format: column operator value | column operator value ...
Example: Region == Western Europe | Happiness Score > 5
> Region == Middle East and Northern Africa | Happiness Score > 6.5
                 Country                           Region  Rank  Score  Std Error  Economy  Family  Health  Freedom  Trust  Generosity  Dystopia
10                Israel  Middle East and Northern Africa    11   7.28       0.03     1.23    1.22    0.91     0.41   0.08        0.33      3.09
19  United Arab Emirates  Middle East and Northern Africa    20   6.90       0.04     1.43    1.13    0.81     0.64   0.39        0.26      2.25
21                  Oman  Middle East and Northern Africa    22   6.85       0.05     1.36    1.08    0.76     0.63   0.33        0.22      2.47
27                 Qatar  Middle East and Northern Africa    28   6.61       0.06     1.69    1.08    0.80     0.64   0.52        0.33      1.56

[menu]
Enter your choice: 2
Available columns:  ['Country', 'Region', 'Happiness Rank', 'Happiness Score', 'Standard Error', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']
Which column would you like to sort by? Family
Ascending or descending? (a/d) d
                 Country                           Region  Rank  Score  Std Error  Economy  Family  Health  Freedom  Trust  Generosity  Dystopia
10                Israel  Middle East and Northern Africa    11   7.28       0.03     1.23    1.22    0.91     0.41   0.08        0.33      3.09
19  United Arab Emirates  Middle East and Northern Africa    20   6.90       0.04     1.43    1.13    0.81     0.64   0.39        0.26      2.25
21                  Oman  Middle East and Northern Africa    22   6.85       0.05     1.36    1.08    0.76     0.63   0.33        0.22      2.47
27                 Qatar  Middle East and Northern Africa    28   6.61       0.06     1.69    1.08    0.80     0.64   0.52        0.33      1.56

[menu]
Enter your choice: 5
Available columns:  ['Country', 'Region', 'Happiness Rank', 'Happiness Score', 'Standard Error', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']
First column: Family
Second column: Happiness Rank
Your correlation value is: -0.94. This means there is a strong negative correlation between your two variables
```
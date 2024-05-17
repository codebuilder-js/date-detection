A program with a regular expression that can detect dates in the 
DD/MM/YYYY format. Assume that the days range from 01 to 31, the 
months range from 01 to 12, and the years range from 1000 to 2999. 
Note that if the day or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month 
or for leap years; it will accept nonexistent dates like 31/02/2020 or 
31/04/2021.
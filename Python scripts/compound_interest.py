
def compound_interest(years=9, percent=10, start_capital=500000, capital_increase=500000) -> int:
    
    result=0
    for year in range(years):
        result = start_capital+(start_capital*(percent/100))
        print('Sum for', year+1, 'year wihtout increase:', "{:,.2f}".format(result))
        
        result += capital_increase
        start_capital = result
        print('Sum for', year+1, 'year with increase:', "{:,.2f}".format(result), '\n')

if __name__ == "__main__":
    
    years = 30 #start from zero
    percent = 9 #%
    start_capital = 500000 #500'000
    capital_increase = 500000 #250'000
    
    compound_interest(years, percent, start_capital, capital_increase)
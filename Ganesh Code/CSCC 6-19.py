def driving_cost(miles_per_gallon, dollars_per_gallon, 
    miles_driven=10.0):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon
        
if __name__ == '__main__':
    # Type your code here.
    miles = float(input())
    dollars = float(input())

    price = driving_cost(miles, dollars) 
    print(f'{price:.2f}')
    print(f'{price * 5:.2f}')
    print(f'{price * 40:.2f}')
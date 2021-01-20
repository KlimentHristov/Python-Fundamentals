random = float(input())

def grade(rate):
    if 2 <= rate <= 2.99:
        return 'Fail'
    elif 3 <= rate <= 3.49:
        return 'Poor'
    elif 3.50 <= rate <= 4.49:
        return 'Good'
    elif 4.50 <= rate <= 5.49:
        return 'Very Good'
    elif 5.50 <= rate <= 6.00:
        return 'Excellent'

print(grade(random))




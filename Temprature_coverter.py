
def convert_degree_fehrenhite(temp):
    return (temp*(9/5))+32


t = int(input("enter temp  in degrees :"))
print(f'{t} degrees are '+str(convert_degree_fehrenhite(t))+" Fahrenheit"    )

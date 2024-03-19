print("Welcome to the Fibonacci Calculator App")
usrInput = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

fiboSeries = [1,1]

# Create the Fibonacci Sequence
for i in range(usrInput-2):
    newFib = fiboSeries[i]+fiboSeries[i+1]
    fiboSeries.append(newFib)

# Display the fibonacci sequence
for i in fiboSeries:
    print(i)

print("\nThe corresponding Golden Ratio values are:")

goldenRatio = []
# Compute the golden ratio values
for i in range(len(fiboSeries)-1):
    ratio = fiboSeries[i+1]/fiboSeries[i]
    goldenRatio.append(ratio)

# Display the golden ratio values
for i in goldenRatio:
    print(i)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")
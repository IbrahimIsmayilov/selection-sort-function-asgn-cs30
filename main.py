nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        # Search for minimum
        minPosition = i
        for n in range(i + 1, len(anArray)):
            if (anArray[n] < anArray[minPosition]):
                minPosition = n
        anArray[i], anArray[minPosition] = anArray[minPosition], anArray[i] 
        

print(selectionSort(nums))
print(selectionSort(words))
if __name__ == '__main__':
# Task 1.

    def prukazku_Velukden(str):
        counts = dict()
        words = str.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    print( prukazku_Velukden ('Коли    не    прийду    до    церкви, то    все    паски    святять. Якби то можна бути через зиму - котом, через літо - пастухом, а на Великдень - попом.'))

# Task 2



    koshuk = {
            "паска": 1,
            "ковбаса": 2,
            "сир": 2,
            "яйця": 10
        }
    prices = {
            "паска": 45,
            "ковбаса": 250,
            "сир": 200,
            "яйця": 3.5
        }
koshuk_price = {k: koshuk[k] * prices[k] if k in koshuk.keys() and prices.keys() else 0 for k in prices}

total = sum(value for _, value in koshuk_price.items() if value > 0)

print(koshuk_price)
print(total, 'грн.' )

#Task 3
i = [i for i in range(1,11)]
j = [i**2 for i in range(1,11)]
print(list(zip(i, j)))


base_numbers = [2, 3, 4, 5]
exponent = 3
result = [pow(base, exponent) for base in base_numbers]
print(f"O resultado de elevar cada número base ao expoente {exponent} é:")
for i, base in enumerate(base_numbers):
    print(f"{base} ^ {exponent} = {result[i]}")

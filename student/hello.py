inp = int(input("Enret: "))
a = {
    4: "a",
    3: 'b',
    2: 'c',
    1: 'e'
}

if inp in a:
    print(a.get(inp))
else:
    print("0")

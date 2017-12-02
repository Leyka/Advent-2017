def main(): 
  
    total = 0

    with open('input.txt', 'r') as file: 
        data = file.read()
        
        for index, value in enumerate(data):
            if value == data[(index+1) % len(data)]: # Circular comparison with last index and first index
                total += int(value)
            
    print("part one: " + total)

if __name__ == '__main__': 
    main() 
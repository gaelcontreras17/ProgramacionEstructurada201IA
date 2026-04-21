print("  ", end=" ")
for col in range(1, 16):
    if col < 10:
        print(col, end="  ")
    else:
        print(col, end=" ")
print()

print("   " + "*** " * 15)


for row in range(1, 5):
    
    print(row, end="* ")
    
    for col in range(1, 16):
        resultado = row * col
        
      
        if resultado < 10:
            print(resultado, end="  ") 
        elif resultado < 100:
            print(resultado, end=" ")
            
    print()
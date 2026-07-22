import sys

def main():
    total_sum = 0
    
    
    for line in sys.stdin:
        
        num = int(line.strip())
        
        
        if num == 0:
            break
            
        
        total_sum += num
        
    
    print(total_sum)

if __name__ == "__main__":
    main()

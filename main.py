# python3

def parallel_processing(n, m, data):
    output = []
    threads=[(i,0) for i in range(n)]
    
    for i in range(m):
        
       index,start=min(threads,key=lambda x:x[1]) 
       
       output.append((index,start+time))
       threads[index]=(index,start+data[i])
    return output

def main():
    n,m = map(int, input().split())
    data=list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    
    for index,start in result:
        print(index,start)



if __name__ == "__main__":
    main()

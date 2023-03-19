# python3

def parallel_processing(n, m, data):
    output = []
    threads=[(i,0) for i in range(n)]
    
    for i in range(m):
        
       index,time=min(threads,key=lambda x: x[1]) 
       output.append((index,time))
       threads[index]=(index,time+data[i])
    return output

def main():
    n,m = map(int, input().split())
    data=list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    
    for index,time in result:
        print(index,time)



if __name__ == "__main__":
    main()

# python3

def parallel_processing(n, m, data):
    output = []
    threads=[(0,i) for i in range(n)]
    
    for i in range(m):
       thread,start=min(threads,key=lambda x:x[1]) 
       time=data[i]
        output.append((thread,start+time))
        assigned_jobs[thread]=(thread,start+data[i])
    return output

def main():
    n,m = map(int, input().split())
    data=list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    
    for thread,start in result:
        print(thread,start)



if __name__ == "__main__":
    main()

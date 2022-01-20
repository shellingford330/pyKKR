import multiprocessing

def conduct(value):
    pool_obj = multiprocessing.Pool(5)
    answer = pool_obj.map(sumall,range(0,value))
    print(answer)

def sumall(value):
      return sum(range(1, value + 1))

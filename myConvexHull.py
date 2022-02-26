import numpy as np

def ConvexHullMonic(bucket):
    #print("ASLI")
    #print(bucket[0,0])
    #bucketSorted = sorted(bucket, key=lambda x: (x[0], x[1]))

    #print("KEURUT")
    #print(bucketSorted[0])

    #max_index_col = np.argmax(bucket, axis=0)
    #min_index_col = np.argmin(bucket, axis=0)
    
    solution = np.array([[0,0]])

    #solution[0] = max_index_col
    #solution = np.vstack((solution, min_index_col))

    sort = sorted(bucket,key=lambda x:(x[0],x[1]))
    print(sort[0])
    print(sort[len(sort)-1])

    solution[0] = sort[0]
    solution = np.vstack((solution, bucket[len(sort)-1]))
    
    print(solution)

    s1 = np.array([[1, 2]])
    s1 = np.delete(s1, 0, axis=0)
    s2 = np.array([[1, 2]])
    s2 = np.delete(s2, 0, axis=0)



    #print(bucket[solution[0,0],0])
    #print(bucket[solution[0,0],1])
    #print(bucket[solution[0,1],0])
    #print(bucket[solution[0,1],1])
    #print(bucket[solution[1,0],0])
    #print(bucket[solution[1,0],1])
    #print(bucket[solution[1,1],0])
    #print(bucket[solution[1,1],1])



    matriks = np.array([[solution[0,0], solution[0,1], 1], [solution[1,0], solution[1,1], 1], [0,0,1]])
    

    for i  in range (len(bucket)):
        if((bucket[i,0] != solution[0,0] and bucket[i,1] != solution[0,1]) or (bucket[i,0] != solution[1,0] and bucket[i,1] != solution[1,1])):
            matriks[2,0] = bucket[i,0]
            matriks[2,1] = bucket[i,1]
            d = np.linalg.det(matriks)
            if(d > 0):
                s1 = np.vstack((s1, bucket[i]))
            else:
                s2 = np.vstack((s2, bucket[i]))

    print("s1")
    print(s1)
    print("s2")
    print(s2)


    #np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
    #result.append(bucketSorted[0])
    #result.append(bucketSorted[len(bucketSorted)-1])

    #print(result[0])
    #print(result[1])
    #print(bucket.index(result[0]))
    return solution


'''
Algorithm ConvexHull(P)
// P is a set of input points

Sort all the points in P and find two extreme points A and B
S1 ← Set of points right to the line AB  
S2 ← Set of points right to the line BA 
Solution ← AB followed by BA 

Call FindHull(S1, A, B)
Call FindHull(S2, B, A)



Algorithm FindHull(P, A, B)

if isEmpty(P) then
  return
else
  C ← Orthogonally farthest point from AB
  Solution ← Replace AB by AC followed by CB 
  Partition P – { C } in X0, X1 and X2
  Discard X0 in side triangle

  Call FindHull(X1, A, C)
  Call FindHull(X2, C, B)
end
'''
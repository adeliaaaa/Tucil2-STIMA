import numpy as np

def ConvexHullMonic(bucket):
    #print("ASLI")
    #print(bucket[0,0])
    #bucketSorted = sorted(bucket, key=lambda x: (x[0], x[1]))

    #print("KEURUT")
    #print(bucketSorted[0])

    #max_index_col = np.argmax(bucket, axis=0)
    #min_index_col = np.argmin(bucket, axis=0)
    
    solution = np.array([[0.0,0.0]])

    #solution[0] = max_index_col
    #solution = np.vstack((solution, min_index_col))

    sort = sorted(bucket,key=lambda x:(x[0],x[1]))
    print(sort[0])
    print(sort[len(sort)-1])

    solution[0] = sort[0]
    solution = np.vstack((solution, sort[len(sort)-1]))
    
    print(solution)


    #print(bucket[solution[0,0],0])
    #print(bucket[solution[0,0],1])
    #print(bucket[solution[0,1],0])
    #print(bucket[solution[0,1],1])
    #print(bucket[solution[1,0],0])
    #print(bucket[solution[1,0],1])
    #print(bucket[solution[1,1],0])
    #print(bucket[solution[1,1],1])

    matriks = np.array([[solution[0,0], solution[0,1], 1], [solution[1,0], solution[1,1], 1], [0,0,1]])
    s1 = np.array([[1.0, 2.0]])
    s1 = np.delete(s1, 0, axis=0)

    s2 = np.array([[1.0, 2.0]])
    s2 = np.delete(s2, 0, axis=0)
    

    for i  in range (len(bucket)):
        if((bucket[i,0] != solution[0,0] and bucket[i,1] != solution[0,1]) or (bucket[i,0] != solution[1,0] and bucket[i,1] != solution[1,1])):
            matriks[2,0] = bucket[i,0]
            matriks[2,1] = bucket[i,1]
            d = np.linalg.det(matriks)
            if(d > 0):
                s1 = np.vstack((s1, bucket[i]))
            else:
                s2 = np.vstack((s2, bucket[i]))

    solution = np.vstack((solution, findHull(solution, s1, solution[0], solution[1])))     
    solution = np.vstack((solution, findHull(solution, s2, solution[1], solution[0])))     

    #print("s1")
    #print(s1)
    #print("s2")
    #print(s2)


    #np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
    #result.append(bucketSorted[0])
    #result.append(bucketSorted[len(bucketSorted)-1])

    #print(result[0])
    #print(result[1])
    #print(bucket.index(result[0]))
    return solution


def findHull(solution, S,A,B):
    #print("Masuk sini---------------------------------")
    print("A,B,solution")
    print(A, B, solution)
    #print(A[1])
    #print(B[0])
    #print(B[1])
    #print("Masuk sini---------------------------------")
    if(S.size == 0):
        print('CEKTES---------------')
    else:
        # Find Orthogonally farthest point from AB
        fartest = S[0]
        tempDistance = 0.00
        for i in range (len(S)):
            sisiA = (((B[1] - A[1])**2) + ((B[0]-A[0])**2))**(1/2)
            sisiB = (((S[i,1] - A[1])**2) + ((S[i,0]-A[0])**2))**(1/2)
            sisiC = (((B[1] - S[i,1])**2) + ((B[0]-S[i,0])**2))**(1/2)
            setKel = (sisiA + sisiB + sisiC)/2
            jarak = (2/sisiA)*((setKel*(setKel-sisiA)*(setKel-sisiB)*(setKel-sisiC))**(1/2))
            #print(A[0])
            #print(A[1])
            #print(B[0])
            #print(B[1])
            #print(S[i,0])
            #print(S[i,1])
            #print(jarak)
            if(jarak.any() > tempDistance):
                tempDistance = jarak
                fartest = S[i]
        #panjangSolution = len(solution)
        solution = np.vstack((solution, fartest))
        #solution[panjangSolution - 1] = fartest
        print("fARTESTNYA")
        print(fartest)
        x1 = np.array([[1.0, 2.0]])
        x1 = np.delete(x1, 0, axis=0)

        x2 = np.array([[1.0, 2.0]])
        x2 = np.delete(x2, 0, axis=0) 

        for i  in range (len(S)):
            if (pointInTriangle(A[0], A[1], B[0], B[1], fartest[0], fartest[1], S[i,0], S[i,1]) == False) :
                if(fartest[0] > S[i,0]):
                    x1 = np.vstack((x1, S[i]))
                else:
                    x2 = np.vstack((x2, S[i]))

        findHull(solution, x1, A, fartest)
        findHull(solution, x1,fartest,B)

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
---------
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

def pointInTriangle(x1, y1, x2, y2, x3, y3, x, y):

    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / denominator
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / denominator
    c = 1 - a - b
 
    return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1

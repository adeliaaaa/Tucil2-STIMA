import numpy as np

def ConvexHullMonic(bucket):
 
    solution = np.array([[0.0,0.0]])



    sort = sorted(bucket,key=lambda x:(x[0],x[1]))
    #print(sort[0])
    #print(sort[len(sort)-1])

    solution[0] = sort[0]
    solution = np.vstack((solution, sort[len(sort)-1]))


    hulSim = np.array([[5, 5]])
    hulSim = np.delete(hulSim, 0, axis=0)


    s1 = np.array([[1.0, 2.0]])
    s1 = np.delete(s1, 0, axis=0)

    s2 = np.array([[1.0, 2.0]])
    s2 = np.delete(s2, 0, axis=0)
    

    for i  in range (len(bucket)):
        if((bucket[i,0] != solution[0,0] and bucket[i,1] != solution[0,1]) or (bucket[i,0] != solution[1,0] and bucket[i,1] != solution[1,1])):
            if(findDeter(solution[0,0], solution[0,1], solution[1,0], solution[1,1], bucket[i,0], bucket[i,1]) > 0):    
                s1 = np.vstack((s1, bucket[i]))
            else:
                s2 = np.vstack((s2, bucket[i]))
   
    result = np.array([[1.0, 2.0]])
    result = np.delete(result, 0, axis=0)


    hulSim = np.append(hulSim, np.array(findHull(bucket, hulSim, solution, s1, solution[0], solution[1])), axis=0)
    hulSim = np.append(hulSim, np.array(findHull(bucket, hulSim,solution, s2, solution[1], solution[0])), axis=0)

    return hulSim


def findHull(bucket, hulSim,solution, S,A,B):

    if(S.size == 0):
        #print(S)
        #print(A)
        temp = np.array([[0, 0]])
        temp[0][0] = findIndex(bucket, A[0], A[1])
        temp[0][1] = findIndex(bucket, B[0], B[1])
        return temp
    else:
        # Find Orthogonally farthest point from AB
        solution = np.array([[1.0, 2.0]])
        solution = np.delete(solution, 0, axis=0)
        fartest = S[0]
        tempDistance = 0.00
        for i in range (len(S)):
            '''
            sisiA = (((B[1] - A[1])**2) + ((B[0]-A[0])**2))**(1/2)
            sisiB = (((S[i,1] - A[1])**2) + ((S[i,0]-A[0])**2))**(1/2)
            sisiC = (((B[1] - S[i,1])**2) + ((B[0]-S[i,0])**2))**(1/2)
            setKel = (sisiA + sisiB + sisiC)/2
            jarak = (2/sisiA)*((setKel*(setKel-sisiA)*(setKel-sisiB)*(setKel-sisiC))**(1/2))
            '''

            d = np.linalg.norm(np.cross(B-A, A-S[i]))/np.linalg.norm(B-A)

            if(d > tempDistance):
                tempDistance = d
                fartest = S[i]

        #solution = np.vstack((solution, fartest))

        x1 = np.array([[1.0, 2.0]])
        x1 = np.delete(x1, 0, axis=0)

        x2 = np.array([[1.0, 2.0]])
        x2 = np.delete(x2, 0, axis=0) 

        for i  in range (len(S)):
            if (pointInTriangle(A[0], A[1], B[0], B[1], fartest[0], fartest[1], S[i,0], S[i,1]) == False) :
                if(findDeter(A[0], A[1], fartest[0], fartest[1], S[i,0], S[i,1]) > 0):
                    x1 = np.vstack((x1, S[i]))
                else:
                    x2 = np.vstack((x2, S[i]))

        solution = np.append(solution, np.array(findHull(bucket, hulSim,solution, x1, A, fartest)), axis=0)
        solution = np.append(solution, np.array(findHull(bucket, hulSim,solution,x2,fartest,B)), axis=0)

        #print(solution)

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


def findDeter(a,b,c,d,x,y):
    matriks = np.array([[a, b, 1], [c, d, 1], [0,0,1]])    

    matriks[2,0] = x
    matriks[2,1] = y
    d = np.linalg.det(matriks)
        
        
    return d

def findIndex(bucket, x, y):
    for i in range (len(bucket)):
        if(bucket[i][0] == x and bucket[i][1] == y):
            return i

def findJarak(x,y,s,t):
    d = (((x-s)**2)+((y-t)**2))**(1/2)

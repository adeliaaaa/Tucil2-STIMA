import numpy as np

def ConvexHullMonic(bucket):
    solution = np.array([[0.0,0.0]])
    sort = sorted(bucket,key=lambda x:(x[0],x[1]))
    solution[0] = sort[0]
    solution = np.vstack((solution, sort[len(sort)-1]))

    hulSim = np.array([[5, 5]])
    hulSim = np.delete(hulSim, 0, axis=0)
    s1 = np.array([[1.0, 2.0]])
    s1 = np.delete(s1, 0, axis=0)
    s2 = np.array([[1.0, 2.0]])
    s2 = np.delete(s2, 0, axis=0)
    
    for i  in range (len(bucket)):
        if((bucket[i,0] != solution[0,0] or bucket[i,1] != solution[0,1]) or (bucket[i,0] != solution[1,0] or bucket[i,1] != solution[1,1])):
            if((findDeter(solution[0,0], solution[0,1], solution[1,0], solution[1,1], bucket[i,0], bucket[i,1]) > 0)):  
                if((abs(findDeter(solution[0,0], solution[0,1], solution[1,0], solution[1,1], bucket[i,0], bucket[i,1]))) > 1e-12):
                    s1 = np.vstack((s1, bucket[i]))
            else:
                if((abs(findDeter(solution[0,0], solution[0,1], solution[1,0], solution[1,1], bucket[i,0], bucket[i,1]))) > 1e-12):
                    s2 = np.vstack((s2, bucket[i]))

    #print("S1")
    #print(s1)
    #print("S2")
    #print(s2)

    hulSim = np.append(hulSim, np.array(findHull(bucket, hulSim, solution, s1, solution[0], solution[1])), axis=0)
    hulSim = np.append(hulSim, np.array(findHull(bucket, hulSim,solution, s2, solution[1], solution[0])), axis=0)

    return hulSim

def findHull(bucket, hulSim,solution, S,A,B):
    if(S.size == 0):
        temp = np.array([[0, 0]])
        temp[0][0] = findIndex(bucket, A[0], A[1])
        temp[0][1] = findIndex(bucket, B[0], B[1])

        print(temp)
        return temp
    else:
        solution = np.array([[1.0, 2.0]])
        solution = np.delete(solution, 0, axis=0)
        fartest = S[0]
        tempDistance = 0.00
        # Find Orthogonally farthest point from AB
        for i in range (len(S)):
            d = np.linalg.norm(np.cross(B-A, A-S[i]))/np.linalg.norm(B-A)

            if(d > tempDistance):
                tempDistance = d
                fartest = S[i]

        print("fartest", fartest)

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

        return solution

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
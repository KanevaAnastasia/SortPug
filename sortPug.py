def QSort(left, right):
  global c;
  key = a[(left + right) // 2][0];
  i = left;
  j = right;
  while True:
     while a[i][0] < key:
        i += 1;
     while a[j][0] > key:
        j -= 1;
     if i <= j:
       a[i], a[j] = a[j], a[i];
       i += 1;
       j -= 1;
     if i > j:
       break;
  if left < j:
      QSort(left, j);
  if i < right:
      QSort(i, right);
def ver(m):
    if m == 1:
        return "YES"
    for i in range(n):
        k = 0
        j = 0
        while j < len(A[a[i][0]]):
            if abs(i - A[a[i][0]][j]) % m == 0:
                k += 1;
                A[a[i][0]].pop(j)
                
            j += 1;
        if (k==0):
            return "NO"
            
    return "YES"
    
f = open('input.txt', 'r')
n, m = f.readline().split();
n = int(n);
m = int(m)
a = f.readline().split()
A = dict();
for i in range(n):
    a[i] = [int(a[i]), i]
    A[a[i][0]] = A.get(a[i][0],[])
    A[a[i][0]].append(a[i][1]);
QSort(0, len(a)-1);

f1 = open('output.txt', 'w')

f1.write(ver(m));
f.close()
f1.close()

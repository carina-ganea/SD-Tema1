import time
import math

def TLE(T):
    if time.time() - T > 10:
        return True
    return False


def pivot_mediana_BFPRT(A):
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]
    subliste = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]
    mediane = [sl[len(sl) // 2] for sl in subliste]
    return pivot_mediana_BFPRT(mediane)


def Verificare(v, initial):
    if len(v) != len(initial):
        return False
    else:
        initial.sort()
        for i in range(len(v)):
            if v[i] != initial[i]:
                return False
    return True


def MergeSort(v):
    if len(v) == 1:
        return v
    st = [x for x in v[:len(v) // 2]]
    dr = [x for x in v[len(v) // 2:]]
    st = MergeSort(st)
    dr = MergeSort(dr)
    rez = []
    i = j = 0
    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            rez.append(st[i])
            i += 1
        else:
            rez.append(dr[j])
            j += 1
    rez.extend(st[i:])
    rez.extend(dr[j:])
    return rez


def RadixSortBaza10(v):
    M = max(v)
    M = len(str(M))
    p = 1
    rez = [x for x in v]
    for i in range(M):
        C = [[] for x in range(10)]
        for x in rez:
            C[x // p % 10].append(x)
        rez = []
        for x in C:
            rez.extend(x)
        p *= 10
    return rez

def RadixSortBaza2(v):
    M = max(v)
    M = int(math.log(M,2)) + 1
    p = 0
    rez = [x for x in v]
    for i in range(M):
        C = [[],[]]
        for x in rez:
            C[(x >> p) % 2].append(x)
        rez = []
        for x in C:
            rez.extend(x)
        p = p + 1
    return rez


def QuickSort(v):
    if len(v) == 0:
        return []
    if len(v) == 1:
        return v
    p = pivot_mediana_BFPRT(v)
    st = []
    eq = []
    dr = []
    for x in v:
        if x < p:
            st.append(x)
        elif x == p:
            eq.append(x)
        else:
            dr.append(x)
    st = QuickSort(st)
    dr = QuickSort(dr)
    st.extend(eq)
    st.extend(dr)
    return st


def CountSort(v):
    t = time.time()
    frecv = [0 for i in range(max(v) + 1)]
    for x in v:
        frecv[x] += 1
    rez = []
    for x in range(max(v) + 1):
        if not TLE(t):
            while frecv[x] != 0:
                rez.append(x)
                frecv[x] -= 1
        else:
            return False
    return rez


def BubbleSort(v):
    t = time.time()
    ok = False
    rez = [x for x in v]
    while not ok:
        if TLE(t):
            return False
        ok = True
        for i in range(len(rez) - 1):
            if rez[i] > rez[i + 1]:
                c = rez[i]
                rez[i] = rez[i + 1]
                rez[i + 1] = c
                ok = False
    return rez


sortari = [sorted, BubbleSort, CountSort, RadixSortBaza10, RadixSortBaza2, MergeSort, QuickSort]

g = open("rezultat.out", "w")

for sortare in sortari:

    g.write(str(sortare) + ': \n')

    for i in range(1, 13):
        # citire
        file = "test" + str(i) + ".in"
        f = open(file)
        n = f.readline().split()
        v = [int(x) for x in f.readline().split()]
        f.close()

        g.write('\t' + file + ': ')

        # timp executie
        t = time.time()
        rez = sortare(v)
        if not rez:
            g.write('Depaseste 10 sec. timp de executie\n')
        else:
            g.write(str(time.time() - t) + ' sec. --> ')

            if Verificare(rez, v):
                g.write("Sortare corecta\n")
            else:
                g.write("Sortare incorecta\n")
    g.write('\n')

g.close()

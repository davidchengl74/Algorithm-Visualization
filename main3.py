

#CPSC Algorithm Class

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
#import numpy as np
import random


# set the style of the graph
plt.style.use('seaborn-pastel')

# input the size of the aay (list here)
# and shuffle the elements to create
# a random list
data=int(input("Data Type: Random = 1 or Reverse = 2 or Almost sorted = 3"))
if data == 1:
    n = int(input("Enter # of data points (Entering a large number will have signicant slowdown)\n"))
    a = [i for i in range(1, n+1)]
    random.shuffle(a)
elif data == 2:
    n = int(input("Enter # of data points (Entering a large number will have signicant slowdown)\n"))
    a = [i for i in range(1, n+1)]
    a.sort(reverse=True)
elif data == 3:
    n = int(input("Enter # of data points (Entering a large number will have signicant slowdown)\n"))
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)
    for i in range(len(a)//2):
        min_idx = i
        for j in range(i + 1, len(a) - (len(a)//4)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
else:
    print("Error, program exits")
    exit()


print("\nInsertion sort = 1\n")
print("Selection Sort = 2\n")
print("Shellsort = 3\n")
print("Bubblesort = 4\n")
print("Mergesort = 5\n")
print("Quicksort = 6\n")
print("Quicksort 3-Way = 7\n")
m=int(input("Enter a sort type\n"))


#insertion sort
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1

        while(i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i -= 1
            yield a
        a[i+1] = key
        yield a

# selection sort
def selectionsort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
                yield a
        a[i],a[min_idx] = a[min_idx],a[i]
        yield a

# shell sort
def shellsort(a):
    gap = len(a) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(a):

            if a[i] >a[j]:
               yield a
               a[i],a[j] = a[j],a[i]
               yield a

            i += 1
            j += 1

            k = i
            while k - gap > -1:

                if a[k - gap] > a[k]:
                   yield a
                   a[k-gap],a[k] = a[k],a[k-gap]
                k -= 1

        gap //= 2
        yield a

# bubblesort
def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                yield a
                a[j],a[j+1] = a[j+1],a[j]
                yield a
    
# Merge sort
def mergeSort(a):
    size = len(a)
    result = []
    for i in range(size):
        result.append([])
        result[i].append(a[i])

    while size > 1:
        i = 0
        j = 0
        temp = []
        while i < size // 2:
            temp.append([])
            temp[i].extend(result[j])
            temp[i].extend(result[j + 1])
            temp[i].sort()
            yield sum(temp,[])
            i += 1
            j += 2
            
        if size % 2 == 1:
            temp.append([])
            temp[i].extend(result[j])
            yield sum(temp,[])
            size = size // 2 + 1
        else:
            size = size // 2

        result = list(temp)
        yield sum(result,[])


#Quicksort
def quicksort(a, l ,r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j] = a[j], a[l]
    yield a

    yield from quicksort(a, l, j - 1)
    yield from quicksort(a, j + 1, r)

# Quick Sort 3-Way
def quicksort3(a):
    f =  0
    l = len(a) - 1
    quicksort3Helper(a, f, l)

def swap (a, i , j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
#Quick Sort 3 -way helper function
def quicksort3Helper(a, f , l):
    if (f >= l):
        return
    if (f - l == 1):
        if a[f] < a[l]:
            swap(a, f, l)
        return

    x, y = quicksort3Partition(a, f, l)
    quicksort3Helper(a, f, x)
    quicksort3Helper(a, y, l)
#quicksort 3 way partition
def quicksort3Partition(a, f, l):
    mid = f
    pivot = a[l]

    while mid <= l:
        if a[mid] < pivot:
            swap(a, f, mid)
            f += 1
            mid += 1
        elif a[mid]  > pivot:
            swap(a, mid, l)
            l -=1
        else:
            mid +=1
    return f - 1, mid



# generator object returned by the function
if m==1:
    generator= insertionsort(a)
    plottype= "Running Insertion Sort"
if m==2:
    generator = selectionsort(a)
    plottype = "Running Selection Sort"
if m==3:
    generator = shellsort(a)
    plottype = "Running Shell Sort"
if m==4:
    generator = bubblesort(a)
    plottype = "Running Bubble Sort"
    #generator == shellsort(a)
if m == 5:
    generator = mergeSort(a)
    plottype = "Running Merge Sort"
if m == 6:
    generator = mergeSort(a)
    plottype = "Running QuickSort Sort"

if m == 7:
    generator = mergeSort(a)
    plottype = "Running QuickSort 3-Way Sort"

# to set the colors of the bars.
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.7, 0.7),
                (1.0, 0, 0)],
        "blue": [(0, 1, 1),
                (1.0, 0, 0)]
    }
)


fig, ax = plt.subplots()

# the bar container
rects = ax.bar(range(len(a)), a, align="edge",
            color=color_map(data_normalizer(range(n))))

# setting the view limit of x and y axes
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*len(a)))

# the text to be shown on the upper left
# indicating the number of iterations

text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]

# function to be called repeatedly to animate

def animate(A, rects, iteration):

    # setting the size of each bar equal
    # to the value of the elements
    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))


anim = FuncAnimation(fig, func=animate,
                    fargs=(rects, iteration), frames=generator, interval=20,
                    repeat=False)



ax.set_title(plottype)
fig.suptitle(str(n) + " Data Points", fontsize=12)

plt.show()
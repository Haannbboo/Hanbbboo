# Q11
class Node(object):
    def __init__(self, **kwargs):
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        self.data = kwargs.get('data', None)


class MyTree(object):
    def __init__(self, **kwargs):
        self.root = Node(**kwargs)

    def is_empty(self):
        return self.root is None

t = MyTree(data=83, left=Node(data=79, left=Node(data=76), right=Node(data=75)),
           right=Node(data=72, left=Node(data=70), right=Node(data=68)))

def preorder(root):
    if not isinstance(root, Node):
        return
    result = []
    if root:
        result.append(root.data)
        result.append(preorder(root.left))
        result.append(preorder(root.right))
    return result


def inorder(root):
    if not isinstance(root, Node):
        return
    result = []
    if root:
        result.append(preorder(root.left))
        result.append(root.data)
        result.append(preorder(root.right))
    return result


def postorder(root):
    if not isinstance(root, Node):
        return
    result = []
    if root:
        result.append(preorder(root.left))
        result.append(preorder(root.right))
        result.append(root.data)
    return result


# Q15
import pandas as pd
def table(values):
    df = pd.DataFrame()
    limit = 4
    for counter1 in range(0, limit):
        mini = counter1
        print('counter1: '+str(counter1))
        print('mini_counter1: '+ str(mini))
        
        for counter2 in range(counter1+1, limit+1):
            if values[counter2] < values[mini]:
                mini = counter2
                print('mini_counter2: '+ str(mini))
            print('counter2: '+str(counter2))
        if mini != counter1:
            print('temp: '+str(values[mini]))
            values[mini], values[counter1] = values[counter1], values[mini]
    return values

values = [20, 6, 38, 50, 40]


def code(values):
    limit = 4    
    flag = True
    
    while flag is True:
        flag = False
        for counter in range(0, limit):
            if values[counter] > values[counter+1]:
                values[counter], values[counter+1] = values[counter+1], values[counter]
                flag = True
    return values


# Q17
import random

def generate_data():
    chars = [chr(i) for i in range(97, 97+27)]
    cities = ['Beijing', 'Shanghai', 'Shenyang', 'Dalian', 'Cardiff']
    
    last_name = ''.join([random.choice(chars) for _ in range(random.randint(3, 10))])
    first_name = ''.join([random.choice(chars) for _ in range(random.randint(3, 10))])
    city = random.choice(cities)
    address1 = ''.join([random.choice(chars) for _ in range(random.randint(3, 15))]) + ' neighboor'
    address2 = ''.join([random.choice(chars) for _ in range(random.randint(3, 15))]) + ' street'
    address3 = ''.join([random.choice(chars) for _ in range(random.randint(3, 15))]) + ' district'
    postcode = random.randint(100000, 101000)
    
    return [last_name, first_name, address1, address2, address3, city, postcode]

data = [generate_data() for _ in range(512)]


def search():
    search = "Cardiff"
    total = 0

    for i in range(0, 511):
        if search == data[i][5]:
            total += 1

    return total


# merge sort

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    length = len(arr) // 2
    left = arr[ :length]
    right = arr[length: ]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
            
        else:
            result.append(right.pop(0))
            
    result += right
    result += left

    return result

array = [11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]
# output: [11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]





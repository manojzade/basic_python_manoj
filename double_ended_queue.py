class double_ended_queue:

    def __init__(self):
        """
           Define an empty stack
           Here we are using empty list to implement the stack data structure
        """
        self._list = []

    def isEmpty(self):
        if len(self._list) == 0:
            return True
        else:
            return False

    def remove_front(self):
        self._list.pop(0)

    def remove_rear(self):
        self._list.pop()

    def add_front(self, item):
        self._list.insert(0, item)

    def add_rear(self, item):
        self._list.append(item)

    def size(self):
        return len(self._list)
    def getcahr(self, index):
        return self._list[index]

    def get_rear_cahr(self):
        return self._list[-1]

def ck_palindrom(text):
    flag = False
    dq = double_ended_queue()
    for i in text:
        dq.add_rear(i)
    # print(dq)
    i =0
    while dq.size() > 1:

        # dq.remove_front()
        # print(dq.getcahr(i))
        # if (dq.remove_front() == dq.remove_rear()):
        if (dq.getcahr(i) == dq.get_rear_cahr()):
            flag = True
            a = dq.remove_front()
            b = dq.remove_rear()
            # print(a)
        else:
            flag = False
            break
    print(flag)


ck_palindrom('radar')
ck_palindrom('radar1')
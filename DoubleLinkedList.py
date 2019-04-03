#Класс-узел списка Node:
class Node:
    #Конструктор:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next  = next

    #Метод преобразования в строку:
    def __repr__(self):
        return repr(self.data)

#Класс двусвязного списка:
class DoubleLinkedList:
    #Конструктор:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    #Преобразование к строке:
    def __repr__(self):
        Nodes = []
        сurrent = self.head
        while сurrent:
            Nodes.append(repr(сurrent))
            сurrent = сurrent.next
        return '[' + ', '.join(Nodes) + ']'

    def __getitem__(self, key):
        current = self.head
        count = 0
        while current and count != key:
            count += 1
            current = current.next
        return current

    def __setitem__(self, key, val):
        current = self.head
        count = 0
        while current and count != key:
            count += 1
            current = current.next
        current.data = val

    #Вставить элемент в конец списка:
    def append(self, data):
        if not self.head:
            self.head = self.tail = Node(data = data)
            self.length += 1
            return
        сurrent = self.tail
        сurrent.next = self.tail = Node(data = data, prev = сurrent)
        self.length += 1

    #Найти элемент в списке:
    def find(self, key):
        сurrent = self.head
        while сurrent and сurrent.data != key:
            сurrent = сurrent.next
        return сurrent.data

    #Удалить элемент по ключу
    def delKey(self, key):
        self.head
        if not self.head:
            return
        old = current = self.head
        count = 0
        if key == 0:
            self.head = self.head.next
            return
        while current:
            if count == key:
                if current.next == self.tail:
                    self.tail = current
                    break
                else:
                    old.next = current.next
                break
            old = current
            current = current.next
            count += 1

    #Удалить узел из списка:
    def delete(self, Node):
        if Node.prev:
            Node.prev.next = Node.next
        if Node.next:
            Node.next.prev = Node.prev
        if Node is self.head:
            self.head = Node.next
        if Node is self.tail:
            self.tail = Node.prev
        Node.prev = None
        Node.next = None

    #Узнать длину списка
    def getLenght(self) -> int:
        length = 0
        if not self.head:
            return 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length


dll = DoubleLinkedList()

with open("list.txt", "r") as file:
    dll = file.readline().split()

print(dll)
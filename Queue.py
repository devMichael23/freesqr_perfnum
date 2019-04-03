#Класс-узел очереди:
class QNode:
    #Конструктор:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    #Метод преобразования узла в строку:
    def __repr__(self):
        return repr(self.data)

#Класс очереди:
class Queue:
    #Конструктор:
    def __init__(self, size = 0):
        self.head = None
        self.size = 0
        
    #Преобразование к строке:
    def __repr__(self):
        QNodes = []
        Curr = self.head
        if not self.head:
            return '[' + ', '.join(QNodes) + ']'
        if not Curr.next:
            QNodes.append(repr(Curr))
        else:
            QNodes.append(repr(Curr))
            Curr = self.head.next
            while Curr:
                QNodes.append(repr(Curr))
                Curr = Curr.next
        return '[' + ', '.join(QNodes) + ']'

    #Поместить в очередь:
    def Enqueue(self, data):
        if not self.head:
            self.head = QNode(data)
            self.size += 1
            return
        else:
            Curr = self.head
            while Curr.next:
                Curr = Curr.next
            Curr.next = QNode(data)
            self.size += 1

    #Удалить из очереди:
    def Dequeue(self):
        if self.size == 0:
            print ("Очередь пуста")
        else:
            if not self.head.next:
                Buff = self.head
                self.head = self.head.next
                self.size -= 1
                return Buff.data 
            else:
                Curr = Buff = self.head
                while Curr:
                    Curr = Curr.next
                self.head = Buff.next
                Curr = self.head
                self.size -= 1
                return Buff.data

    #Детектор простого числа:
    def PerfectNumberCounter(self):
        current = self.head
        count = 0
        while current:
            d = 2
            while d*d <= current.data and current.data % d != 0:
                d += 1
            if d*d > current.data:
                count +=1
                current = current.next
            else:
                current = current.next
                continue
        return count-1

q = Queue()
q.Enqueue(1)
q.Enqueue(2) #
q.Enqueue(3) #
q.Enqueue(4)
q.Enqueue(5) #
q.Enqueue(6)
q.Enqueue(7) #
q.Enqueue(8)
q.Enqueue(9)
q.Enqueue(10)
q.Enqueue(11) #
q.Enqueue(12)

print(q.PerfectNumberCounter())



class Subject:
    def __init__(self):
        self.observers = {}

    def subscribe(self, observer):
        self.observers[observer.id] = observer

    def unsubscribe(self, observer):
        del self.observers[observer.id]

    def notify(self, id):
        if id in self.observers:
            self.observers[id].update(id)
        else:
            print(f"Ningún observador coincide con el ID {id}.")


class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, received_id):
        if received_id == self.id:
            print(f"¡El ID {received_id} coincide con el ID del Observador {self.id}!")


class ObserverA(Observer):
    def __init__(self):
        super().__init__("ABCD")


class ObserverB(Observer):
    def __init__(self):
        super().__init__("EFGH")


class ObserverC(Observer):
    def __init__(self):
        super().__init__("IJKL")


class ObserverD(Observer):
    def __init__(self):
        super().__init__("MNOP")


if __name__ == "__main__":
    subject = Subject()
    observer_a = ObserverA()
    observer_b = ObserverB()
    observer_c = ObserverC()
    observer_d = ObserverD()

    subject.subscribe(observer_a)
    subject.subscribe(observer_b)
    subject.subscribe(observer_c)
    subject.subscribe(observer_d)

    ids = ["ABCD", "1234", "EFGH", "5678", "IJKL", "9101", "MNOP", "1112"]
    print("Emisión de IDs:")
    for id in ids:
        subject.notify(id)

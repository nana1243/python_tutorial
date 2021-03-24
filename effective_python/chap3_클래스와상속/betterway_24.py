"""
겍체를 범용으로 생성하려면 @classmethod 다형성을 이용하자

"""
import os
from threading import Thread


class Input(object):
    def read(self):
        raise NotImplementedError


class PathInputData(Input):
    def __init__(self, path):
        super().__init__()
        self.path = path

    # 처리할 바이트 데이터를 반환하는 표준 인터페이스인 read를 구현할 것이다
    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineWorker(Worker):
    def map(self):
        data = self.input_data.read()  # PathInputData class에서 샤용되는 함
        self.result = data.count("\n")

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]

    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)  # data를 읽어오고
    workers = create_workers(inputs)  # workers 들을 만들고
    return execute(workers)

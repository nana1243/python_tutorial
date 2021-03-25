"""
겍체를 범용으로 생성하려면 @classmethod 다형성을 이용하자

1. 파이썬에서는 클래스별로 생성자 한개를 만들 수 있다.
2. 클래스에 필요한 다른 생성자를 정의하려면, @classmethod를 사용하자
3. 구체서브 클래스들을 만들고 연결하는 범용적인 방법을 제공하려면, 클래스 메서드 다형성을 이용하자!

[이전의 설계의 문제점]
** map_reduce 함수가 전혀 범용적이지 않다는 점이다.
- 다른 언어에서는 이 문제가 다형성으로 해결된다.
이 문제를 해결하는 가장 좋은 방법은 classmethod 다형성을 이용하는 것이다.
->생성된 객체가 아니라 전체 클래스에 적용 된다는 점만 빼면,
read에 사용한 인스턴스 메서드 다형성과 똑같다.


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

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


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
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other):
        self.result += other.result

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


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

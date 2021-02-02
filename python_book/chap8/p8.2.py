charles = {"name": "Charles L. Dodgson", "born": 1982}

lewis = charles

print(lewis is charles)  # id 함수로 이사실을 확인한
lewis["balance"] = 950
print(charles)

alex = {"name": "Charles L. Dodgson", "born": 1982, "balance": 950}

print(alex is lewis)

""" dict 클래스에서 __eq__()를 구현하는 방식 때문에 두 객체를 비교해서 같다고 판단한다"""
print(alex == charles)  # 동일한 값을 갖고 있지만, 서로 다른 객체에 바인딩됨

print(alex is not charles)

# import inspect

promos = [
    globals()[name]
    for name in globals()
    if name.endswith("_promo") and name != "best_promo"
]


def best_promo(order):
    """최대로 할인받을 금액을 반환한다"""
    return max(promo(order) for promo in promos)


# 새로운 promotions 모듈을 내부 조사해서 만든 promos 리스트

# promos = [
#     func for name,func in inspect.getmembers(promotions,inspect.isfunction)
# ]

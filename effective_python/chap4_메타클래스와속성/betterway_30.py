"""
30. 속성을 리팩토링 하는 대신에, @property를 고려하자

- 기존의 인스턴스 속성에 새 기능을 부여하려면, @property를 사용하자
- @property를 사용하여 점점 나은 데이터 모델로 발전시키자
- @property를 너무 많이 사용하면, 클래스와 이를 호출하는 모든 곳을
    리팩토링 하는 방안을 고러하자

"""
from datetime import datetime, timedelta


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.rest_time = datetime.now()
        self.quota = 0
        self.max_quota = 0
        self.quota_consumed = 0

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # 새 기간의 할당량을 리셋
            self.quota_consumed = 0
            self.max_quota = 0

        elif delta < 0:
            # 새 기간의 할당량을 채움.
            assert self.quota_consumed == 0
            self.max_quota = amount

        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

    def __repr__(self):
        return "Bucket(quota = %d)" % self.quota

    def fill(self, bucket, amount):
        now = datetime.now()
        if now - bucket.rest_time > bucket.period_delta:
            bucket.quota = 0
            bucket.rest_time = now
        bucket.quota += amount

    def deduct(self, bucket, amount):
        now = datetime.now()
        if now - bucket.rest_time > bucket.period_delta:
            return False
        if bucket.quota - amount < 0:
            return False
        bucket.quota -= amount
        return True


bucket = Bucket(60)
bucket.fill(bucket, 100)
print(bucket.quota)

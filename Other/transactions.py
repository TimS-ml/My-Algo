from typing import *


class KVStore:
    def __init__(self):
        self.stack = [{}]

    def set(self, key: Any, value: Any):
        """O(1)"""
        self.stack[-1][key] = value

    def get(self, key: Any) -> Optional[Any]:
        """O(transaction)"""
        for i in range(len(self.stack) - 1, -1, -1):
            if key in self.stack[i]:
                return self.stack[i][key]

    def begin(self):
        """O(1)"""
        self.stack.append({})

    def commit(self):
        """O(n_keys)"""
        last_dic = self.stack.pop()

        for k, v in last_dic.items():
            self.stack[-1][k] = v

    def rollback(self):
        """O(1)"""
        self.stack.pop()


def test_KVStore():
    kv = KVStore()
    kv.set(1, 3)

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_single_transaction():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4


def test_KVStore_rollback():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_multiple_begin():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)

    kv.begin()
    kv.set(3, 5)

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) == None
    assert kv.get(3) == None


from collections import deque
from typing import Any, Optional


class DB:
    def __init__(self):
        self.current = {}
        self.stack = deque()
        self.open_transactions = 0

    def get(self, value: Any) -> Optional[Any]:
        return self.current.get(value)

    def set(self, key: Any, value: Any) -> None:
        if self.open_transactions == 0:
            self.current[key] = value
            return

        self.stack.append({key: value})

    def delete(self, key: int) -> None:
        self.current.pop(key)

    def commit(self):
        if self.open_transactions == 0:
            return

        changes = {}
        while len(self.stack) > 0:
            curr = self.stack.pop()

            if curr == "X_BLOCK":
                break
            # for any/all transactions add to temporary change store
            changes.update(curr)

        # finally, update main data store
        self.current.update(changes)

        # reduce transaction count
        self._update_transaction_count(-1)

    def begin(self):
        self._update_transaction_count(1)
        self.stack.append("X_BLOCK")
        self.current = dict(self.current)

    def rollback(self):
        if self.open_transactions == 0:
            return

        while len(self.stack) != 0:
            curr = self.stack.pop()
            if curr == "X_BLOCK":
                break

        self._update_transaction_count(-1)

    def _update_transaction_count(self, val: int) -> None:
        self.open_transactions += val
        self.open_transactions = abs(self.open_transactions)

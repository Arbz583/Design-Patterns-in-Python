from abc import ABC, abstractmethod

class AuditTrail:

    def record(self):
        print("Auditing")


class Task(ABC):

    def __init__(self) -> None:
        self.audit_trail = AuditTrail()
    # you can not use __ ans abstractmethod together!
    @abstractmethod
    def _do_execute(self):
        pass

    def execute(self):
        self.audit_trail.record()
        self._do_execute()

class TransferMoneyTask(Task):

    def _do_execute(self):
        print("Trasferring money")

transfer_money_task = TransferMoneyTask()
transfer_money_task.execute()
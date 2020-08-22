from cms.core.db import pgdb


from cms.logic.common.user import UserRole, User, init_super_user
from cms.logic.question import Question
from cms.logic.record import TransactionRequest
from cms.logic.message import TransactionMessage
from cms.logic.record import TransactionRecord


pgdb.create_tables([UserRole, User])
pgdb.create_tables([Question, TransactionRequest, TransactionMessage, TransactionRecord])
init_super_user()
pgdb.close()

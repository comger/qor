"""
author comger@163.com
交易付费记录逻辑
用户允许自由发布问题, 问题允许被多个答复者进行交易报价, 用户只能选择一个答复者进行交易,
交易是一个线上交流及线上交线同步的过程，一但用户确认解决了问题，用户将按交易价格进行支付。
"""
from peewee import ForeignKeyField, FloatField, BooleanField
from pydantic import BaseModel, Field
from cms.core.db import DBBaseModel
from cms.logic.common.user import User
from cms.logic.request import TransactionRequest


class TransactionRecord(DBBaseModel):
    # 交易记录
    request = ForeignKeyField(TransactionRequest, backref='record')
    from_user = ForeignKeyField(User, backref='records_pay', help_text="付费用户")
    to_user = ForeignKeyField(User, backref='records_get', help_text="收费用户")
    amount = FloatField(help_text="金额")
    status = BooleanField(help_text="付费状态", default=0)
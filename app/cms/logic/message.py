"""
author comger@163.com
交易消息逻辑
用户允许自由发布问题, 问题允许被多个答复者进行交易报价, 用户只能选择一个答复者进行交易,
交易是一个线上交流及线上交线同步的过程，一但用户确认解决了问题，用户将按交易价格进行支付。
"""
from peewee import ForeignKeyField, TextField, BooleanField
from pydantic import BaseModel, Field
from cms.core.db import DBBaseModel
from cms.logic.common.user import User
from cms.logic.request import TransactionRequest


class TransactionMessage(DBBaseModel):
    # 交易消息
    request = ForeignKeyField(TransactionRequest, backref='messages')
    user = ForeignKeyField(User, backref='messages', help_text="用户")
    message = TextField(help_text="消息主体")
    status = BooleanField(help_text="消息是否已读")

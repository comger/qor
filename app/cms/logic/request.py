"""
author comger@163.com
交易请求逻辑
用户允许自由发布问题, 问题允许被多个答复者进行交易报价, 用户只能选择一个答复者进行交易,
交易是一个线上交流及线上交线同步的过程，一但用户确认解决了问题，用户将按交易价格进行支付。
"""
from peewee import CharField, ForeignKeyField, TextField, IntegerField, FloatField
from pydantic import BaseModel, Field
from cms.core.db import DBBaseModel
from cms.logic.common.user import User
from cms.logic.question import Question


class TransactionRequest(DBBaseModel):
    # 交易请求
    question = ForeignKeyField(Question, backref='transactions', help_text="请求的问题")
    user = ForeignKeyField(User, backref='requests', help_text="请求用户")
    message = CharField(help_text="交易请求表白")
    price = FloatField(help_text="请求报价")
    # status 0: 新请求，1: 确认请求, 2: 交易成功, 3: 交易失败
    status = IntegerField(default=0, help_text="交易状态")
    # 一个提问, 每个用户只能做一次交易请求

    class Meta:
        indexes = (
            (('question', 'user'), True),
        )

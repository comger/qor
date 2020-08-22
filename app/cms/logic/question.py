"""
author comger@163.com
用户提问逻辑
用户允许自由发布问题, 问题允许被多个答复者进行交易报价, 用户只能选择一个答复者进行交易,
交易是一个线上交流及线上交线同步的过程，一但用户确认解决了问题，用户将按交易价格进行支付。
"""
from peewee import CharField, ForeignKeyField, TextField, IntegerField, FloatField
from playhouse.postgres_ext import ArrayField
from pydantic import BaseModel, Field
from cms.core.db import DBBaseModel
from cms.logic.common.user import User


class Question(DBBaseModel):
    # 问题
    question = CharField(help_text="问题描述")
    user = ForeignKeyField(User, backref='question', help_text="提问者")
    tags = ArrayField(CharField, null=True, default=[])

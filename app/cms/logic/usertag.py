"""
author comger@163.com
用户关注领域逻辑
每个用户可以选择最多3个领域作为自己专业所在, 系统会按领域匹配程度推送问题给用户
usertag {
    uid: xxx,
    tag: xxx
}
"""
from peewee import CharField, ForeignKeyField
from pydantic import BaseModel, Field
from cms.core.db import DBBaseModel
from cms.logic.common.crud import CRUDBase
from cms.logic.common.user import User


class UserTag(DBBaseModel):
    uid = ForeignKeyField(User, backref='usertags')
    tag = CharField()


class UserTagBase(BaseModel):
    uid: str = Field(..., title="用户ID")
    tag: str = Field(..., title="标签")


class UserTagCreate(UserTagBase):
    pass


class UserTagUpdate(UserTagBase):
    pass


class UserTagOut(UserTagBase):
    id: int = Field(..., title="ID")


class CRUDUserTag(CRUDBase[UserTag, UserTagCreate, UserTagUpdate, UserTagOut]):
    pass


crud_usertag = CRUDUserTag(UserTag)
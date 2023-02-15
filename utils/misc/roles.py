from enum import Enum


class UserRole(Enum):
    NOT_REG_USER = "not_reg_user"
    USER = "user"
    ADMIN = "admin"
    SUB = "sub"
    BAN = "ban"
    BLOCKED = "blocked"
    VIP = 'vip'

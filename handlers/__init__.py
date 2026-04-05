# handlers package
from .user_handlers import register as register_user_handlers
from .file_handlers import register as register_file_handlers
from .payment_handlers import register as register_payment_handlers
from .admin_handlers import register as register_admin_handlers

__all__ = [
    'register_user_handlers',
    'register_file_handlers', 
    'register_payment_handlers',
    'register_admin_handlers'
]

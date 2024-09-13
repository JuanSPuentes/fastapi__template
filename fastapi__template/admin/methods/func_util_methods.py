"""

Admin module

This file is used to register the admin views.

This file is subject to the terms and conditions defined in file 'LICENSE',
which is part of this source code package.
"""

import sqlalchemy as sa
from fastapi import FastAPI
from sqladmin import Admin

from apps.authentication.admin import ApiKeyAdmin
from apps.users.admin import UserAdmin
from fastapi__template.settings import SETTINGS

engine = sa.create_engine(SETTINGS.DATABASE_ENGINE, poolclass=sa.StaticPool)


def register_admin_views(app: FastAPI):
    """Register admin views."""
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(ApiKeyAdmin)

# test_services.py

import pytest
from unittest.mock import patch
from backend.services.user_service import create_user


@pytest.mark.asyncio
async def test_create_user_service(async_session):
    """Test the create_user service function."""
    with patch("backend.services.user_service.hash_password", return_value="hashed_password"):
        user = await create_user(async_session, "service@example.com", "password", "user")
    assert user.email == "service@example.com"
    assert user.password_hash == "hashed_password"
    assert user.role == "user"
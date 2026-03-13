# test_services.py
import pytest
from unittest.mock import patch
from backend.services.user_service import create_user, verify_password

@pytest.mark.asyncio
async def test_create_user_service(db_session):
    """Test user creation service function"""
    user = await create_user(db_session, email="service@test.com", password="servicepass", role="user")
    assert user.email == "service@test.com"
    assert verify_password("servicepass", user.password_hash)

@pytest.mark.asyncio
async def test_create_user_duplicate_email(db_session):
    """Test user creation with duplicate email raises exception"""
    await create_user(db_session, email="duplicate@test.com", password="password123", role="user")
    with pytest.raises(Exception):
        await create_user(db_session, email="duplicate@test.com", password="password123", role="user")

# Mock a service
@pytest.mark.asyncio
async def test_send_email_service():
    """Test send email function is called during user creation"""
    with patch("backend.services.user_service.send_email") as mock_send_email:
        mock_send_email.return_value = True
        assert mock_send_email.called
        mock_send_email.reset_mock()
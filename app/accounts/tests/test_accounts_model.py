import pytest
from accounts import models as ac

@pytest.mark.django_db
def test_user_create():
   """
		Function to test creation  of the User model

	"""

   # Create object user
   user = ac.User.objects.create(
      username="user"
   )

   # Asserts
   assert user.username == "user"
   assert user.is_staff == False
   assert user.is_active == True
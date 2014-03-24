from django import test

from compareuser.models import CompareUser
from compareobject.models import CompareObjectType


class CompareUserTestCase(test.TestCase):
    
    def test_new_user_has_repository(self):
        
        user = CompareUser.objects.create(
            username="test",
            email="test@test.com"
        )
        
        self.assertIsNotNone(user.repository)
        
    def test_new_user_has_default_allowed_object_types(self):
        
        object_type = CompareObjectType.objects.create(name="test", default=True)
        
        user = CompareUser.objects.create(
            username="test",
            email="test@test.com"
        )
        
        self.assertIn(object_type, user.allowed_object_types.all())
        
    def test_new_user_doesnt_have_not_default_allowed_object_types(self):
        
        object_type = CompareObjectType.objects.create(name="test", default=False)
        
        user = CompareUser.objects.create(
            username="test",
            email="test@test.com"
        )
        
        self.assertNotIn(object_type, user.allowed_object_types.all())
        
    def test_user_dont_loose_assigned_allowed_object_types(self):
        
        object_type1 = CompareObjectType.objects.create(name="test1", default=False)
        object_type2 = CompareObjectType.objects.create(name="test2", default=True)
        
        user = CompareUser.objects.create(
            username="test",
            email="test@test.com"
        )
        
        user.allowed_object_types.add(object_type1)
        user.save()

        self.assertIn(object_type2, user.allowed_object_types.all())
        
    def test_user_doesnt_gain_default_allowed_object_types(self):
        
        user = CompareUser.objects.create(
            username="test",
            email="test@test.com"
        )
        
        object_type = CompareObjectType.objects.create(name="test1", default=True)
        
        user.username = "test2"
        user.save()
        
        self.assertNotIn(object_type, user.allowed_object_types.all())
        
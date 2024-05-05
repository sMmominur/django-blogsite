from ..models import Category

class CategoryService:
    @staticmethod
    def get_active_categories():
        return Category.objects.filter(status='Active')

    @staticmethod
    def get_inactive_categories():
        return Category.objects.filter(status='Inactive')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

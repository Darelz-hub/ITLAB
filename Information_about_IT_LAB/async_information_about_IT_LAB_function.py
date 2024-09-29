from asgiref.sync import sync_to_async

from Information_about_IT_LAB.models import Documents, CategoryDocument


@sync_to_async()
def get_category_id(name):
    category = CategoryDocument.objects.get(name=name)
    return category.id
async def get_documents(category):
    documents = Documents.objects.filter(category=category)
    documents_list = []
    async for document in documents:
        documents_list.append(document)
    return documents_list
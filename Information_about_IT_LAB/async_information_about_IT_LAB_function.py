from asgiref.sync import sync_to_async

from Information_about_IT_LAB.models import Documents, CategoryDocument, Management


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

async def get_managers():
    managers = Management.objects.all()
    managers_list = []
    async for manager in managers:
        managers_list.append(manager)
    return managers_list
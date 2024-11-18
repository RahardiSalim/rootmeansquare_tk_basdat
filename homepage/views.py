from django.shortcuts import render

# View for categories and subcategories
def homepage(request):
    # Hardcoded data for categories and subcategories
    categories = [
        {'name': 'Kategori Jasa 1', 'subcategories': ['Subkategori Jasa 1', 'Subkategori Jasa 2', 'Subkategori Jasa 3']},
        {'name': 'Kategori Jasa 2', 'subcategories': ['Subkategori Jasa 1', 'Subkategori Jasa 2', 'Subkategori Jasa 3']},
        {'name': 'Kategori Jasa 3', 'subcategories': ['Subkategori Jasa 1', 'Subkategori Jasa 2', 'Subkategori Jasa 3']},
    ]

    # Handle filtering
    selected_category = request.GET.get('category', None)
    search_query = request.GET.get('search', '')

    if selected_category:
        categories = [cat for cat in categories if cat['name'] == selected_category]

    if search_query:
        for cat in categories:
            cat['subcategories'] = [sub for sub in cat['subcategories'] if search_query.lower() in sub.lower()]

    return render(request, 'homepage.html', {'categories': categories})

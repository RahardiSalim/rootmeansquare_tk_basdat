from django.shortcuts import render, redirect

# Dummy data for categories, subcategories, and orders
CATEGORIES = {
    'Home Cleaning': ['Setrika', 'Daily Cleaning', 'Pembersihan Dapur'],
    'Massage': ['Full Body Massage', 'Foot Massage', 'Head Massage']
}

ORDERS = [
    {
        'id': 1,
        'subcategory': 'Setrika',
        'customer': 'John Doe',
        'order_date': '2024-11-01',
        'job_date': '2024-11-03',
        'price': 50000,
        'status': 'Mencari Pekerja Terdekat',
    },
    {
        'id': 2,
        'subcategory': 'Daily Cleaning',
        'customer': 'Jane Smith',
        'order_date': '2024-11-02',
        'job_date': '2024-11-04',
        'price': 75000,
        'status': 'Mencari Pekerja Terdekat',
    },
    {
        'id': 3,
        'subcategory': 'Pembersihan Dapur',
        'customer': 'Robert Brown',
        'order_date': '2024-11-05',
        'job_date': '2024-11-07',
        'price': 60000,
        'status': 'Mencari Pekerja Terdekat',
    },
]

JOBS = [
    {
        'id': 1,
        'subcategory': 'Setrika',
        'customer': 'John Doe',
        'order_date': '2024-11-01',
        'job_date': '2024-11-03',
        'price': 50000,
        'status': 'Menunggu Pekerja Berangkat',
    },
    {
        'id': 2,
        'subcategory': 'Daily Cleaning',
        'customer': 'Jane Smith',
        'order_date': '2024-11-02',
        'job_date': '2024-11-04',
        'price': 75000,
        'status': 'Pekerja Tiba Di Lokasi',
    },
    {
        'id': 3,
        'subcategory': 'Pembersihan Dapur',
        'customer': 'Robert Brown',
        'order_date': '2024-11-05',
        'job_date': '2024-11-07',
        'price': 60000,
        'status': 'Pelayanan Jasa Sedang Dilakukan',
    },
]

STATUS_OPTIONS = [
    'Menunggu Pekerja Berangkat',
    'Pekerja Tiba Di Lokasi',
    'Pelayanan Jasa Sedang Dilakukan',
    'Pesanan Selesai',
    'Pesanan Dibatalkan',
]

def pekerjaan_jasa_view(request):
    selected_category = request.GET.get('category')
    selected_subcategory = request.GET.get('subcategory')
    
    # Filter subcategories based on selected category
    subcategories = CATEGORIES.get(selected_category, []) if selected_category else []

    # Filter orders based on selected category and subcategory
    filtered_orders = [order for order in ORDERS if order['status'] == 'Mencari Pekerja Terdekat']
    if selected_subcategory:
        filtered_orders = [order for order in filtered_orders if order['subcategory'] == selected_subcategory]

    context = {
        'categories': CATEGORIES.keys(),
        'subcategories': subcategories,
        'orders': filtered_orders,
        'selected_category': selected_category,
        'selected_subcategory': selected_subcategory,
    }

    if request.method == 'POST':
        # Handle "Kerjakan Pesanan" action
        order_id = int(request.POST.get('order_id'))
        for order in ORDERS:
            if order['id'] == order_id:
                order['status'] = 'Menunggu Pekerja Terdekat'
        return redirect('pekerjaan_jasa')

    return render(request, 'pekerjaan_jasa.html', context)


def status_pekerjaan_view(request):
    search_name = request.GET.get('name', '')
    search_status = request.GET.get('status', '')

    # Filter jobs based on search criteria
    filtered_jobs = JOBS
    if search_name:
        filtered_jobs = [job for job in filtered_jobs if search_name.lower() in job['subcategory'].lower()]
    if search_status:
        filtered_jobs = [job for job in filtered_jobs if job['status'] == search_status]

    if request.method == 'POST':
        job_id = int(request.POST.get('job_id'))
        for job in JOBS:
            if job['id'] == job_id:
                # Update job status sequentially
                if job['status'] == 'Menunggu Pekerja Berangkat':
                    job['status'] = 'Pekerja Tiba Di Lokasi'
                elif job['status'] == 'Pekerja Tiba Di Lokasi':
                    job['status'] = 'Pelayanan Jasa Sedang Dilakukan'
                elif job['status'] == 'Pelayanan Jasa Sedang Dilakukan':
                    job['status'] = 'Pesanan Selesai'
        return redirect('status_pekerjaan')

    context = {
        'jobs': filtered_jobs,
        'status_options': STATUS_OPTIONS,
        'search_name': search_name,
        'search_status': search_status,
    }
    return render(request, 'status_pekerjaan.html', context)

from django.shortcuts import render, redirect
from django.utils.timezone import now

# View for subcategory services
def subcategory_services_user(request, subcategory_name):
    # Hardcoded data for subcategory services
    subcategory = {
        'name': subcategory_name,
        'category': 'Kategori Jasa 1',
        'description': 'Deskripsi dari subkategori jasa yang telah dipilih.',
        'services': [
            {'name': 'Sesi Layanan 1', 'price': 'Rp 50,000'},
            {'name': 'Sesi Layanan 2', 'price': 'Rp 100,000'},
        ],
        'workers': ['Pekerja 1', 'Pekerja 2', 'Pekerja 3', 'Pekerja 4'],
        'testimonials': [
            {
                'user_name': 'Pengguna A',
                'date': '2024-11-01',
                'worker_name': 'Pekerja 1',
                'rating': '5/5',
                'text': 'Pelayanan sangat memuaskan!',
            },
        ],
    }
    return render(request, 'subcategory_user.html', {'subcategory': subcategory})

def subcategory_services_worker(request, subcategory_name):
    # Hardcoded data for subcategory services (same structure as above)
    subcategory = {
        'name': subcategory_name,
        'category': 'Kategori Jasa 1',
        'description': 'Deskripsi dari subkategori jasa yang telah dipilih.',
        'services': [
            {'name': 'Sesi Layanan 1', 'price': 'Rp 50,000'},
            {'name': 'Sesi Layanan 2', 'price': 'Rp 100,000'},
        ],
        'workers': ['Pekerja 1', 'Pekerja 2', 'Pekerja 3', 'Pekerja 4'],
        'testimonials': [
            {
                'user_name': 'Pengguna A',
                'date': '2024-11-01',
                'worker_name': 'Pekerja 1',
                'rating': '5/5',
                'text': 'Pelayanan sangat memuaskan!',
            },
        ],
    }
    return render(request, 'subcategory_worker.html', {'subcategory': subcategory})


# Simpan data pesanan (hardcoded untuk demo)
# Dummy data orders
orders = [
    {
        'subcategory': 'Subkategori Jasa 1',
        'service_session': 'Sesi Layanan 1',
        'price': 'Rp 50,000',
        'worker_name': 'Pekerja 1',
        'status': 'Menunggu Pembayaran',
        'date': '2024-11-17 14:30:00',
        'discount_code': 'DISKON50',
        'payment_method': 'E-Wallet',
        'testimonial_created': False,
    },
    {
        'subcategory': 'Subkategori Jasa 2',
        'service_session': 'Sesi Layanan 2',
        'price': 'Rp 100,000',
        'worker_name': 'Pekerja 2',
        'status': 'Mencari Pekerja Terdekat',
        'date': '2024-11-17 15:00:00',
        'discount_code': 'DISKON20',
        'payment_method': 'Transfer Bank',
        'testimonial_created': False,
    },
    {
        'subcategory': 'Subkategori Jasa 3',
        'service_session': 'Sesi Layanan 3',
        'price': 'Rp 75,000',
        'worker_name': 'Pekerja 3',
        'status': 'Pesanan Selesai',
        'date': '2024-11-16 10:00:00',
        'discount_code': '',
        'payment_method': 'Cash',
        'testimonial_created': False,
    },
    {
        'subcategory': 'Subkategori Jasa 1',
        'service_session': 'Sesi Layanan 4',
        'price': 'Rp 120,000',
        'worker_name': 'Pekerja 4',
        'status': 'Menunggu Pembayaran',
        'date': '2024-11-18 08:30:00',
        'discount_code': 'DISKON30',
        'payment_method': 'E-Wallet',
        'testimonial_created': True,
    }
]


def create_order(request):
    if request.method == 'POST':
        # Ambil data dari form
        order_date = now().strftime('%Y-%m-%d %H:%M:%S')
        discount_code = request.POST.get('discount_code', '')
        total_payment = request.POST.get('total_payment', 'Rp 0')
        payment_method = request.POST.get('payment_method', 'Unknown')
        status = 'Menunggu Pembayaran'

        # Tambahkan ke daftar pesanan
        orders.append({
            'subcategory': 'Subkategori Jasa',
            'service_session': 'Sesi Layanan 1',
            'price': total_payment,
            'worker_name': 'Pekerja 1',
            'status': status,
            'date': order_date,
            'discount_code': discount_code,
            'payment_method': payment_method,
        })

        # Redirect ke halaman pesanan jasa
        return redirect('view_orders')

    # Tambahkan 'current_date' ke konteks
    return render(request, 'create_order_modal.html', {'current_date': now().strftime('%Y-%m-%d %H:%M:%S')})


def view_orders(request):
    # Filter berdasarkan query string jika ada
    subcategory_filter = request.GET.get('subcategory', None)
    status_filter = request.GET.get('status', None)

    # Salin data pesanan
    filtered_orders = orders

    # Filter jika ada parameter
    if subcategory_filter:
        filtered_orders = [order for order in filtered_orders if order['subcategory'] == subcategory_filter]
    if status_filter:
        filtered_orders = [order for order in filtered_orders if order['status'] == status_filter]

    # Tambahkan logika tombol ke setiap pesanan
    for order in filtered_orders:
        order['show_cancel_button'] = order['status'] in ["Menunggu Pembayaran", "Mencari Pekerja Terdekat"]
        order['show_testimonial_button'] = order['status'] == "Pesanan Selesai" and not order.get('testimonial_created', False)

    return render(request, 'view_orders.html', {'orders': filtered_orders})

from django.shortcuts import render

def profil_pekerja(request):
    # Hardcoded testimonials
    testimonials = [
        {
            "user_name": "Jane Doe",
            "date": "2024-11-01",
            "rating": 5,
            "text": "Pekerjaan sangat memuaskan!"
        },
        {
            "user_name": "Mike Smith",
            "date": "2024-11-02",
            "rating": 4,
            "text": "Pelayanan cepat dan ramah."
        },
        {
            "user_name": "Alice Johnson",
            "date": "2024-11-03",
            "rating": 3,
            "text": "Hasil kerja cukup baik, tapi bisa lebih baik lagi."
        }
    ]

    # Render template with hardcoded data
    return render(request, 'profil_pekerja.html', {
        "testimonials": testimonials
    })

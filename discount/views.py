from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime, timedelta

def diskon_view(request):
    # Dummy data for vouchers
    vouchers = [
        {
            'code': 'SAVE10',
            'discount': '10%',
            'min_order': 100000,
            'validity_days': 30,
            'quota': 100,
            'price': 50000
        },
        {
            'code': 'MEGA20',
            'discount': '20%',
            'min_order': 200000,
            'validity_days': 15,
            'quota': 50,
            'price': 75000
        },
        {
            'code': 'SUPER30',
            'discount': '30%',
            'min_order': 300000,
            'validity_days': 7,
            'quota': 25,
            'price': 100000
        }
    ]

    # Dummy data for promos
    promos = [
        {
            'code': 'NEWYEAR2024',
            'end_date': '2024-01-31'
        },
        {
            'code': 'CHINESE2024',
            'end_date': '2024-02-15'
        }
    ]

    # Dummy user balance
    user_balance = 80000

    context = {
        'vouchers': vouchers,
        'promos': promos,
        'user_balance': user_balance
    }
    
    return render(request, 'discount.html', context)

def buy_voucher(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        voucher_code = data.get('voucher_code')
        user_balance = 80000  # Dummy user balance

        # Dummy voucher data
        vouchers = {
            'SAVE10': {'price': 50000, 'validity_days': 30, 'quota': 5},
            'MEGA20': {'price': 75000, 'validity_days': 15, 'quota': 3},
            'SUPER30': {'price': 100000, 'validity_days': 7, 'quota': 2}
        }

        if voucher_code in vouchers:
            voucher = vouchers[voucher_code]
            if user_balance >= voucher['price']:
                # Calculate expiry date
                expiry_date = (datetime.now() + timedelta(days=voucher['validity_days'])).strftime('%d/%m/%Y')
                
                return JsonResponse({
                    'status': 'success',
                    'message': f'Selamat! Anda berhasil membeli voucher kode {voucher_code}. '
                              f'Voucher ini akan berlaku hingga tanggal {expiry_date} '
                })
            else:
                return JsonResponse({
                    'status': 'failed',
                    'message': 'Maaf, saldo Anda tidak cukup untuk membeli voucher ini.'
                })
        else:
            return JsonResponse({
                'status': 'failed',
                'message': 'Kode voucher tidak valid!'
            })

    return JsonResponse({
        'status': 'failed',
        'message': 'Invalid request method!'
    })
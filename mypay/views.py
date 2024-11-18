from django.shortcuts import render, redirect
from datetime import date

# User data
USER_DATA = {
    'name': 'John Doe',  # Tambahkan nama pengguna
    'phone': '081234567890',
    'balance': 1000000,
    'transactions': [
        {'amount': 50000, 'date': '2024-11-01', 'category': 'TopUp'},
        {'amount': -20000, 'date': '2024-11-10', 'category': 'Withdrawal'},
        {'amount': 100000, 'date': '2024-11-15', 'category': 'TopUp'},
    ],
}

# Available services and banks
SERVICES = [
    {'id': 1, 'name': 'Cleaning Service', 'price': 50000},
    {'id': 2, 'name': 'Repair Service', 'price': 75000},
    {'id': 3, 'name': 'Gardening Service', 'price': 60000},
]

BANKS = ['BCA', 'Mandiri', 'BNI', 'OVO', 'GoPay']

# MyPay main view (shows balance and transaction history)
def mypay_view(request):
    context = {
        'user': USER_DATA,
    }
    return render(request, 'mypay/mypay.html', context)

# MyPay transaction form view
def mypay_transaction_view(request):
    context = {
        'user': USER_DATA,
        'services': SERVICES,
        'banks': BANKS,
        'date': date.today(),
    }

    if request.method == 'POST':
        category = request.POST.get('category')  # Get transaction category
        context['category'] = category  # Add category to the context

        # Handle form submission based on the category
        if category == 'TopUp':
            nominal = request.POST.get('nominal')
            if nominal:
                nominal = int(nominal)
                USER_DATA['balance'] += nominal  # Update balance
                USER_DATA['transactions'].append({
                    'amount': nominal,
                    'date': str(date.today()),
                    'category': 'TopUp',
                })
        elif category == 'PayService':
            service_id = request.POST.get('service')
            service = next((s for s in SERVICES if str(s['id']) == service_id), None)
            if service:
                USER_DATA['balance'] -= service['price']  # Deduct service price
                USER_DATA['transactions'].append({
                    'amount': -service['price'],
                    'date': str(date.today()),
                    'category': service['name'],
                })
        elif category == 'Transfer':
            no_hp = request.POST.get('no_hp')
            nominal = request.POST.get('nominal')
            if nominal:
                nominal = int(nominal)
                USER_DATA['balance'] -= nominal  # Deduct transferred amount
                USER_DATA['transactions'].append({
                    'amount': -nominal,
                    'date': str(date.today()),
                    'category': f'Transfer to {no_hp}',
                })
        elif category == 'Withdraw':
            bank = request.POST.get('bank')
            account_number = request.POST.get('account_number')
            nominal = request.POST.get('nominal')
            if nominal:
                nominal = int(nominal)
                USER_DATA['balance'] -= nominal  # Deduct withdrawn amount
                USER_DATA['transactions'].append({
                    'amount': -nominal,
                    'date': str(date.today()),
                    'category': f'Withdrawal to {bank}',
                })

    return render(request, 'mypay/mypay_transaction.html', context)

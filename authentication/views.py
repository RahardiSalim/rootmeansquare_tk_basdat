from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegisterPenggunaForm, RegisterPekerjaForm, UpdatePenggunaForm, UpdatePekerjaForm

# Merged dummy data with staff status and all user information
DUMMY_USERS = [
    {
        'name': 'User1',
        'gender': 'L',
        'phone': '081234567890',
        'password': 'password1',
        'birth_date': '1990-01-01',
        'address': 'Jakarta',
        'balance': 1000000,
        'is_staff': False,
        'level': 'Gold',
    },
    {
        'name': 'User2',
        'gender': 'P',
        'phone': '081234567891',
        'password': 'password2',
        'birth_date': '1992-02-02',
        'address': 'Bandung',
        'balance': 2000000,
        'is_staff': False,
        'level': 'Silver',
    },
    {
        'name': 'User3',
        'gender': 'L',
        'phone': '081234567892',
        'password': 'password3',
        'birth_date': '1985-03-03',
        'address': 'Surabaya',
        'balance': 1500000,
        'is_staff': False,
        'level': 'Bronze',
    },
    {
        'name': 'User4',
        'gender': 'P',
        'phone': '081234567893',
        'password': 'password4',
        'birth_date': '1988-04-04',
        'address': 'Medan',
        'balance': 3000000,
        'is_staff': False,
        'level': 'Gold',
    },
    {
        'name': 'User5',
        'gender': 'L',
        'phone': '081234567894',
        'password': 'password5',
        'birth_date': '1991-05-05',
        'address': 'Yogyakarta',
        'balance': 2500000,
        'is_staff': False,
        'level': 'Silver',
    },
    {
        'name': 'User6',
        'gender': 'P',
        'phone': '081234567895',
        'password': 'password6',
        'birth_date': '1994-06-06',
        'address': 'Semarang',
        'balance': 3500000,
        'is_staff': True,
        'bank': 'Bank A',
        'account_number': '12345678',
        'npwp': '123-456-789',
        'photo_link': 'foto1.jpg',
        'rating': 4.5,
        'completed_orders': 100,
    },
    {
        'name': 'User7',
        'gender': 'L',
        'phone': '081234567896',
        'password': 'password7',
        'birth_date': '1996-07-07',
        'address': 'Makassar',
        'balance': 4000000,
        'is_staff': True,
        'bank': 'Bank B',
        'account_number': '23456789',
        'npwp': '234-567-890',
        'photo_link': 'foto2.jpg',
        'rating': 4.7,
        'completed_orders': 120,
    },
    {
        'name': 'User8',
        'gender': 'P',
        'phone': '081234567897',
        'password': 'password8',
        'birth_date': '1997-08-08',
        'address': 'Bali',
        'balance': 4500000,
        'is_staff': True,
        'bank': 'Bank C',
        'account_number': '34567890',
        'npwp': '345-678-901',
        'photo_link': 'foto3.jpg',
        'rating': 4.8,
        'completed_orders': 150,
    },
    {
        'name': 'User9',
        'gender': 'L',
        'phone': '081234567898',
        'password': 'password9',
        'birth_date': '1993-09-09',
        'address': 'Balikpapan',
        'balance': 5000000,
        'is_staff': True,
        'bank': 'Bank D',
        'account_number': '45678901',
        'npwp': '456-789-012',
        'photo_link': 'foto4.jpg',
        'rating': 4.6,
        'completed_orders': 130,
    },
    {
        'name': 'User10',
        'gender': 'P',
        'phone': '081234567899',
        'password': 'password10',
        'birth_date': '1995-10-10',
        'address': 'Lampung',
        'balance': 6000000,
        'is_staff': True,
        'address': 'Bank E',
        'account_number': '56789012',
        'npwp': '567-890-123',
        'photo_link': 'foto5.jpg',
        'rating': 4.9,
        'completed_orders': 200,
    },
]

def home_view(request):
    return render(request, 'homepageplaceholder.html')

def login_view(request):
    if request.session.get('is_authenticated', False):
        return redirect('authentication:homepage')
        
    if request.method == 'POST':
        no_hp = request.POST.get('no_hp')
        password = request.POST.get('password')
        
        # Find user in dummy data
        user = next((u for u in DUMMY_USERS if u['phone'] == no_hp and u['password'] == password), None)
        
        if user:
            # Create session data with complete user information
            request.session['user'] = user
            request.session['is_authenticated'] = True
            request.session['role'] = 'pekerja' if user['is_staff'] else 'pengguna'
            return redirect('authentication:homepage')
        else:
            messages.error(request, 'Invalid phone number or password.')
    
    return render(request, 'authentication/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('authentication:login')

def register_pengguna_view(request):
    if request.method == 'POST':
        form = RegisterPenggunaForm(request.POST)
        if form.is_valid():
            no_hp = form.cleaned_data['no_hp']
            if any(user['phone'] == no_hp for user in DUMMY_USERS):
                messages.error(request, 'Phone number already registered.')
                return render(request, 'authentication/register_pengguna.html', {'form': form})
            
            new_user = {
                'name': form.cleaned_data['username'],
                'gender': form.cleaned_data['gender'],
                'phone': no_hp,
                'password': form.cleaned_data['password1'],
                'birth_date': form.cleaned_data['tgl_lahir'].strftime('%Y-%m-%d'),
                'address': form.cleaned_data['alamat'],
                'balance': 0,
                'is_staff': False,
                'level': 'Bronze'  # Default level for new users
            }
            DUMMY_USERS.append(new_user)
            
            messages.success(request, 'Registration successful. Please login.')
            return redirect('authentication:login')
    else:
        form = RegisterPenggunaForm()
    
    return render(request, 'authentication/register_pengguna.html', {'form': form})

def register_pekerja_view(request):
    if request.method == 'POST':
        form = RegisterPekerjaForm(request.POST)
        if form.is_valid():
            no_hp = form.cleaned_data['no_hp']
            if any(user['phone'] == no_hp for user in DUMMY_USERS):
                messages.error(request, 'Phone number already registered.')
                return render(request, 'authentication/register_pekerja.html', {'form': form})
            
            npwp = form.cleaned_data['npwp']
            if any(user.get('npwp') == npwp for user in DUMMY_USERS if user.get('is_staff', False)):
                messages.error(request, 'NPWP already registered.')
                return render(request, 'authentication/register_pekerja.html', {'form': form})
            
            new_user = {
                'name': form.cleaned_data['username'],
                'gender': form.cleaned_data['gender'],
                'phone': no_hp,
                'password': form.cleaned_data['password1'],
                'birth_date': form.cleaned_data['tgl_lahir'].strftime('%Y-%m-%d'),
                'address': form.cleaned_data['alamat'],
                'balance': 0,
                'is_staff': True,
                'bank': form.cleaned_data['nama_bank'],
                'account_number': form.cleaned_data['no_rekening'],
                'npwp': npwp,
                'photo_link': 'default.jpg',
                'rating': 0,
                'completed_orders': 0
            }
            DUMMY_USERS.append(new_user)
            
            messages.success(request, 'Registration successful. Please login.')
            return redirect('authentication:login')
    else:
        form = RegisterPekerjaForm()
    
    return render(request, 'authentication/register_pekerja.html', {'form': form})

def profile_view(request):
    user_data = request.session.get('user', {})
    
    if not user_data:
        return redirect('authentication:login')

    if request.method == 'POST':
        form_class = UpdatePekerjaForm if user_data.get('is_staff', False) else UpdatePenggunaForm
        form = form_class(request.POST)

        if form.is_valid():
            # Update user data in session and dummy data
            updated_data = form.cleaned_data
            user_data.update(updated_data)
            request.session['user'] = user_data

            # Update dummy data
            for i, user in enumerate(DUMMY_USERS):
                if user['phone'] == user_data['phone']:
                    DUMMY_USERS[i].update(updated_data)
                    break

            messages.success(request, 'Profile updated successfully.')
            return redirect('authentication:profile')
    else:
        initial_data = {
            'username': user_data.get('name', ''),
            'no_hp': user_data.get('phone', ''),
            'gender': user_data.get('gender', ''),
            'tgl_lahir': user_data.get('birth_date', ''),
            'alamat': user_data.get('address', ''),
        }
        
        if user_data.get('is_staff', False):
            initial_data.update({
                'nama_bank': user_data.get('bank', ''),
                'no_rekening': user_data.get('account_number', ''),
                'npwp': user_data.get('npwp', ''),
            })
            form = UpdatePekerjaForm(initial=initial_data)
        else:
            form = UpdatePenggunaForm(initial=initial_data)

    context = {
        'user': user_data,
        'form': form
    }
    return render(request, 'authentication/profile.html', context)
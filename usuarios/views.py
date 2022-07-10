from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from validate_docbr import CPF

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        CPF = request.POST['CPF']
        idade = request.POST['idade']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if not CPF.strip():
            messages.error(request, 'O campo CPF não pode ficar em branco')
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')

        if  len(CPF) != 11 or len(set(CPF)) == 1:
            messages.error(request, 'CPF Inválido')
            print(CPF)
            print('cpf invalido')
            return redirect('cadastro')

        if len(CPF) ==11:
            Validacpf(CPF) == False
            messages.error(request, 'CPF Inválido')
            print(CPF)
            print('cpf invalido')
            return redirect('cadastro')

        if senhas_diferentes(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            print('As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=CPF).exists():
            messages.error(request, 'Usuário já cadastrado')
            print('Usuário já cadastrado')
            return redirect('cadastro')
            
        user = User.objects.create_user(username=nome, email=CPF, last_name=idade, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        CPF = request.POST['CPF']
        senha = request.POST['senha']
        if CPF == "" or senha == "":
            messages.error(request, 'Os campos CPF e senha não podem ficar em branco')
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
            print(CPF, senha)
        if User.objects.filter(email=CPF).exists():
            nome = User.objects.filter(email=CPF).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def senhas_diferentes(senha, senha2):
    return senha != senha2

def Validacpf(CPF):
    ocpf = CPF

    fatiacpf = CPF[:9]


    soma =0 
    for chave, multiplicador in enumerate(range(len(fatiacpf)+1, 1, -1 )):
        
        soma += int(fatiacpf[chave])* multiplicador
        

    resto = 11 -(soma%11)
    resto = resto if resto <=9 else 0


    fatiacpf2 = fatiacpf + str(resto)

    soma2 =0 
    for chave, multiplicador in enumerate(range(len(fatiacpf2)+1, 1, -1 )):
        
        soma2 += int(fatiacpf2[chave])* multiplicador
        

    resto2 = 11 -(soma2%11)
    resto2 = resto2 if resto2 <=9 else 0


    validacpf = fatiacpf + str(resto) 
        
    if fatiacpf + str(resto) +str(resto2) != ocpf :
        return False
    else:
        return True



def matricula_curso(request, avasus_id):
    matricula = get_object_or_404(Avasus, pk = avasus_id)
    matricula.add()
    return redirect('dashboard')
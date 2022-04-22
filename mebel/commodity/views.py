from django.shortcuts import render, redirect
from .forms import ContactForme, ProductForme,CrocekryForme,CreateUserForm ,UserCreationForm
from .models import Product, Crocekry


def register_user(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # print('aaaaaaaaaaaaaaaa')
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('sign_in')

    context = {'form': form}
    return render(request, 'commodity/sign_up.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('contact')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('contact')
            else:
                messages.info(request, "ERORR")

        context = {}

        return render(request, 'commodity/sign_in.html', context)


def logout_user(request):
    # if login_user is request.user.is_authenticated:
    logout(request)
    return redirect('contact')

    # else:
        # return render(request, 'commodity/sign_up.html')


def create_contact(request):
    form = ContactForme()
    if request.method == "POST":
        form = ContactForme(request.POST)
        if form.is_valid:
            form.save()
            return redirect("contact")
        else:
            print('dilshod')
    else:
        form =ContactForme()
    product = Product.objects.all()
    crocekry = Crocekry.objects.all()
    context = {
        "form": form,
        "product": product,
        "crocekry": crocekry

    }
    return render(request, "commodity/index.html", context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForme(instance=product)
    if request.method == "POST":
        form = ProductForme(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('contact')

    context = {
        "form": form
    }

    return render(request, "commodity/updateproduct.html", context)


def delete_product(request, pk):
    product =Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('contact')

    context = {
        "product": product
    }

    return render(request, 'commodity/delateproduct.html', context)


def create_product(request):
    form = ProductForme()
    if request.method == "POST":
        form =ProductForme(request.POST)
        if form.is_valid:
            form.save()
            return redirect("contact")
    else:
        form = ProductForme()

    context = {
        "form": form
    }
    return render(request, "commodity/updateproduct.html", context)


def update_crocekry(request, pk):
    crocekry = Crocekry.objects.get(id=pk)
    form = CrocekryForme(instance=crocekry)
    if request.method == "POST":
        form = CrocekryForme(request.POST, instance=crocekry)
        if form.is_valid:
            form.save()
            return redirect('contact')

    context = {
        "form": form
    }

    return render(request, "commodity/updatecrocekry.html", context)


def delete_crocekry(request, pk):
    crocekry =Crocekry.objects.get(id=pk)
    if request.method == 'POST':
        crocekry.delete()
        return redirect('contact')

    context = {
        "crocekry": crocekry
    }

    return render(request, 'commodity/delatecrocekry.html', context)


def create_crocekry(request):
    form = CrocekryForme()
    if request.method == "POST":
        form =CrocekryForme(request.POST)
        if form.is_valid:
            form.save()
            return redirect("contact")
    else:
        form = CrocekryForme()

    context = {
        "form": form
    }
    return render(request, "commodity/updatecrocekry.html", context)


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'commodity/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items(())))

# def product(request):
#     product = Product.objects.all()
#
#     context = {
#         "product": product
#     }
#     return render(request, "commodity/index.html", context)
















# from django.http import HttpResponse
#
#
# def index(request):
#     print(request)
#     return HttpResponse('')

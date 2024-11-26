from django.shortcuts import render, redirect
from django.views import View
from sqlalchemy import *

# Create your views here.
from .forms import *

con = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
conn = con.connect()


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        f = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        request.session["username"] = username
        request.session["password"] = password
        ddd = "LOGIN"
        st = text(f"SELECT * FROM {ddd} WHERE (username='{username}' AND password='{password}') ")
        rs = conn.execute(st)
        kk = rs.fetchall()
        print(kk)
        try:
            if kk[0]:
                self.request.session["login"] = "login"
                return redirect("print")
        except:
            return redirect("login")

from django.shortcuts import render
from sqlalchemy import *
from django.http import JsonResponse,HttpResponse
# Create your views here.
import pandas as pd
from requests import session
import requests
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views import View
import json

def logged_in(f):
    # @wraps(f)
    def decorated_func(request,*args,**kwargs):
        print(request.session.get("login"))
        if request.session.get("login"):
            return f(request,*args,**kwargs)

        # if request.session:
        #     return f(request,*args,**kwargs)
        # else:
        #     return redirect("/")
        # return f(request, *args, **kwargs)
    return decorated_func


def class_logged_in(f):
    # @wraps(f)
    def decorated_func(self,request,*args,**kwargs):
        print(self.request.session.get("login"))
        if self.request.session.get("login"):
            return f(self,request,*args,**kwargs)

        # if request.session:
        #     return f(request,*args,**kwargs)
        # else:
        #     return redirect("/")
        # return f(request, *args, **kwargs)
    return decorated_func

@logged_in
def db(request):
    con=create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn=con.connect()
    con2 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn2 = con2.connect()

    # metadata = MetaData() #extracting the metadata
    # datat= Table('FSI', metadata,
    # autoload_with=con) #Table object
    # re=pd.read_sql_query("SELECT * FROM FSI",conn)
    # query = datat.select() #SELECT * FROM divisions
    # print(query)
    ff=request.POST.get("name","")
    yy=request.POST.get("family","")
    rr=request.POST.get("national_number","")
    print(ff)
    dddd="SAMPLE"
    logg="LOG"
    username=request.session.get("username")
    password = request.session.get("password")
    print(username)
    print(password)
    if ff and yy and rr:
        st = text(
            f"SELECT * FROM {dddd} WHERE  (name LIKE N'%{ff}%' AND family LIKE N'%{yy}%' AND national_number LIKE '%{rr}%') ")
        rs = conn.execute(st)
        print(rs)
        lo = text(f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
        # lo=insert(logg).values(username=usrname)
        print(lo)
        # compiled = lo.compile()
        loo = conn2.execute(lo)
        conn2.commit()
        # print(loo)
        return render(request, "index.html", {"re": rs})
    elif (ff and yy) or (ff and rr) or (rr and yy) :
        st=text(f"SELECT * FROM {dddd} WHERE  (name LIKE N'%{ff}%' AND family LIKE N'%{yy}%') OR (name LIKE N'%{ff}%' AND national_number LIKE '%{rr}%') OR (national_number LIKE '%{rr}%' AND family LIKE N'%{yy}%') ")
        rs = conn.execute(st)
        print(rs)
        lo = text(f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
        # lo=insert(logg).values(username=usrname)
        print(lo)
        # compiled = lo.compile()
        loo = conn2.execute(lo)
        conn2.commit()
        # print(loo)
        return render(request,"index.html",{"re":rs})
    elif ff or yy or rr:
        gh=text(f"SELECT * FROM {dddd} WHERE name LIKE N'%{ff}%' OR family LIKE N'%{yy}%' OR national_number LIKE '%{rr}%'")
        kl = conn.execute(gh)
        lo = text(f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
        # lo=insert(logg).values(username=usrname)
        print(lo)
        # compiled = lo.compile()
        loo = conn2.execute(lo)
        conn2.commit()
        # print(loo)
        return render(request,"index.html",{'kl':kl})
    else:
        return render(request,"index.html")

class Run(View):




    @class_logged_in
    def get(self,request):
        return render(request,"index.html")

    # @require_http_methods(['POST'])
    # @logged_in
    def post(self,request):
        if request.method=='POST':
            con = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
            conn = con.connect()
            con2 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
            conn2 = con2.connect()

            # metadata = MetaData() #extracting the metadata
            # datat= Table('FSI', metadata,
            # autoload_with=con) #Table object
            # re=pd.read_sql_query("SELECT * FROM FSI",conn)
            # query = datat.select() #SELECT * FROM divisions
            # print(query)
            # ff = request.POST.get("search", "")
            # ff = request.POST.get("search_a", "")
            ff = request.POST.get("search_a2", "")
            yy = request.POST.get("search_a", "")
            print(ff)
            dddd = "FSI"
            logg = "LOG"
            username = request.session.get("username")
            password = request.session.get("password")
            print(username)
            print(password)
            if ff and yy:
                st = text(f"SELECT * FROM {dddd} WHERE (Country='{ff}' AND Year='{yy}') ")
                rs = conn.execute(st)
                print(rs)
                lo = text(f"INSERT INTO {logg} (username,search) VALUES ('{username}','{ff}')")
                # lo=insert(logg).values(username=usrname)
                print(lo)
                # compiled = lo.compile()
                loo = conn2.execute(lo)
                conn2.commit()
                print(loo)
                li=[]
                for r in rs:
                    gg=json.dumps(r)
                    li.append(gg)
                    print(gg)
                print(li)
                return JsonResponse( li,safe=False)
            else:
                gh = text(f"SELECT * FROM {dddd} WHERE Country='{ff}'")
                kl = conn.execute(gh)
                print(kl)
                lo = text(f"INSERT INTO {logg} (username,search) VALUES ('{username}','{ff}')")
                # lo=insert(logg).values(username=usrname)
                print(lo)
                # compiled = lo.compile()
                loo = conn2.execute(lo)
                conn2.commit()
                print(loo)
                for row in kl:
                    row_dict = dict(row._mapping)
                    print(row_dict)
                    json_data = json.dumps(row_dict)
                    print(json_data)
                    return JsonResponse(json_data,safe=False)
        return HttpResponse('')
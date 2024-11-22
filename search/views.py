from django.shortcuts import render
from sqlalchemy import *
from django.http import JsonResponse
# Create your views here.
import pandas as pd
from requests import session
import requests

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

# @logged_in
# def db(request):
#     con=create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
#     conn=con.connect()
#     con2 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
#     conn2 = con2.connect()
#
#     # metadata = MetaData() #extracting the metadata
#     # datat= Table('FSI', metadata,
#     # autoload_with=con) #Table object
#     # re=pd.read_sql_query("SELECT * FROM FSI",conn)
#     # query = datat.select() #SELECT * FROM divisions
#     # print(query)
#     ff=request.POST.get("search","")
#     yy=request.POST.get("year","")
#     print(ff)
#     dddd="FSI"
#     logg="LOG"
#     username=request.session.get("username")
#     password = request.session.get("password")
#     print(username)
#     print(password)
#     if ff and yy:
#         st=text(f"SELECT * FROM {dddd} WHERE (Country='{ff}' AND Year='{yy}') ")
#         rs = conn.execute(st)
#         print(rs)
#         lo = text(f"INSERT INTO {logg} (username) VALUES ('{username}')")
#         # lo=insert(logg).values(username=usrname)
#         print(lo)
#         # compiled = lo.compile()
#         loo = conn2.execute(lo)
#         conn2.commit()
#         # print(loo)
#
#
#
#         return render(request,"index.html",{"re":rs})
#     else:
#         gh=text(f"SELECT * FROM {dddd} WHERE Country='{ff}'")
#         kl = conn.execute(gh)
#
#         return render(request,"index.html",{'kl':kl})

from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views import View
import json
class Run(View):

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
            ff = request.POST.get("search", "")
            yy = request.POST.get("year", "")
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
                lo = text(f"INSERT INTO {logg} (username) VALUES ('{username}')")
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
                for row in kl:
                    row_dict = dict(row._mapping)
                    print(row_dict)
                    json_data = json.dumps(row_dict)

                    return JsonResponse(json_data,safe=False)

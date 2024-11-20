from django.shortcuts import render
from sqlalchemy import *
# Create your views here.
import pandas as pd
from requests import session
import requests

def logged_in(f):
    # @wraps(f)
    def decorated_func(request,*args,**kwargs):
        print(request.session.get("login"))
        if request.session.get("login"):
            return f(*args,**kwargs)

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
   
    # metadata = MetaData() #extracting the metadata
    # datat= Table('FSI', metadata,             
    # autoload_with=con) #Table object
    # re=pd.read_sql_query("SELECT * FROM FSI",conn)
    # query = datat.select() #SELECT * FROM divisions
    # print(query)
    ff=request.POST.get("search","")
    yy=request.POST.get("year","")
    print(ff)
    dddd="FSI"
    if ff and yy:
        st=text(f"SELECT * FROM {dddd} WHERE (Country='{ff}' AND Year='{yy}') ")
        rs = conn.execute(st)
        print(rs)
        return render(request,"index.html",{"re":rs})
    else:    
        gh=text(f"SELECT * FROM {dddd} WHERE Country='{ff}'")
        kl = conn.execute(gh)
  
        return render(request,"index.html",{'kl':kl})

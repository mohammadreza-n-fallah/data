import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from sqlalchemy import *
from sqlalchemy.dialects.mssql import NVARCHAR, INTEGER, FLOAT


def logged_in(f):
    # @wraps(f)
    def decorated_func(request, *args, **kwargs):
        print(request.session.get("login"))
        if request.session.get("login"):
            return f(request, *args, **kwargs)

        # if request.session:
        #     return f(request,*args,**kwargs)
        # else:
        #     return redirect("/")
        # return f(request, *args, **kwargs)

    return decorated_func


def class_logged_in(f):
    # @wraps(f)
    def decorated_func(self, request, *args, **kwargs):
        print(self.request.session.get("login"))
        if self.request.session.get("login"):
            return f(self, request, *args, **kwargs)

        # if request.session:
        #     return f(request,*args,**kwargs)
        # else:
        #     return redirect("/")
        # return f(request, *args, **kwargs)

    return decorated_func


@logged_in
def db(request):
    con = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn = con.connect()
    con2 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn2 = con2.connect()
    con3 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn3 = con3.connect()
    con4 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn4 = con4.connect()
    con5 = create_engine("mssql://@localhost/vvv?driver=ODBC Driver 17 for SQL Server")
    conn5 = con5.connect()

    # metadata = MetaData() #extracting the metadata
    # datat= Table('FSI', metadata,
    # autoload_with=con) #Table object
    # re=pd.read_sql_query("SELECT * FROM FSI",conn)
    # query = datat.select() #SELECT * FROM divisions
    # print(query)
    ff = request.POST.get("name", "")
    yy = request.POST.get("family", "")
    rr = request.POST.get("national_number", "")
    ee = request.POST.get("email", "")
    pp = request.POST.get("phone", "")
    print(ff)
    dddd = "SAMPLE"
    logg = "LOG"
    username = request.session.get("username")
    password = request.session.get("password")
    print(username)
    print(password)
    vb = text(f"SELECT name AS [text()] FROM sys.columns WHERE object_id = OBJECT_ID('dbo.SAMPLE') ")
    vm = conn3.execute(vb)
    ress = vm.fetchall()
    lii = [row[0].upper() for row in ress]
    # if ff:
    kkss = text("""

    CREATE OR ALTER PROCEDURE SearchProducts
      @Name NVARCHAR(50) = NULL,
        @Family NVARCHAR(50) = NULL,
        @National_Number NVARCHAR(50) = NULL,
        @Email NVARCHAR(50) = NULL,
        @Phone NVARCHAR(50) = NULL
        AS
        BEGIN
            SET NOCOUNT ON;
        
            DECLARE @SQL NVARCHAR(MAX);
            DECLARE @Params NVARCHAR(MAX);
        
            -- Base query
            SET @SQL = 'SELECT * FROM SAMPLE WHERE 1=1';
        
            -- Build conditions dynamically
            IF @Name IS NOT NULL
                SET @SQL += ' AND name = @Name';
        
            IF @Family IS NOT NULL
                SET @SQL += ' AND family LIKE ''%'' + @Family + ''%''';
        
            IF @National_Number IS NOT NULL
                SET @SQL += ' AND national_number = @National_Number';
        
            IF @Email IS NOT NULL
                SET @SQL += ' AND email = @Email';
        
            IF @Phone IS NOT NULL
                SET @SQL += ' AND phone = @Phone';
        
            -- Define parameters
            SET @Params = '@Name NVARCHAR(50), @Family NVARCHAR(50), @National_Number NVARCHAR(50), @Email NVARCHAR(50), @Phone NVARCHAR(50)';
            PRINT @SQL;
            -- Execute the query
            EXEC sp_executesql @SQL, @Params, @Name, @Family, @National_Number, @Email, @Phone;
        END;

""")

    kkssv = conn4.execute(kkss)
    # for i in kkssv:
    #     print(i)
    print("Stored procedure created/updated successfully.")

    # Execute the stored procedure
    execute_procedure = text(f"""
        EXEC SearchProducts 
            @Name = {f"N'{ff}'" if ff else 'NULL'} ,
            @Family = {f"N'{yy}'" if yy else 'NULL'},
            @National_Number = {f"N'{rr}'" if rr else 'NULL'},
            @Email = {f"N'{ee}'" if ee else 'NULL'},
            @Phone = {f"N'{pp}'" if pp else 'NULL'}
            
        
             
          
           
            
             
   
    """)


    kl = conn4.execute(
        execute_procedure
        # {
        #     "name": 'אופיר',
        # #     "family": yy,
        # #     "national_number": rr,
        #     "email": "shakedmiriam@gmail.com" or None,
        # #     "phone": pp,
        # }
    )
    # for kk in kl:
    #     print(kk)
    # result_data = [dict(row) for row in kl]
    # print("Query Results:", result_data)
    # render(request, "index.html", {"lii": lii, "kl": kl})
    # Close the connection
    # conn4.close()
    result_data = [row for row in kl]
    print("Query Results:", result_data)
    for kk in kl:
        print(kk)
    print(lii)

    conn4.close()
    return render(request, "index.html", {"lii": lii,"kl":result_data})
    # conn4.close()
    # if ff and yy and rr:
    #     st = text(
    #         f"SELECT * FROM {dddd} WHERE  (name LIKE N'%{ff}%' AND family LIKE N'%{yy}%' AND national_number LIKE '%{rr}%') ")
    #     rs = conn.execute(st)
    #     print(rs)
    #     lo = text(
    #         f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
    #     # lo=insert(logg).values(username=usrname)
    #     print(lo)
    #     # compiled = lo.compile()
    #     loo = conn2.execute(lo)
    #     conn2.commit()
    #     # print(loo)
    #     return render(request, "index.html", {"re": rs, "lii": lii})
    # elif ((ff and yy) or (ff and rr) or (ff and ee) or (ff and pp) or (yy and rr)or (yy and ee) or (yy and pp)
    #       or (rr and ee) or (rr and pp) or (ee and pp)):
    #     st = text(
    #         f"SELECT * FROM {dddd} WHERE  (name LIKE N'%{ff}%' AND family LIKE N'%{yy}%') OR (name LIKE N'%{ff}%' AND national_number LIKE '%{rr}%') OR (national_number LIKE '%{rr}%' AND family LIKE N'%{yy}%') ")
    #     rs = conn.execute(st)
    #     print(rs)
    #     lo = text(
    #         f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
    #     # lo=insert(logg).values(username=usrname)
    #     print(lo)
    #     # compiled = lo.compile()
    #     loo = conn2.execute(lo)
    #     conn2.commit()
    #     # print(loo)
    #     return render(request, "index.html", {"re": rs, "lii": lii})
    # elif ff or yy or rr or ee or pp:
    #     gh = text(
    #         f"SELECT * FROM {dddd} WHERE name LIKE N'%{ff}%' OR family LIKE N'%{yy}%' OR national_number LIKE '%{rr}%' OR email LIKE N'%{ee}%' OR phone LIKE N'%{pp}%'")
    #     kl = conn.execute(gh)
    #     lo = text(
    #         f"INSERT INTO {logg} (username,name,family,national_number) VALUES (N'{username}',N'{ff}',N'{yy}','{rr}')")
    #     # lo=insert(logg).values(username=usrname)
    #     print(lo)
    #     # compiled = lo.compile()
    #     loo = conn2.execute(lo)
    #     conn2.commit()
    #     # print(loo)
    #     return render(request, "index.html", {'kl': kl, "lii": lii})
    # else:
    # return render(request, "index.html", {"lii": lii})


class Run(View):

    @class_logged_in
    def get(self, request):
        return render(request, "index.html")

    # @require_http_methods(['POST'])
    # @logged_in
    def post(self, request):
        if request.method == 'POST':
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
                li = []
                for r in rs:
                    gg = json.dumps(r)
                    li.append(gg)
                    print(gg)
                print(li)
                return JsonResponse(li, safe=False)
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
                    return JsonResponse(json_data, safe=False)
        return HttpResponse('')
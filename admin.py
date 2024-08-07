from fasthtml.common import *
from hmac import compare_digest
import datetime

db = database('data/onboard.db')

#Create Database Tables

candidates,doc_types,users,candidate_docs,doc_configs,configs_doc_type = \
     db.t.candidates,db.t.doc_types,db.t.users \
    ,db.t.candidate_docs,db.t.doc_configs,db.t.configs_doc_type

if candidates not in db.t:
    candidates.create(dict(id=int,email=str,pwd=str 
                           ,first_name=str,last_name=str
                           ,status=str),pk="id")

if doc_types not in db.t:
    doc_types.create(dict( id=int,name=str,description=str
                          ,is_required=bool),pk="id")

if users not in db.t:
    users.create(id=int,username=str
                ,passwd=str,email=str,role=str,pk="id")

if doc_configs not in db.t:
    doc_configs.create(  id=int
                        ,name=str,description=str
                        ,created_by=str
                        ,pk="id")
    doc_configs.add_foreign_key('created_by','users','id')

if candidate_docs not in db.t:
    candidate_docs.create(   dict(id=int
                            ,file_path=str,upload_date=datetime.datetime
                            ,verification_status=str)
                            ,candidate_id=int
                            ,doc_types_id=int
                            ,pk="id")
    candidate_docs.add_foreign_key("candidate_id","candidates","id")
    candidate_docs.add_foreign_key("doc_types_id","doc_types","id")


if configs_doc_type not in db.t:
    configs_doc_type.create( doc_config_id=int,doc_types_id=int,
                            pk=("doc_config_id","doc_types_id"))
    configs_doc_type.add_foreign_key("doc_config_id","doc_configs","id")
    configs_doc_type.add_foreign_key("doc_types_id","doc_types","id")


# # create dataclasses
# Candiates=candidates.dataclass()
# DocumentType = doc_types.dataclass()
# Users = users.dataclass()
# DocumentConfig = doc_configs.dataclass()
# CandidateDocu = candidate_docs.dataclass()
# configDocuType = configs_doc_type.dataclass()

# login_redir = RedirectResponse("/login",status_code=303)
# signup_redir = RedirectResponse("/signup",status_code=303)

# # interceptor *Beforeware*
# def before(req,sess):
#     auth = req.scope["auth"]=sess.get('auth',None)
#     if not auth: return login_redir
#     DocumentConfig.xtra(created_by=auth)

# bware = Beforeware(before,skip=[r'/favicon\.ico',r'/static/*',r'.*\.css','/login'])

# def _not_found(req,exc): return Titled('Oh oh',Div("You landed in no man land"))

# app = FastHTML( before=bware
#                ,exception_handlers={404:_not_found}
#                ,hdrs=(picolink,SortableJS('.sortable'))
#                )

# rt = app.route
# @dataclass
# class Login: username: str; passwd: str
# @dataclass
# class Signup: username:str; passwd: str; retype_passwd: str;first_name: str; last_name: str

# def clr_signup(): return Div(hx_swap_oob='innerHTML',id='signup')

# @rt("/signup")
# def get():
#     frm = Form(
#         Input(id='email',placeholder='email@domain.com')
#         ,Input(id='passwd',type='password',placeholder='Password')
#         ,Input(id='retype_passwd',type='password',placeholder='Retype Password')
#         ,Button('signup')
#         ,Button("cancel",hx_get='/signup')
#         ,action='/signup',method='post'
#     )
#     return Titled('SignUp',frm)

# @rt("/signup")
# def post(login: Login):
#     pass

# @rt("/login")
# def get():
#     frm = Form(
#          Input(id='email',placeholder='email@domain.com')
#         ,Input(id='passwd',type='password',placeholder='Password')
#         ,Button('login')
#         ,action='/login',method='post'
#     )
#     return Titled('Login',frm)


# @rt("/login")
# def post(login:Login,sess):
#     if not login.username or not login.passwd: return login_redir
#     try:
#         u = users[login.username]
#     except NotFoundError: 
#         return signup_redir



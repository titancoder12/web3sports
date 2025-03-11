
Forked starter code from:
https://github.com/eugenelin89/django_rest_api 

Django Testing:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#locallibrary_tests

Making Queries with Django:
https://docs.djangoproject.com/en/4.1/topics/db/queries/
For demo on FE deployment see 1:19, https://www.youtube.com/watch?v=w7ejDZ8SWv8&list=PLRFqA66fjSmEmpa5Hw2VfnTHTA74jlAta&index=1&t=3605s

/myproject
This is the project directory

/myproject/myproject
This is the app directory. myproject is the "root" app.
setting.py is in this directory.


RAFCE to quickly create component.

Routing and Login:
https://blog.logrocket.com/complete-guide-authentication-with-react-router-v6/
https://codesandbox.io/s/react-router-v6-auth-demo-4jzltb

Local Dev Env:
http://127.0.0.1:8000/api/
http://localhost:3000/dashboar

authentication:
https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html
https://testdriven.io/blog/django-spa-auth/
https://medium.com/swlh/django-rest-framework-and-spa-session-authentication-with-docker-and-nginx-aa64871f29cd

Token Authentication Example:
(insure) mytutorial $ http POST http://localhost:8000/api-token-auth/ username='test' password='test123!'
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Date: Mon, 09 Jan 2023 22:08:00 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.10.6
Vary: Origin, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "token": "4df7736e1fc8ca1ecec9a0d6954500bf1a5ec2de"
}
curl -X GET http://127.0.0.1:8000/api/mybusiness/ -H 'Authorization: Token 4df7736e1fc8ca1ecec9a0d6954500bf1a5ec2de'
[{"id":3,"business_type":"http://127.0.0.1:8000/api/businesstype/1/","product":"http://127.0.0.1:8000/api/product/1/","client":"http://127.0.0.1:8000/api/clients/1/","status":"http://127.0.0.1:8000/api/businessstatus/1/","projected_FYC":1.0,"application_date":"2022-12-17","application_location":"Kaohsiung","created_by":"test","created_date":"2022-12-17T13:33:00Z","modified_date":"2022-12-17T13:33:00Z","highlighted":false}]

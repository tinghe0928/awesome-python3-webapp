#print("****************************************************************************************************************************************************************")
#
#
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)


#print("****************************************************************************************************************************************************************")

#
# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello1():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# @asyncio.coroutine
# def hello2():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello1(), hello2()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()



#print("****************************************************************************************************************************************************************")



# import asyncio
#
#
# async def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop1 = asyncio.get_event_loop()
#
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop1.run_until_complete(asyncio.wait(tasks))
# print('This is end')
# loop1.close()



#print("****************************************************************************************************************************************************************")

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
#
# g = foo()
#
# print(next(g))
# print("*"*20)
# print(next(g))
# print(next(g))


# print("****************************************************************************************************************************************************************")
#
#
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
#
#
# g = foo()
# print(next(g))
# print("*"*20)
# print(g.send(7))


##############################################################################################################################################################################################################################
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    home_message = '<h1>Home</h1>'
    return home_message


@app.route('/signin',methods=['GET'])
def signin_form():
    signin_form = '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
    return signin_form


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()


























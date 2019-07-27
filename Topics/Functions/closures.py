# Python Closures. A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
# https://youtu.be/swU3c34d2NQ

def logger(msg):

    def log_message():
        print('Log', msg)
    
    return log_message

log_hi = logger('Hi')
log_hi()


# 
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('test headline!')
print_h1('another headline!')
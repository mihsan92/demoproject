def add(x,y):
  '''adding two numbers'''
  return x + y

def subs(x,y):
  '''substracting two numbers'''
  return x - y

def mult(x,y):
  '''multiplying two numbers'''
  return x * y

def divide(x,y):
  '''divide two numbers'''
  if y == 0:
    return "Error. Can't be zero"
  else:
    return x / y
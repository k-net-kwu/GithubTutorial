# -*- coding: utf-8 -*-

def hello(name : str) -> None:
  print(f'hello {name}!')

def bye(name : str) -> None:
  print(f'bye {name}!') 
  
def main(): 
  NAME = 'Your name'
  hello(NAME)
  bye(NAME)

if __name__ == '__main__':
  main()

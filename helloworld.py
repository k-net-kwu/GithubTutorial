# -*- coding: utf-8 -*-

def hello(name : str) -> None:
  print(f'hello {name}!')
  
  
def main(): 
  NAME = 'Your name'
  hello(NAME)
  
if __name__ == '__main__':
  main()

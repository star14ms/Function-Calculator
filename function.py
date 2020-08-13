from functions import *

def fx(list):
  if isTrue_rational_num_list(list) == False: # 유리수가 아니면 초기화
    return None
  coefficients = Change_strs_fractions(list) # 유리수면 분수꼴로 변환
  coefficients.reverse() # 오름차순으로 (계산, 출력 편의)
  return coefficients

def f(x, coefficients): ### x, Coefficients : rational-num ###
  y = 0
  for n in range(len(coefficients)):
    if n == 0:
      y += coefficients[0]
    else:
      y += coefficients[n]*x**n  
  return y


# 사용법 익히기

print('ㅡ' * 20)
print('1. define f(x):') 
print("Type 'fx' or 'f(x)' and type coefficients\nfor each Coefficients in descending order\n")
# 1. f(x) 정의: 'f(x)'를 치고, 각 항의 계수를 내림차순으로 입력해라
print('2. define value of x')
print('Type fx or f(x) with a substitute of\nsome rational-num in x')
print('ex) f1.7, f(1/3)')
# 2. x의 값 정의: x자리에 어떤 유리수를 대입하여 f(x)를 한번 더 쳐라

coefficients = None
while True:
  print('ㅡ' * 20)
  a = input()
  
  if a == 'fx' or a == 'f(x)':
    while True:
      list = input('Coefficients(rational-num): ').split() # Coefficients: 계수
      coefficients = fx(list)
  
      if coefficients == None: 
        print('Error: not rational-num!'); continue # 유리수가 아닌 원소가 있었으면 다시
      else: break

    expression = Change_human_tailored_expression(coefficients) # 인간맞춤형 x에 대한 식으로 변환
    print('f(x) =', expression); continue # 식 출력

  if coefficients == None:
    print("Type 'fx' or 'f(x)' first!"); continue
  
  if 'f' in a and a.index('f')==0:
    if 'f(' in a and ')' in a and a.index('f(')==0 and a.index(')')==len(a)-1:
      x = a.replace('f(','').replace(')','')
    else: 
      x = a.replace('f','')
  
    if isTrue_rational_num(x) == False: # 유리수가 아니면 다시
      print('Error: not rational-num!'); continue
    x = Change_str_fraction(x) # 유리수면 분수꼴로 변환

    print('f(x) =', expression); # 식 출력
    
    print('f({}) ='.format(Change_to_decimal(x)), Change_to_decimal(f(x, coefficients))) # 값 계산하여 출력
  else: print("Type f{num}, or f({num})!"); continue

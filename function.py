from functions import *

def f(x): # x의 값이 먼저 정의되어 인자로 받을 수 있어야 함
  print('ㅡ' * 16)
  alpha = 'abcdefghijklmnopqrstuvwxyz' # 25차식까지 지원 (a, b, c : ax^2 + bx + c)

  print('Type the coefficients for each term in descending order') # (각 항의 계수를 내림차순으로 입력해라)
  terms = input('Coefficients : ').split() # (Coefficients: 계수)
  if isTrue_rational_num_list(terms) == False: # 유리수가 아니면 초기화
    return 'error: Not rational num!'
  terms = Change_strs_fractions(terms) # 유리수면 분수꼴로 변환

  if len(terms) == 1:
    print('f(x) = ', end='')
    y = Change_to_decimal(terms[0]) # 가능하면 분수->소수 전환
    return y # 상수항 뿐일때 답 바로 반환

  for n in range(len(alpha)-len(terms)):
    terms.insert(0, 0) # 나머지 항은 값이 0
  terms.reverse() # 오름차순으로 (계산, 출력 편의)

  print('f(x) = ', end='')
  Print_human_tailored_expansion(terms) # (인간맞춤형 식 출력)

  print('     = ', end='')
  y = 0
  for n in range(len(terms)):
    if n == 0:
      y += terms[0]
    else:
      y += terms[n]*x**n
  y = Change_to_decimal(y)
  return y # 답 계산하여 반환

while True:
  print('ㅡ' * 16)

  x = input('x = ') # x의 값 입력받고, 
  if isTrue_rational_num(x) == False: # 유리수가 아니면 초기화
    print('error: Not rational num!'); continue
  x = Change_str_fraction(x) # 유리수면 분수꼴로 변환

  print(f(x))

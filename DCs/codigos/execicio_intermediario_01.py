saldo = 0 

while True:
 try:
  valor = float(input())

  if valor > 0:
   saldo = saldo + valor
   print("Deposito realizado com sucesso!")
   print("Saldo atual: R$ {:.2f}".format(saldo))
   break
  
  elif valor == 0:
   print("Encerrando o programa...")
   break

  else:
   print("Valor invalido! Digite um valor maior que zero.")

 except EOFError:
  break

def calcule(num1, operator, num2):
   if operator == "+":
     return(num1+num2)
   elif operator =="-":
      return(num1-num2)
   elif operator =="*":
      return(num1*num2)
   elif operator == "/":
      return(num1/num2)
   elif operator =="%":
      return(num1%num2)


resultat=calcule(26,"+",24)
print(resultat)
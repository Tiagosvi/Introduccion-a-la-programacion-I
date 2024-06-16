fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = (fibonacci (n - 2)) + (fibonacci (n - 1))

parteEntera::Float->Int
parteEntera x | x<1 && x>=0 =0
              | x>(-1) && x<=0 = -1
              | x>=1 = 1+parteEntera (x-1)
              | otherwise =(-1)+parteEntera (x+1)


sumaImpares :: Int -> Int 
sumaImpares 0 = 0
sumaImpares a = sumaImpares (a-1) + (a*2 - 1) 


sumaDigitos :: Int -> Int
sumaDigitos x | x == 0 = 0
              | otherwise = (rem x 10) + sumaDigitos (div x 10)



todosDigitosIguales :: Int -> Bool
todosDigitosIguales x |  x < 10 = True
                      | x < 100 = rem x 10 == div x 10 
                      | otherwise = todosDigitosIguales (rem x 100) 










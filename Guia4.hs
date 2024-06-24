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


cantDigitos :: Int -> Int
cantDigitos x | x == 0 = 0
              | otherwise = 1 + cantDigitos(div x 10)

invertirNum :: Int -> Int
invertirNum 0 = 0
invertirNum x = ultimoNum * (10^((cantDigitos x) -1)) + invertirNum(div x 10)
            where ultimoNum = mod x 10


esCapicua :: Int -> Bool
esCapicua x | x < 10 = True
            | otherwise = x == invertirNum x


menorDivisor :: Int -> Int
menorDivisor x | mod x 2 == 0 = 2
               | otherwise = encontrarDivisores x 2

encontrarDivisores :: Int -> Int -> Int
encontrarDivisores x y| mod x y == 0 = y
                      | otherwise = encontrarDivisores x (y+1)


esPrimo :: Int -> Bool
esPrimo x = x == menorDivisor x

mayorDigitoPar :: Int -> Int
mayorDigitoPar 0 = -1
mayorDigitoPar x = mayor (mayorDigitoParAux x)


mayorDigitoParAux :: Int -> [Int]
mayorDigitoParAux 0 = []
mayorDigitoParAux x | esPar(mod x 10) = mod x 10: mayorDigitoParAux (div x 10)
                    | otherwise = mayorDigitoParAux (div x 10)


mayor :: [Int] -> Int
mayor [y] = y
mayor (x:y:xs) | x > y = mayor (x:xs)
               | otherwise = mayor (y:xs)

esPar :: Int -> Bool
esPar x = mod x 2 == 0 








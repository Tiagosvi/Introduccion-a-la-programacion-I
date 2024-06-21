--Ejercicio:
porcentajeDeVotosAfirmativos :: [(String,String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos [] [] 0 = 0
porcentajeDeVotosAfirmativos (x:xs) (y:ys) n = division ((sumatoriaVotos (y:ys)) * 100) (n) 

sumatoriaVotos :: [Int] -> Int
sumatoriaVotos [] = 0
sumatoriaVotos (x:xs) = x + sumatoriaVotos xs

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

--Ejercicio 2:
formulasInvalidas :: [(String,String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((x,y):xs) | x == y = True
                             | pertenece x xs = True 
                             | pertenece y xs = True
                             | otherwise = formulasInvalidas xs


pertenece :: String -> [(String,String)] -> Bool
pertenece p [] = False
pertenece p ((x,y):xs) | p == x = True
                       | p == y = True
                       | otherwise = pertenece p xs


-- Ejercicio 3:
porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos p [] [] = 0
porcentajeDeVotos p (x:xs) (y:ys) = division ((unVice p (x:xs) (y:ys)) * 100) (sumatoriaVotos (y:ys))


unVice :: String -> [(String,String)] -> [Int] -> Int
unVice p [] [] = 0
unVice p ((x,y):xs) (z:zs) | p == y = z + unVice p xs zs
                           | otherwise = unVice p xs zs

-- Ejercicio 4:

menosVotado :: [(String,String)] -> [Int] -> String
menosVotado [] [] = ""
menosVotado ((x,y):(b,c):xs) (z:a:zs) | longitud (z:a:zs) == 2 && z >= a = b
                            | longitud (z:a:zs) == 2 && z < a = x
                            | z > a = menosVotado ((x,y):(b,c):xs) (a:zs)
                            | otherwise = menosVotado ((x,y):(b,c):xs) (z:zs)

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
--Ejercicio:
divisoresPropios :: Int -> [Int]
divisoresPropios 0 = []
divisoresPropios n = encontrarDivisores n 1


encontrarDivisores :: Int -> Int -> [Int]
encontrarDivisores x y | x == y = (y:[])
                       | mod x y == 0 = y: encontrarDivisores x (y+1)
                       | otherwise = encontrarDivisores x (y+1)

--Ejercicio 2:
sonAmigos :: Int -> Int -> Bool
sonAmigos n m = sumatoria (divisoresPropios n) - n == m

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


-- Ejercicio 3:
losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = buscoPerfectos n 1


esPerfecto :: Int -> Bool
esPerfecto n = sumatoria(divisoresPropios n) - n == n  


buscoPerfectos :: Int -> Int -> [Int]
buscoPerfectos 0 _ = []
buscoPerfectos x y | esPerfecto y = y: buscoPerfectos (x-1) (y+1) 
                   | otherwise = buscoPerfectos x (y+1) 


listaDeAmigos :: [Int] -> [(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos (x:xs) | listaDeAmigosAux x xs /= (0,0) = listaDeAmigosAux x xs: listaDeAmigos xs
                     | otherwise = listaDeAmigos xs

listaDeAmigosAux :: Int -> [Int] -> (Int,Int)
listaDeAmigosAux _ [] = (0,0)
listaDeAmigosAux n (x:xs) | sonAmigos n x = (n,x)
                          | otherwise = listaDeAmigosAux n xs
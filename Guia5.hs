-- Ejercicio 1:

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [Int] -> Int
ultimo [] = 0
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | otherwise = ultimo xs


principio :: [Int] -> [Int]
principio [] = []
principio (x:xs) | longitud (x:xs) == 2 = x:[]
                 | otherwise = x: principio xs


reverso :: [Int] -> [Int]
reverso [] = []
reverso (x:xs) |  longitud xs == 0 = x:[]
               |  otherwise =  (reverso xs) ++ (x:[])


-- Ejercicio 2:

pertenece :: Int -> [Int] -> Bool
pertenece n [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

todosIguales :: [Int] -> Bool
todosIguales [] = False
todosIguales (x:xs) | longitud (x:xs) == 1 = True
                    | otherwise = pertenece x xs && todosIguales xs

todosDistintos :: [Int] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

hayRepetidos :: [Int] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs


quitar :: Int -> [Int] -> [Int]
quitar n [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = quitar n xs ++ [x]

quitarTodos :: Int -> [Int] -> [Int]
quitarTodos n [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = quitar n xs ++ [x]

               
eliminarRepetidos :: [Int] -> [Int]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs
                         | otherwise = eliminarRepetidos xs  ++ [x]

mismosElementos :: [Int] -> [Int] -> Bool
mismosElementos [] [] = True
mismosElementos _ [] = True
mismosElementos [] _ = False
mismosElementos (x:xs) (y:ys) | not(pertenece x (y:ys)) = False
                              | otherwise = mismosElementos xs (y:ys)

capicua :: [Int] -> Bool
capicua [] = False
capicua (x:xs) = reverso (x:xs) == (x:xs)


-- Ejercicio 3:

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x < y = maximo (y:xs)
                | otherwise = maximo (x:xs)

sumarN :: Int -> [Int] -> [Int]
sumarN n [] = []
sumarN n (x:xs) = (x+n): sumarN n xs

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

ult :: [Int] -> Int
ult [x] = x
ult (x:xs) = ult xs

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ult (x:xs)) (x:xs)

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x: pares xs
             | otherwise = pares xs

multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x: multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

ordenar :: [Int] -> [Int]
ordenar [] = []
--ordenar (x:xs) | maximo (x:xs) NO ME SALEE!!!

-- Ejercicio 4:

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [y] = y:[]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == ' ' = ' ': sacarBlancosRepetidos xs
                               | otherwise = x: sacarBlancosRepetidos (y:xs)

contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras [x] = 1
contarPalabras (x:xs) | x == ' ' =  1 + contarPalabras (xs)
                      | otherwise = contarPalabras xs



palabras :: [Char] -> [[Char]]
palabras [] = []
palabras ls = palabrasAux ls []

palabrasAux :: [Char] -> [Char] -> [[Char]]
palabrasAux [] palabra = [palabra]
palabrasAux (x:xs) palabra | x /= ' ' = palabrasAux xs (palabra ++[x])
                          | otherwise = [palabra]++ (palabrasAux xs [])


--palabraMasLarga :: [Char] -> Int
--palabraMasLarga [] = 0
--palabraMasLarga (x:xs) = contarPalabras (palabras (x:xs)) NO ME SALE!!!

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs

aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [] n = []
aplanarConNBlancos (x:xs) n = x ++ (blancosN " " n) ++ aplanarConNBlancos xs n

blancosN :: [Char] -> Int -> [Char]
blancosN [] n = []
blancosN (x:xs) n | 0 >= n = " "
                  | otherwise = (x:xs) ++ blancosN (x:xs) (n-1)


-- Ejercicio 5:

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


ultimo :: [Int] -> Int
ultimo [] = 0
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | otherwise = ultimo xs


reverso :: [Int] -> [Int]
reverso [] = []
reverso (x:xs) | longitud xs == 0 = x:[]
               | otherwise = reverso xs ++ x:[]


pertenece :: Int -> [Int] -> Bool
pertenece a [] = False
pertenece a (x:xs) | a == x = True
                   | otherwise = pertenece a xs



todosDistintos :: [Int] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs


quitar :: Int -> [Int] -> [Int]
quitar n [] = []
quitar n (x:xs) | n == x = quitar n xs
                | otherwise = x: quitar n xs


eliminarRepetidos :: [Int] -> [Int]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = eliminarRepetidos xs
                         | otherwise = x: eliminarRepetidos xs 


mismosElementos :: [Int] -> [Int] -> Bool
mismosElementos [] _ = True
mismosElementos (x:xs) (y:ys) | not(pertenece x (y:ys)) = False
                              | otherwise = mismosElementos xs (y:ys)


capicua :: [Int] -> Bool
capicua [] = False
capicua (x:xs) = reverso (x:xs) == (x:xs)


sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs


maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)


sumarN :: Int -> [Int] -> [Int]
sumarN n [] = []
sumarN n (x:xs) = (x + n): sumarN n xs

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarElPrimero(reverso (x:xs))


pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x: pares xs
             | otherwise = pares xs


multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x: multiplosDeN n xs
                      | otherwise = multiplosDeN n xs



sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == ' ' = ' ': sacarBlancosRepetidos xs
                               | otherwise = x: sacarBlancosRepetidos (y:xs)

contarPalabras :: [Char] -> Int
contarPalabras (x:xs) = contarPalabrasAux(sacarBlancosRepetidos (x:xs))

contarPalabrasAux :: [Char] -> Int
contarPalabrasAux [] = 0
contarPalabrasAux [x] = 1
contarPalabrasAux (x:xs) | x == ' ' = 1 + contarPalabrasAux xs
                         | otherwise = contarPalabrasAux xs


palabras :: [Char] -> [[Char]]
palabras [] = []
palabras ls = palabrasAux ls []

palabrasAux :: [Char] -> [Char] -> [[Char]]
palabrasAux [] palabra = [palabra]
palabrasAux (x:xs) palabra | x /= ' ' = palabrasAux xs (palabra ++[x])
                           | otherwise = [palabra]++ (palabrasAux xs [])



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





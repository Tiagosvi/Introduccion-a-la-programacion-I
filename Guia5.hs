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



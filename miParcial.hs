-- Ejercicio:

hayQueCodificar :: Char -> [(Char,Char)] -> Bool
hayQueCodificar c [] = False
hayQueCodificar c ((x,y):xs) | c == x = True
                             | otherwise = hayQueCodificar c xs

--Ejercicio 2:
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char,Char)] -> Int
cuantasVecesHayQueCodificar c (x:xs) (z:zs) | not(hayQueCodificar c (z:zs)) = 0
                                            | otherwise = aparece c (x:xs)

aparece :: Char -> [Char] -> Int
aparece c [] = 0
aparece c (x:xs) | c == x = 1 + aparece c xs
                 | otherwise = aparece c xs

--Ejercicio 3:

laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
laQueMasHayQueCodificar [] [] = 'd'
laQueMasHayQueCodificar (x:z:xs) (y:ys) | longitud (x:z:xs) == 2 &&  contador x  (y:ys) >= contador z (y:ys) = x
                                        | longitud (x:z:xs) == 2 &&  contador x  (y:ys) <  contador z (y:ys) = z
                                        | contador x  (y:ys) >= contador z (y:ys) = laQueMasHayQueCodificar (x:xs) (y:ys)
                                        | otherwise = laQueMasHayQueCodificar (z:xs) (y:ys)

contador :: Char -> [(Char,Char)] -> Int
contador c [] = 0
contador c ((x,y):xs) | c == x = 1 + contador c xs
                      | otherwise = contador c xs

longitud :: [Char] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--Ejercicio 4:

codificarFrase :: [Char] -> [(Char,Char)] -> [Char]
codificarFrase [] _ = []
codificarFrase (x:xs) ((z,y):zs) | not(hayQueCodificar x ((z,y):zs)) = x: codificarFrase xs ((z,y):zs)
                                 | otherwise = codificarFraseAux x ((z,y):zs) : codificarFrase xs ((z,y):zs)

codificarFraseAux :: Char -> [(Char,Char)] -> Char
codificarFraseAux c [] = 'a'
codificarFraseAux c ((x,y):xs) | c /= x = codificarFraseAux c xs
                               | otherwise = y




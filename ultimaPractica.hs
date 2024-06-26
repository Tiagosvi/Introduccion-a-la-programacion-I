--Ejercicio:
aproboMasDeNMaterias :: [(String,[Int])] -> String -> Int -> Bool
aproboMasDeNMaterias (x:xs) a n = cuantasAprobo (encontrarAlumno (x:xs) a) >=  n

encontrarAlumno :: [(String,[Int])] -> String -> [Int]
encontrarAlumno [] a = []
encontrarAlumno ((x,y):xs) a | x == a = y
                             | otherwise = encontrarAlumno xs a


cuantasAprobo :: [Int] -> Int
cuantasAprobo [] = 0
cuantasAprobo (x:xs) | x >= 4 = 1 + cuantasAprobo xs
                     | otherwise = cuantasAprobo xs

--Ejercicio 2:
buenosAlumnos :: [(String,[Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((x,y):xs) | buenAlumno y = x: buenosAlumnos xs
                        | otherwise = buenosAlumnos xs

buenAlumno :: [Int] -> Bool
buenAlumno (x:xs) = promedio (x:xs) > 8 && aprobadas (x:xs)

aprobadas :: [Int] -> Bool
aprobadas [] = True
aprobadas (x:xs) | x < 4 = False
                 | otherwise = aprobadas xs

promedio :: [Int] -> Float
promedio (x:xs) = division (sumatoria (x:xs)) (longitud (x:xs)) 

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

division:: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


--Ejercicio 3:
mejorPromedio :: [(String, [Int])] -> [String]
mejorPromedio [(x,y)] = [x]
mejorPromedio ((x,y):(a,b):xs) | promedio y > promedio b = mejorPromedio ((x,y):xs)
                               | otherwise = mejorPromedio ((a,b):xs)


type Tablero = [[Int]]

masRepetido :: Tablero -> Int
masRepetido (x:y:xs) | longitudT (x:y:xs)  == 2 && masAparecidoLista x (x:y:xs) >= masAparecidoLista y (x:y:xs) = masAparecidoLista x (x:y:xs)
                     | longitudT (x:y:xs) == 2 && masAparecidoLista x (x:y:xs) < masAparecidoLista y (x:y:xs) = masAparecidoLista y (x:y:xs)
                     | masAparecidoLista x (x:y:xs) >= masAparecidoLista y (x:y:xs) = masRepetido (x:xs)
                     | otherwise = masRepetido (y:xs)


masAparecidoLista :: [Int] -> Tablero -> Int
masAparecidoLista [x]_ = x
masAparecidoLista (x:y:xs) t | sumaApariciones x t > sumaApariciones y t = masAparecidoLista (x:xs) t
                             | otherwise = masAparecidoLista (y:xs) t

apariciones :: Int -> [Int] -> Int
apariciones n [] = 0
apariciones n (x:xs) | n /= x = apariciones n xs
                        | otherwise = 1 + apariciones n xs


sumaApariciones :: Int -> Tablero -> Int
sumaApariciones n [] = 0
sumaApariciones n (x:xs) = apariciones n x + sumaApariciones n xs

longitudT :: Tablero -> Int
longitudT [] = 0
longitudT (x:xs) = 1 + longitudT xs
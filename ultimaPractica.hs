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


--Ejercicio 4:
seGraduoConHonores :: [(String, [Int])]
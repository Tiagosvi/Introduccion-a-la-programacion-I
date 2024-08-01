problemaFinal :: [Int] -> [Int] -> [Int]
problemaFinal [] _ = []
problemaFinal (a:as) (b:bs) = buscarMayor(buscarPosicion (a+1)  (b:bs)) : problemaFinal as (b:bs) 

buscarPosicion :: Int -> [Int] -> [Int]
buscarPosicion 0 _ = []
buscarPosicion a [] = []
buscarPosicion a (x:xs) = x: buscarPosicion (a-1) xs

buscarMayor :: [Int] -> Int
buscarMayor [x] = x
buscarMayor (x:y:xs) | x > y = buscarMayor (x:xs)
                     | otherwise = buscarMayor (y:xs)
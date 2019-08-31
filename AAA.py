dog = "When Mr. Bilbo Baggins of Bag End announced"

let1 = dog.count('a')
let2 = dog.count('e')
let3 = dog.count('i')
let4 = dog.count('o')

l1 = dog[let1-1:let1]
l2 = dog[let2-1:let2]
l3 = dog[let3-1:let3]
l4 = dog[let4-1:let4]
pasword = l1+l2+l3+l4
print(pasword)
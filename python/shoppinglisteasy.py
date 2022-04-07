########
#link https://open.kattis.com/problems/shoppinglisteasy
########



shoppinglists, items = map(int, input().split())



first_shoplist_uniq = set(input().split())


common = first_shoplist_uniq

for i in range(shoppinglists-1):

	second_shoplist_uniq = set(input().split())

	common = common & second_shoplist_uniq

	#common = first_shoplist_uniq & second_shoplist_uniq

	#print(common)


print(len(common))
for elm in list(sorted(common)):
	print(elm)










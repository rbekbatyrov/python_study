#exercise 3.4
#create bicycle
spisok_gostei=[1, 2, 3, 4, 5, 6, 7]
print(spisok_gostei)
print('---')

#form a letter for our friend
privetstvie=f'Hello {spisok_gostei[3]}. I want to invite you to my programm!!!'
print(privetstvie)
print('---')

#exercise 3.5
#form new letter for new guest
zamenenyi_gost=(spisok_gostei[4])
print('Etot gost ne prided', zamenenyi_gost)
spisok_gostei[4]=8
print('pridet', spisok_gostei[4], 'vmesto', zamenenyi_gost)
print('Itogo, vot te kotorye pridut', spisok_gostei)
privetstvie=f"Hello {spisok_gostei[4]}. I want to invite you to my programm!!!"
print(privetstvie)
print('---')

#exercise 3.6
#dobavlyaem eshe treh gostei
spisok_gostei.insert(0, 9)
spisok_gostei.insert(3, 10)
spisok_gostei.append(11)
print('vot eshe troe')
print('Itogo, vot te kotorye pridut', spisok_gostei)
print('---')

#exercise 3.7
#sokrashenie_1
print('K bolshomu sozhaleniu, v restoran budut priglasheni tolko dva gostya')
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
refusing_message=f'Uvazhaemyi {spisok_gostei.pop()}, Vashe priglashenie otozvano'
print(refusing_message)
podtverzhdenie=f'Uvazhaemyi {spisok_gostei[0]}, Vashe priglashenie podtverzhdeno'
print(podtverzhdenie)
podtverzhdenie=f'Uvazhaemyi {spisok_gostei[1]}, Vashe priglashenie podtverzhdeno'
print(podtverzhdenie)
print('---')

#ochistka
print(spisok_gostei)
del spisok_gostei[0]
del spisok_gostei[0]
print(spisok_gostei)

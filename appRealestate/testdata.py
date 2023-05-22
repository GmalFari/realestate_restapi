# IndexError: list index out of range
# >>> for i in jsonData['hits']:
# ...     newData = Property.objects.create(property_title=i['title_l1'])
# ...     with open(f'/home/homepage/testDir/{images[random.randint(0,len(images)-1)]}', 'rb') as f:
# ...             image = File(f)
# ...             newData.coverPhoto.save(f'{i["id"]}',image)
# ...     newData.save()
# ... 
# >>> for i in jsonData['hits']:
# ...     newData = Property.objects.create(property_title=i['title_l1'])
# ...     with open(f'/home/homepage/testDir/{images[random.randint(0,len(images)-1)]}', 'rb') as f:
# ...             image = File(f)
# ...             newData.coverPhoto.save(f'{i["id"]}.jpeg',image)
# ...     newData.save()
# ... 
# >>> A

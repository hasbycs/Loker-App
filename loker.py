def testing(loker):
    floor = 1
    nine = True
    three = False
    seven = False
    two = False
    array = []
    if loker.isdigit():
      for i in range(1,int(loker)+1):
        array.append(i)
        if int(loker) == i:
            return 'loker ' + str(loker) + ' terdapat di lantai ' + str(floor)
        elif nine and len(array)==9:
          floor+=1
          nine = False
          three = True
          array = []
        elif three and len(array)==3:
          floor+=1
          three = False
          seven = True
          array = []
        elif seven and len(array)==7:
          floor+=1
          seven = False
          two = True
          array = []
        elif two and len(array)==2:
          floor+=1
          two = False
          nine = True
          array = []
      return 'loker tidak ditemukan'
    else:
        return 'masukkan nomor loker'


flag=False
while(not flag):
  print('masukkan nomor loker : ')
  x = input()
  print(testing(x))
def bubble_sort(text):

    try:
        assert type(text) is str
    except:
        raise TypeError("Text is not string.")


    text_list = text.split(' ')
    n = len(text_list)
    count = 0

    for i in range(n):

        for j in range (0, n - i - 1):

            if len(text_list[j]) > len(text_list[j+1]):  #判斷當前名字長度是否大於下一個名字

                count += 1
                print ("第%d次"%count)
                print ("交換前：%s"%text_list)

                text_list[j], text_list[j+1] = text_list[j+1], text_list[j] #如果當前名字長度大過下一個，交換兩個名字位置

                print ("交換後：%s \n"%text_list,)

            elif len(text_list[j]) == len(text_list[j+1]):  #判斷當前名字與下一個名字長度是否一樣

                if ord(text_list[j][0]) > ord(text_list[j+1][0]): #判斷當前名字與下一個名字首字母大小

                    count += 1
                    print("第%d次"%count)
                    print ("交換前：%s"%text_list)

                    text_list[j], text_list[j + 1] = text_list[j + 1], text_list[j] #如果首字母比下一個名字首字母大，交換兩個名字位置

                    print ("交換後：%s \n"%text_list)

    print ("排序次數：%d"%count)
    print ("排序結果：%s"%text_list)

    return text_list

text = "Peter Lawrence Isabella Ryan Oliver Ada Benjamin Pauline"

result = bubble_sort(text)
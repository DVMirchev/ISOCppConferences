with open("isocppconferences.txt") as wiki_page:
    wiki_text = wiki_page.read()

    count = -1
    index = 0

    while count != 0:

        index += 1
        count = wiki_text.count('[{}]'.format(index))

        if count == 1:
           print('[{}] is found once'.format(index))
#        else:
#           print('[{}] is found {} times'.format(index, count))


    print('The biggest index is [{}]'.format(index - 1))




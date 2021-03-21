def select_titles(dictionary, genre):
    list_of_titles = []   
    for key, value in dictionary.items():
        if value == genre:
            list_of_titles.append(key)
    return  list_of_titles        

def rate_avg(dictionary, titles):
    list_of_rate = []
     
    for key, value in dictionary.items():
        if key in titles:
            list_of_rate.append(value)
    avg = round((sum(list_of_rate) / len(titles)), 3)
    return 'Средний рейтинг жанров: ' + str(avg)

if __name__ == "__main__":
    cross()
    select_titles()
    rate_avg()
    stata()
    cicle()



    








        









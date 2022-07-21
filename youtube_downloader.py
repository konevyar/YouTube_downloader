from pytube import YouTube

# Запрос у пользователя места для сохранения видео
save_path = input("Where do you want to save video? (Exapmle: C:/Users/Username/Downloads)\n")

while True:
    # Запрос у пользователя ссылки на видео
    video_link = input("Enter link to video you want to download: \n")

    # Попытка найти видео по полученной ссылке
    try:
        get_video = YouTube(video_link)
    except:
        print("Connection error.")
        
    # Получение видео с максимальным разрешением
    video = get_video.streams.get_highest_resolution()

    # Попытка скачать видео
    print('Dowloading...')
    try:
        video.download(save_path)
    except:
        print("Some Error!")

    print('Task Completed!')

    repeat = input('Dou want to download another video? (y/n)\n')
    if repeat == 'y':
        continue
    elif repeat =='n':
        break
    elif repeat != 'y' and repeat != 'n':
        print(repeat)
        continue

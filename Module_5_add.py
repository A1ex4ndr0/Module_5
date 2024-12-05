from time import sleep

class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title: str, duration, time_now = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title

class UrTube:

    def __init__(self, users = None, videos = None, current_user = None):
        users = []
        videos = []
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if i == self.nickname and i == self.password:
                self.current_user = i

    def register(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        Flag = True

        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                Flag = False

        if Flag:
            new_user = User(self.nickname, self.password, self.age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i in self.videos:
                continue
            else:
                self.videos.append(i)

    def get_videos(self, word):
        listvideos = []
        for i in self.videos:
            if word.upper() in i.title.upper():
                listvideos.append(i.title)
        return listvideos

    def watch_video(self, name):
        if self.current_user:
            for i in self.videos:
                if name == i.title:
                    if i.adult_mode and self.age >= 18:
                        for j in range(1, i.duration+1):
                            print(j, end=' ')
                            sleep(1)
                        print("Конец видео")
                        i.duration = 0
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
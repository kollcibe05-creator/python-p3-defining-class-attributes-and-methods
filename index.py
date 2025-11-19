# class Album:
#     all = []
#     album_count = 0
#     GENRES = ["Pop", "RnB", "Zouk", "Rap"]
#     def __init__(self,genre, date):
#         if self.confirm_genre(genre):
#             self.release_date = date
#             self.genre = genre
#             self.increase_album_count()
#         else: 
#             raise ValueError("Please, let's make each other's life easy!!")    
        
#     @classmethod
#     def increase_album_count(cls, increment = 1):
#         cls.album_count += increment
#     @classmethod
#     def confirm_genre(cls, genre):
#         return genre in cls.GENRES





# damn = Album("Zouk",2018)  
# GKMC = Album("Pop",2016)
# section80 = Album("Amapiano",2013)

# # print(damn.genre)
# # print(section80.genre)


class Song:
    all = []
    def __init__(self, name):
        self.name = name
        Song.add_name_to_all(self)
    @classmethod
    def add_name_to_all(cls, name):
        cls.all.append(name)

    @classmethod
    def show_song_names(cls):
        return([song.name for song in cls.all])        


thriller = Song('thriller')
GKMC = Song("Good Kid Maad City")
euphoria = Song("Euphoria")

print(thriller.show_song_names())
print(GKMC.show_song_names())






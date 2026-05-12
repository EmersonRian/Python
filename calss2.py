class Canal:
    def __init__(self,nome,inscritos,descricao):
        self.nome = nome
        self.inscritos = inscritos
        self.descricao = descricao
        self.videos = []
        self.list_playlist = []

    
    def inscreverse(self,quantidade=1):
        self.inscritos += quantidade

    def un_follow(self,quantidade=1):
        if self.inscritos == 0:
            return
        self.desisncrever -= quantidade
    
    def up_video(self,video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print("Video ja esta postado")
    
    def info_canal(self):
        print(
f"""Canal: {self.nome}
Numero de Incritos : {self.inscritos}
Descriçao: {self.descricao}
{len(self.videos)} Videos Postados."""
)
        
    def adicionar_playlist(self,playlist):
        if playlist not in self.list_playlist:
            self.list_playlist.append(playlist)
        else:
            print("Essa playlist ja foi adicionada")

    def info_playlists(self):
        for i in self.list_playlist:
            print(i.info())
        


class Video:
    def __init__(self,nome,descricao):
        self.nome = nome
        self.descrocao = descricao

        self.likes = 0
        self.deslikes = 0
        self.visualizacao = 0

        self.comentarios = []

    # def __repr__(self):
    #     return self.nome

    def like(self):
        self.likes += 1
    def deslike(self):
        self.deslikes += 1

    def vizualizacao(self):
        self.visualizacao += 1
 
    def comentar(self,comenta):
        self.comentarios.append(comenta)

    
    def info_video(self):
        print(
f"""Vidio: {self.nome}
Descriçao: {self.descrocao}
Likes: {self.likes}  Deslikes: {self.deslikes}
Comentario : {self.comentarios}""")


class Playlist:
    def __init__(self,nome):
        self.nome = nome
        self.videos = []

    def adicionar_video(self,video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print("Este vidio ja esta na playlist")
    
    def info(self):
        print(f"Playlist: {self.nome}\n")
        for i in self.videos:
            print(f"{i.info_video()}\n")

        
luan = Canal("Luan_games",100,"Luan Jogando jogos")

vidio_1 = Video("jogando mine","Luan jogando mine")
vidio_2 = Video("jogando stardew","Luan jogando stardew")
vidio_3 = Video("Fazendo Receitas","Cozinhando")
vidio_4 = Video("Fazendo Receitas","Cozinhando")

playlist_1 = Playlist("Games")
playlist_2 = Playlist("Comer")


luan.up_video(vidio_1)
luan.up_video(vidio_2)
luan.up_video(vidio_3)
luan.up_video(vidio_4)

playlist_2.adicionar_video(vidio_3)
playlist_2.adicionar_video(vidio_4)
playlist_1.adicionar_video(vidio_1)
playlist_1.adicionar_video(vidio_2)

luan.adicionar_playlist(playlist_1)
luan.adicionar_playlist(playlist_2)

# vidio_1.info_video()
# luan.info_canal()
# playlist_1.info()

luan.info_playlists()
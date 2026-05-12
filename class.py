class Canal:
    def __init__(self,nome,inscritos,descricao):
        self.nome = nome
        self.inscritos = inscritos
        self.descricao = descricao
        self.videos = []
        self.listar_playlists = []
    
    def inscreverse(self,quantida=1):
        self.inscritos += quantida

    def un_follow(self,quantidade=1):
        if self.inscritos == 0:
            return
        self.desisncrever -= quantidade
    
    def up_video(self,video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print("Video ja esta postado")
    
    def add_playlist(self,playlist,videos):
        self.listar_playlists.append([playlist,videos])

    def info_playlist(self):
        for i in self.listar_playlists:
            print(i)
            print()
            
            

class Videos:
    def __init__(self,nome,descriçao):
        self.nome = nome
        self.descriçao = descriçao

        self.visualizacao = 0
        self.comentario = []
        self.likes = 0
        self.deslikes = 0
        self.data_publicaçao = []

    def __repr__(self):
        return self.nome
    
    def visualizar(self):
        self.visualizacao += 1
    
    def deixar_like(self):
        self.likes += 1

    def deixar_deslike(self):
        self.deslikes += 1
    
    def comentar(self,comentar):
        self.comentario.append(comentar)
    
    def data(self,data):
        self.data_publicaçao.append(data)

    def info(self):
        print(f"""
Titulo: {self.nome}
Descrição: {self.descriçao}
Data de Lançamento: {self.data_publicaçao}
Visualização: {self.visualizacao}
Likes: {self.likes}
DesLikes: {self.deslikes}""")



class Playlist:
    def __init__(self,nome):
        self.nome = nome

        self.videos = []
    
    def __repr__(self):
        return self.nome

    def adicionar_videos(self,video):
        self.videos.append(video)

    def info_playlist(self):
        print(f"Playlist: {self.nome}")
        for i in self.videos:
            i.info()



luan_games = Canal("Luan_games",300,"Jogar jogos")
zuando_nos_games = Videos("Zuando_nos_games","Torrando dinheiro aleios")
zuando_nos_games.data("30/03/2026")
games = Videos("nome","descriçao")

luan_games.up_video(zuando_nos_games)
luan_games.up_video(games)

play = Playlist("Poker")
play.adicionar_videos(zuando_nos_games)
play.adicionar_videos(games)
# play.info_playlist()

luan_games.add_playlist(play,play.videos)
luan_games.info_playlist()

play.info_playlist()





















# class CanalEmpresarial(Canal):
#     def __init__(self,nome,inscritos,descricao):
#         super().__init__(nome,inscritos,descricao)
#         self._comer = []
    
#     @property
#     def equipe(self):
#         return self._comer
    
#     def adicionar_membro(self,caba):
#         if caba not in self._comer:
#             self._comer.append(caba)
#             print(f"Menbro {caba} foi adicionado")
#         else:
#             print(f"O Menbro {caba} Ja esta na lista")
    
#     def remover_menbro_equipe(self,caba):
#         if caba in self._comer:
#             self._comer.remove(caba)
#             print(f"{caba} foi removido da equipe")
#         else:
#             print("Esse menbro nao existe")



# canal_1 = Canal("games",500,"muui legal")
# canal_empresarios = CanalEmpresarial("Empresa","50000","empresa aqui")

# # print(f"O canal {canal_1.nome} tem {canal_1.inscritos} Inscritos. Sua descriçao é {canal_1.descricao}")

# # canal_1.inscreverse()

# # print(f"Quantidade de inscritos {canal_1.inscritos}")

# print(f"O canal {canal_empresarios.nome} tem {canal_empresarios.inscritos} Inscritos. Sua descriçao é {canal_empresarios.descricao}")





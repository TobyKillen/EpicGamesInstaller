import time
import os
import dis


class EpicFileManager:
    global list_of_games
    list_of_games = []

    global tempoary_file_ext
    tempoary_file_ext = "_temp"



    def __init__(self) -> None:
        folder_path = "E:\Epic"
        EpicFileManager.detectExistingGames(folder_path)
        # for full_game_path in list_of_games:
        #     EpicFileManager.tempRenameGame(full_game_path)
        
        for full_game_path in list_of_games:
            EpicFileManager.correctlyRenameGame(full_game_path)

        

    
    def tempRenameGame(full_game_path):
        new_file_name = full_game_path + tempoary_file_ext
        os.rename(full_game_path, new_file_name)
        return

    def correctlyRenameGame(full_game_path):
        print(full_game_path)
        new_file_name = full_game_path.strip(tempoary_file_ext)
        os.rename(full_game_path, new_file_name)
        return


    def detectExistingGames(folder_path):
        game_dir = os.listdir(folder_path)
        for game in game_dir:
            full_game_path = str(folder_path + '\\' + game )
            list_of_games.append(full_game_path)
        return






if __name__ == "__main__":
    EpicFileManager()
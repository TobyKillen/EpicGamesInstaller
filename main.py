import time
import os
import dis
import argparse
import sys


# os.system("cls")
# print('''                                                                   
#          #&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&*       
#         %&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%%      
#        %%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&#     
#        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#     
#        &%&&&%&&&%          %%#         *%&&&     %&&%/        #&%&&&%&&&%&#     
#        &%&%&%&%&%          %%#            %&     &%#            %&%&%&%&%&#     
#        &%&&&%&&&%     &&%&&&%#    &&%&    %&     &&     %&&&    ,&&&%&&&%&#     
#        %%%%%%%%%%     %%%%%%%#    %%%%    %%     %%     %%%%    ,%%%%%%%%%#     
#        &%&&&%&&&%     &&%&&&%#    &&%&    %&     &&     %&&&    ,&&&%&&&%&#     
#        &%&%&%&%&%          &%#    %&%&    %&     &%     %&%&%&%&%&%&%&%&%&#     
#        &%&&&%&&&%          &%#            &&     &&     %&&&%&&&%&&&%&&&%&#     
#        %%%%%%%%%%     %%%%%%%#          ,%%%     %%     %%%%    .%%%%%%%%%#     
#        &%&&&%&&&%     &&%&&&%#    &&%&&&%&&&     &&     %&&&    .&&&%&&&%&#     
#        &%&%&%&%&%     %&%&%&%#    %&%&%&%&%&     &%     %&%&    .&%&%&%&%&#     
#        &%&&&%&&&%     &&%&&&%#    &&%&&&%&&&     &&     &&&%    .&&&%&&&%&#     
#        %%%%%%%%%%          #%#    %%%%%%%%%%     %%&            %%%%%%%%%%#     
#        &%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&&&&&%&&&%&&&%&#     
#        &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&#     
#        &%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&#     
#        %%%%%%%%%%&&      %%%%%   %%%%%   %%&   %%       %&      %%%%%%%%%%#     
#        &%&&&%&&&%   &&&&&&&&&  /  %&%%    (    &%  %%%%%%/   %&&%&&&%&&&%&#     
#        &%&%&%&%&%   &&%(  %&       %%%  %, #%  &%  %%&%&%&&&%#   &%&%&%&%&#     
#        &%&&&%&&&%&&      &&  *&&%&  #%  &&&&%  &%       %%      &&&&%&&&%&#     
#        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#     
#        &%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&(     
#         &&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&      
#            %%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&&&%&#         
#                  &%%&%%%%%%%%%&                   .&&%%%%%%%%%%%%               
#                        &%&&&%&&&%&&&%&*    %%&&&%&&&%&&&%%%                     
#                              %%&%&%&%&%&%&%&%&%&%&&&%                           
#                                    %%&&&%&&&%&%
# ''')



# Find all the games in Dir
# Write paths to temp array
# Rename Folders
# Await for EGS to load in folders
# Delete the newly created folders
# Rename the game folders back to the orgional 


class EGSFileManager:
    global list_of_games
    list_of_games = []

    global list_of_temp_folders
    list_of_temp_folders = []

    global tempoary_file_ext
    tempoary_file_ext = "_temp"



    def __init__(self) -> None:
        folder_path = "E:\EpicTemp"
        EGSFileManager.detectExistingGames(folder_path)
        for folder_path in list_of_games:
            EGSFileManager.tempRenameGame(folder_path)
        EGSFileManager.check_epic_created_game_folder()
        EGSFileManager.removeNewlyCreatedFolders()
        
    def check_epic_created_game_folder():
        print("ALERT!!  Awaiting for EGS to create the game folders. Please head over to EGS and install you're games. ")
        EGSCreatedGameFolders = False
        while not EGSCreatedGameFolders:
            if all(os.path.isdir(game) for game in list_of_games):
                print("Successfully found all the game folders created by EGS. Standby whilst I kill EGS")
                return
   
    def removeNewlyCreatedFolders():
        time.sleep(5)
        for game in list_of_games:
            temp_file_path = game + tempoary_file_ext
            print(temp_file_path)
            os.rmdir(temp_file_path)
        time.sleep(5)
        return

    def tempRenameGame(full_game_path):
        new_file_name = full_game_path + tempoary_file_ext
        os.rename(full_game_path, new_file_name)
        return

    def correctlyRenameGame(temp_game_path):
        orgional_file_name = temp_game_path.strip(tempoary_file_ext)
        print(temp_game_path, orgional_file_name)
        os.rename(temp_game_path, orgional_file_name)
  

    def detectExistingGames(folder_path):
        game_dir = os.listdir(folder_path)
        for game in game_dir:
            full_game_path = str(folder_path + '\\' + game )
            list_of_games.append(full_game_path)
        return

    def detectTempFolders(folder_path):
        game_dir = os.listdir(folder_path)
        for game in game_dir:
            temp_game_path = str(folder_path + '\\' + game )
            list_of_temp_folders.append(temp_game_path)
        return

if __name__ == "__main__":
    EGSFileManager()
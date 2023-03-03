import socket,threading,json,time
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

ROOM_SIZE = 700
PLAYER_SIZE = 140
ROUND_TIME = 30
FPS = 15
TOTAL_PLAYERS = 4

while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1

if TOTAL_PLAYERS > 4:
    TOTAL_PLAYERS = 4

class Connection:
    def __init__(self):
        self.encoder = "utf-8"
        self.header_length = 10

        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((HOST_IP,HOST_PORT))
        self.server_socket.listen()


class Player:
    def __init__(self,number):
        self.number = number
        self.size = PLAYER_SIZE
        self.score = 0
        # Assign starting conditions that vary with player number
        if self.number == 1:
            self.starting_x = 0
            self.starting_y = 0
            self.p_color = (255, 0, 0)
            self.s_color = (150, 0, 0)
        elif self.number == 2:
            self.starting_x = ROOM_SIZE - PLAYER_SIZE
            self.starting_y = 0
            self.p_color = (0, 255, 0)
            self.s_color = (0, 150, 0)
        elif self.number == 3:
            self.starting_x = 0
            self.starting_y = ROOM_SIZE - PLAYER_SIZE
            self.p_color = (0, 0, 255)
            self.s_color = (0, 0, 150)
        elif self.number == 4:
            self.starting_x = ROOM_SIZE - PLAYER_SIZE
            self.starting_y = ROOM_SIZE - PLAYER_SIZE
            self.p_color = (255, 255, 0)
            self.s_color = (150, 150, 0)
        else:
            print("Too many players trying to join...")

        # Set the rest of the player attributes
        self.x = self.starting_x
        self.y = self.starting_y
        self.dx = 0
        self.dy = 0
        self.coord = (self.x, self.y, self.size, self.size)

        self.is_waiting = True
        self.is_ready = False
        self.is_playing = False
        self.status_message = f"Waiting for {TOTAL_PLAYERS} total players"

    def set_player_info(self,player_info):
        self.coord = player_info["coord"]
        self.is_waiting = player_info["is_waiting"]
        self.is_ready = player_info['is_ready']
        self.is_playing = player_info['is_playing']

    def reset_player(self):
        self.score = 0

class Game:
    def __init__(self,connection):
        self.connection = connection
        self.player_count = 0
        self.player_objects = []
        self.player_sockets = []
        self.round_time = ROUND_TIME

    def connect_players(self):
        print("connection ")

my_connection = Connection()
my_game = Game(my_connection)

#Listen for incomming connections
print("Server is listening for incomming connections...\n")
my_game.connect_players()
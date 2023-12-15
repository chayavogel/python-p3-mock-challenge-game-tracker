class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title') or not isinstance(title, str) or len(title) == 0:
            print("try again")
        else:
            self._title = title

    def results(self):
        results_list = [result for result in Result.all if result.game == self]
        return results_list

    def players(self):
        games_set = {result.player for result in Result.all if result.game == self}
        games_list = list(games_set)
        return games_list

    def average_score(self, player):
        results_list = [result.score for result in Result.all if result.game == self and result.player == player]
        average = sum(results_list) / len(results_list)
        return average
     

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            print("Try again")
        elif not 2 <= len(username) <= 18:
            print("Try again")
        else:
            self._username = username

    def results(self):
        results_list = [result for result in Result.all if result.player == self]
        return results_list

    def games_played(self):
        games_set = {result.game for result in Result.all if result.player == self}
        games_list = list(games_set)
        return games_list

    def played_game(self, game):
        games_set = {result.game for result in Result.all if result.player == self}
        games_list = list(games_set)
        return game in games_list

    def num_times_played(self, game):
        games_list = [result.game for result in Result.all if result.player == self]
        count = games_list.count(game)
        return count

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property 
    def score(self):
        return self._score 
    
    @score.setter
    def score(self, score):
        if not isinstance(score, int) or not (1 <= score <= 5000) or hasattr(self, "_score"):
            print("Try again")
        else:
            self._score = score

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
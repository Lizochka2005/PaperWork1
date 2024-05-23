class House:
    def __init__(self):
        self.len = 0
        self.wide = 0
        self.high = 0
        self.wall_k = 0
        self.floor_k = 0
        self.roof_k = 0
        self.window_k = 0
        self.door_k = 0
        self.count_w = 0
        self.count_d = 0
        self.len_d = 0
        self.wide_d = 0
        self.len_w = 0
        self.wide_w = 0
        self.thick_w = 0
        self.thick_wall = 0
        self.thick_roof = 0
        self.thick_floor = 0
        self.thick_d = 0
        self.s = 0
        self.v = 0
        self.s_d = 0
        self.s_win = 0
        self.s_wall = 0
        self.q_win = 0
        self.q_wall = 0
        self.q_door = 0
        self.q_floor = 0
        self.q_roof = 0
        self.Q = 0
        self.P = 0
        self.W = 0
        self.V = 0

class House_multip:
    def Square(self, len, wide):
        return len * wide

    def Square_wall(self, len, wide, high, s_win, s_d):
        return high * (len + wide) * 2 - s_win - s_d

    def Volume(self, high, s):
        return s * high

    def Heat_loss(self, k, s, thick):
        return (s * 40 * k) / thick

    def Power(self, s, Q):
        return (Q * s * 1.25) / 100

class Room:
    def __init__(self):
        self.room_len = 0
        self.room_wide = 0
        self.room_s = 0
        self.k1 = 0
        self.k2 = 0
        self.k3 = 0
        self.k4 = 0
        self.k5 = 0
        self.k6 = 0
        self.k7 = 0
        self.C = 0
        self.N = 0
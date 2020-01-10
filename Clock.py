import multitimer


class Clock:

    def __init__(self, cycle_in_sec):
        self.cycle_count = 0
        self.state = 0
        self.cycle_in_sec = cycle_in_sec
        timer = multitimer.MultiTimer(self.cycle_in_sec, self.update)
        timer.start()

    def update(self):
        self.cycle_count += 1
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0
        print(self.state, self.cycle_count)

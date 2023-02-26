import time

# Simple progress bar
# - spec
# [ETA: 00.00s] [00%] [=====================>] [100%] | elapsed time: 00.00s

# ETA and elapsed time
# - ETA: estimated time of arrival
# - elapsed time: time since the beginning of the process
# max_ETA 999.99s
# max_elapsed_time 999.99s
# if ETA > 999.99s, ETA = 999.99s+@

# 시작시간을 저장해두고 업데이트 될 때마다 현재시간 - 시작시간을 통해 경과시간을 구한다.
# 경과시간을 통해 남은 시간을 계산한다.

color_green = "\033[32m"
color_reset = "\033[0m"

class ElapseManager:
    def __init__(self):
        self._start_time = time.time()
        self._elapsed_time = 0
        self._ETA = 0
    
    def update(self, index, index_max):
        self._elapsed_time = time.time() - self._start_time
        if index == 0:
            self._ETA = 0
        else:
            self._ETA = self._elapsed_time + (self._elapsed_time / index) * (index_max - index)

    def get_elapsed_time(self):
        if self._elapsed_time > 999.99: self._elapsed_time = "999.99 + @"
        return self._elapsed_time

    def get_ETA(self):
        if self._ETA > 999.99: self._ETA = "999.99 + @"
        return self._ETA

class progress_bar:
    def __init__(self, list):
        self._list = list
        self._index = 0
        self._index_max = len(list)
        self._bar_length = 20
        self._bar_max = 100
        self._bar_term = self._bar_max / self._bar_length
        self._elapse_manager = ElapseManager()

    def update(self):
        self._index += 1
        self._elapse_manager.update(self._index, self._index_max)
        return self._list[self._index - 1]
    
    def __str__(self):
        current_percent = (self._index / len(self._list) * self._bar_max)
        ETA = self._elapse_manager.get_ETA()
        elapsed_time = self._elapse_manager.get_elapsed_time()
        progress_bar_charged = '=' * (int(current_percent) // int(self._bar_term)) + '>'
        if self._index == self._index_max:
            return f"ETA: {ETA:02.02f}s [{current_percent:03.02f}%] {color_green}[{progress_bar_charged:20}]{color_reset} [{self._index}/{self._index_max}]  | elapsed time: {elapsed_time:02.02f}s"
        return f"ETA: {ETA:6.02f}s [{current_percent:6.02f}%] [{progress_bar_charged:20}] [{self._index}/{self._index_max}] | elapsed time: {elapsed_time:02.02f}s"

def ft_progress(list : list):
    pb = progress_bar(list)
    for i in list:
        yield pb.update()
        print(pb, end="\r", flush=True)
    print()

def main():
    print("Loading...")
    listy = range(1000)
    ret = 0
    for i in ft_progress(listy):
        ret += (i + 3) % 5
        time.sleep(0.01)
    print("...\nDone!")
    print(ret)

if __name__ == "__main__":
    main()
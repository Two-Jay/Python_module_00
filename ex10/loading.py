
# * import
# --------------------------------------------------------------------------
import time

# * color variables
# --------------------------------------------------------------------------
color_green = "\033[32m"
color_reset = "\033[0m"

# * Class Elapse_manager
# --------------------------------------------------------------------------
class Elapse_manager:
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

# * Class Progress_bar
# --------------------------------------------------------------------------
class Progress_bar:
    def __init__(self, list):
        self._list = list
        self._index = 0
        self._index_max = len(list)
        self._bar_length = 20
        self._bar_max = 100
        self._bar_term = self._bar_max / self._bar_length
        self._elapse_manager = Elapse_manager()

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
    pb = Progress_bar(list)
    for i in list:
        yield pb.update()
        print(pb, end="\r", flush=True)
    print()

def do_loading(listy : list) -> None:
    print("Loading...")
    ret = 0
    for i in ft_progress(listy):
        ret += (i + 3) % 5
        time.sleep(0.01)
    print("...\nDone!")
    print(ret)

def main():
    do_loading(range(100))
    do_loading(range(100, 200))
    do_loading(range(1))
    do_loading(range(4))
    do_loading(range(0,-100,-1))

if __name__ == "__main__":
    main()
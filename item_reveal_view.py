import random

from terminal import erase_entire_line, write, set_horizontal_absolute
from time import sleep


class ItemRevealView:
    def __init__(self, default_initial_duration=3, default_decay_factor=0.7, default_decay_range=0.15):
        self.default_initial_duration = default_initial_duration
        self.default_decay_factor = default_decay_factor
        self.default_decay_range = default_decay_range

    def reveal_value(self, value, initial_duration=None):
        time_slices = self.calculate_time_slices(number_of_slices=len(value), initial_duration=initial_duration)
        letter_order = self.randomize_letters(value)
        write()
        write()
        slice_index = 0
        for tuple_to_reveal in letter_order:
            letter = tuple_to_reveal[0]
            column = tuple_to_reveal[1]
            set_horizontal_absolute(col=column)
            write(letter)
            sleep(time_slices[slice_index])
            slice_index += 1

    def calculate_time_slices(self, number_of_slices, initial_duration=None):
        if initial_duration is None:
            initial_duration_to_use = self.default_initial_duration
        else:
            initial_duration_to_use = initial_duration
        durations = []
        current_duration = initial_duration_to_use
        for slice_index in range(number_of_slices):
            durations.append(current_duration)
            decay_variation = random.uniform(self.default_decay_range*-1, self.default_decay_range)
            current_duration = current_duration * (self.default_decay_factor + decay_variation)
        return durations

    def randomize_letters(self, source):
        tuples = []
        for index, letter in enumerate(source):
            tuples.append((letter, index+1))
        random.shuffle(tuples)
        return tuples

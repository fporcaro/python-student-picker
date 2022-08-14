import random

from src.services.terminal import terminal
from src.services.terminal.terminal import write, set_horizontal_absolute
from time import sleep


class ItemRevealView:
    def __init__(self, default_initial_duration=1.0, default_decay_factor=0.7, default_decay_range=0.2,
                 default_peek_delay_base=0.15, default_peek_delay_variation=0.05):
        self.default_initial_duration = default_initial_duration
        self.default_decay_factor = default_decay_factor
        self.default_decay_range = default_decay_range
        self.default_peek_delay_base = default_peek_delay_base
        self.default_peek_variation = default_peek_delay_variation

    def reveal_value_dramatic(self, value, peek_values, initial_duration=None):
        terminal.erase_to_end_of_line()
        for peek_value in peek_values:
            self.peek_value(peek_value)
        self.reveal_value(value=value, initial_duration=initial_duration)

    def reveal_value(self, value, initial_duration=None):
        time_slices = self.calculate_decaying_time_slices(number_of_slices=len(value), initial_duration=initial_duration)
        letter_order = self.randomize_letters(value)
        slice_index = 0
        terminal.erase_to_end_of_line()
        for tuple_to_reveal in letter_order:
            letter = tuple_to_reveal[0]
            column = tuple_to_reveal[1]
            set_horizontal_absolute(col=column)
            write(letter)
            sleep(time_slices[slice_index])
            slice_index += 1

    def peek_value(self, value):
        time_slices = self.calculate_range_time_slices(number_of_slices=len(value))
        letter_order = self.randomize_letters(value)
        some_letter_order = letter_order[0:int(len(letter_order)*0.65)]
        slice_index = 0
        for tuple_to_reveal in some_letter_order:
            letter = tuple_to_reveal[0]
            column = tuple_to_reveal[1]
            set_horizontal_absolute(col=column)
            write(letter)
            sleep(time_slices[slice_index])
            slice_index += 1
        slice_index = 0
        for tuple_to_reveal in some_letter_order:
            column = tuple_to_reveal[1]
            set_horizontal_absolute(col=column)
            write(' ')
            sleep(time_slices[slice_index]/2)
            slice_index += 1

    def calculate_decaying_time_slices(self, number_of_slices, initial_duration=None):
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

    def calculate_range_time_slices(self, number_of_slices, target_duration=None, target_variation=None):
        if target_duration is None:
            target_duration_to_use = self.default_peek_delay_base
        else:
            target_duration_to_use = target_duration
        if target_variation is None:
            target_variation_to_use = self.default_peek_variation
        else:
            target_variation_to_use = target_variation
        durations = []
        for slice_index in range(number_of_slices):
            duration_variation = random.uniform(target_variation_to_use*-1, target_variation_to_use)
            current_duration = target_duration_to_use + duration_variation
            durations.append(current_duration)
        return durations

    def randomize_letters(self, source):
        tuples = []
        for index, letter in enumerate(source):
            tuples.append((letter, index+1))
        random.shuffle(tuples)
        return tuples

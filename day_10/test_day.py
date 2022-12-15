from main import part_one, part_two
import pytest

day_one_lines = [
    ('bvwbjplbgvbhsrlpgdmjqwftvncz' , 5),
    ('nppdvjthqldpwncqszvftbrmjlhg' , 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' , 10),  
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' , 11)
]

day_two_lines = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' , 26)
]
    

@pytest.mark.parametrize("line, expected_output", day_one_lines)
def test_part_one(line, expected_output):
    assert part_one(line) == expected_output


@pytest.mark.parametrize("line, expected_output", day_two_lines)
def test_part_two(line, expected_output):
    assert part_two(line) == expected_output

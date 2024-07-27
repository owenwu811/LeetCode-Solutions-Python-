#my solution from grokking course in python3 at the end of the greedy pattern: (challenge question without solution):


def jump_game_two(nums):
    farthest_jump, current_jump, jumps = 0, 0, 0
    for i in range(len(nums)):
        farthest_jump = max(farthest_jump, i + nums[i])
        if current_jump == len(nums) - 1:
            return jumps
        if current_jump == i:
            jumps += 1
            current_jump = farthest_jump
        #else:
        #    jumps += 1
        #   current_jump = farthest_jump
    return jumps


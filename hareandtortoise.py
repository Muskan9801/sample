 if len(nums) <= 1:
        return -1

    if len(nums) > 1:
        # The "tortoise and hare" step.
        # We start at the start of the array and try to find an intersection point in the cycle.
        tortoise = hare = nums[0]

        # Keep advancing 'tortoise' by one step and 'hare' by two steps until they meet inside the loop.
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            # Detected Cycle => (hare laps/meets tortoise)
            if tortoise == hare:
                break

        # Send hare back to the start of array to evaluate the point of entrance to the cycle
        # Current tortoise position in the circle is the point of overlap when hare met the tortoise indicating presence of cycle.
        # Advance both of them at the same speed until they meet again.
        hare = nums[0]
        while hare != tortoise:
         hare = nums[hare]
            tortoise = nums[tortoise]
        # The duplicate number must be the entry point of the circle when visiting the array again
        # Tortoise and hare meet again; the intersection index has the duplicate element.
        return hare

    return -1

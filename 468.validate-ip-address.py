#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
import string


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            segments = queryIP.split(".")
            if len(segments) != 4:
                return "Neither"
            for segment in segments:
                if not segment.isdigit() or not 0 <= int(segment) <= 255 or (segment[0] == "0" and len(segment) > 1):
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            segments = queryIP.split(":")
            if len(segments) != 8:
                return "Neither"
            for segment in segments:
                if not segment or len(segment) > 4 or not all(c in string.hexdigits for c in segment):
                    return "Neither"
            return "IPv6"
        return "Neither"
# @lc code=end


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_hex(s):
            try:
                int(s, 16)
                return True
            except ValueError:
                return False
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) == 4:
                for part in parts:
                    if not part.isdigit() or not 0 <= int(part) <= 255 or (len(part) > 1 and part[0] == '0'):
                        return "Neither"
                return "IPv4"
        elif ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) == 8:
                for part in parts:
                    if len(part) == 0 or len(part) > 4 or not all(c in '0123456789ABCDEFabcdef' for c in part):
                        return "Neither"
                return "IPv6"
        
        return "Neither"

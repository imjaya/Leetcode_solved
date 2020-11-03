class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        output = []
        digits = []
        letters = {}
        
        for log in logs:
            if log.split()[1].isnumeric():
                digits.append(log)
            else:
                key = ' '.join(log.split()[1:])
                if key not in letters:
                    letters[key] = []
                letters[key].append(log.split()[0])

        for log in sorted(letters):
            for id in sorted(letters[log]):
                output.append(id + ' ' + log)
        
        for log in digits:
            output.append(log)

        return output
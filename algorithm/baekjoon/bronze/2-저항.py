

class Solution:
    answer = ''

    def start(self):
        for n in range(3):
            color = input()
            if color == 'black':
                self.settingValue(n, '0', 1)
            elif color == 'brown':
                self.settingValue(n, '1', 10)
            elif color == 'red':
                self.settingValue(n, '2', 100)
            elif color == 'orange':
                self.settingValue(n, '3', 1000)
            elif color == 'yellow':
                self.settingValue(n, '4', 10000)
            elif color == 'green':
                self.settingValue(n, '5', 100000)
            elif color == 'blue':
                self.settingValue(n, '6', 1000000)
            elif color == 'violet':
                self.settingValue(n, '7', 10000000)
            elif color == 'grey':
                self.settingValue(n, '8', 100000000)
            elif color == 'white':
                self.settingValue(n, '9', 1000000000)
        print(self.answer)

    def settingValue(self, num, value, mixValue):
        if num == 0:
            self.answer = value
        elif num == 1:
            self.answer += value
        else:
            self.answer = int(self.answer) * mixValue


fun = Solution()
fun.start()


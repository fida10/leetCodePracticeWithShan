class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {};
        asciiCounter = 97;

        for indivChar in key:
            if (indivChar not in cipher and indivChar != ' '):
                cipher[indivChar] = chr(asciiCounter)
                asciiCounter += 1;

        ans = "";

        for indivChar in message:
            if (indivChar == ' '):
                ans += ' ';
            else:
                ans += cipher[indivChar];

        return ans;
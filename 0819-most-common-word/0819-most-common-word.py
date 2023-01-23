class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # paragraph = paragraph.lower()
        # paragraph = re.sub(r'[^\w]', ' ',paragraph)
        # paragraph = paragraph.split()
        # words = [word for word in paragraph
        #             if word not in banned]
        
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]
        return Counter(words).most_common(1)[0][0]
class Solution(object):
    def capitalizeTitle(self, title):
        words=title.split()
        sen=""
        for word in words:
            if len(word)==1 or len(word)==2:
                sen+=word.lower()+" "
            else:
                sen+=word[0].upper() + word[1:].lower()+ ' '
        return sen.strip()        

        
import re
class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
    def replace(self, word):
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
          return self.replace(repl_word)
        else:
          return repl_word


replacer = RepeatReplacer()
a=replacer.replace('juuuuuusssste')
print(a)

text='https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python I missed the New Moon trailer...;;;;;;;;;;;;'
#text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
k='sdv45sdv'
result = ''.join([i for i in k if not i.isdigit()])
print(result)
text = re.sub(r"http\S+", "", text)

print(text)
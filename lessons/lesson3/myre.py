import re



# re.compile()
# re.match()
# re.search()
# re.match().group(0) # return to Match object or None, if the first one do not match, fail to match and return None
# re.match().groups() # return to Match object or None, when there is a match, then return the matched one
#re.split()
"""
\d: for a numner
\w: for a character
\s: for space
.: any one character
*: any character include no character
+: at lesat one character
{8}: 8 character
{3:9}: 3 to 9 character
[0-9a-zA-z\_]: match one number/a character/_
[0-9a-zA-z\_]: match at least one number/a character/_
^: mactch the first one
$: match the last one
"""

str_tz = "UTC+8:00"

t_delta = re.match(r'(^UTC)((\+|\-)(\d))(\:\d{2})',str_tz)
print(t_delta.group(0))
print(t_delta.group(2))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345').group(0))
print(re.match(r'[\w\,]+', 'a,b, c  d').group(0))

print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[t\s]+', 'hththtttthhhh'))
print(re.match(r'^(\w+?)(0*)$', '102334gg0g5500').groups())

"""995903723@qq.com"""
re_rule = re.compile(r'([\w\.]+)@([\w\.]+)com$')

print(re_rule.match('995903723@qq.com').group(0))
print(re_rule.match('15201920322@163.com').group(0))
print(re_rule.search('     15201920322@163.com').group(0))

"""the different between re.match and re.search"""
print(re.search('www','sam.www.com').group(0))
print(re.match('www','sam.www.com').group(0))

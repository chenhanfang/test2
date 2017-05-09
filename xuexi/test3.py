import re

text ='''Paragraph one
on two lines.

Paragraph two.

Paragraph three.'''
#
# for num,para in enumerate(re.findall(r'(.+?)\n{2,}',
#                                      text,
#                                      flags=re.DOTALL)):
#     print(num,repr(para))

print('with findall')
for num,para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                     text,
                                     flags=re.DOTALL)):
    print(num,repr(para))


print('with split:')#####split分割，类似于str.partition()
for num,para in enumerate(re.split(r'\n{2,}',text)):
    print(num,repr(para))

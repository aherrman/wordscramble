import random
import re

_SCRAMBLE_CHARS = '[a-zA-Z]'

def scramble(s):
  arr = [c for c in s]
  random.shuffle(arr)
  return ''.join(arr)


def word_scramble(word, keep_left=1, keep_right=1):
  if keep_left + keep_right >= len(word):
    return word

  left_pos = keep_left
  right_pos = len(word) - keep_right

  left = word[0:left_pos]
  mid = scramble(word[left_pos:right_pos])
  right = word[right_pos:]

  return left + mid + right


def text_scramble(text, keep_left=1, keep_right=1):
  current = ''
  new_text = ''
  for c in text:
    if re.match(_SCRAMBLE_CHARS, c):
      current += c
    else:
      if current:
        new_text += word_scramble(current, keep_left, keep_right)
      current = ''
      new_text += c

  if current:
    new_text += word_scramble(current, keep_left, keep_right)

  return new_text

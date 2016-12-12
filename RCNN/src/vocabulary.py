# -*- coding: utf-8 -*-
words = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789一二三四五六七八九十壹贰叁肆伍陆柒捌玖拾'

def GetChar():
    return [v for i, v in enumerate(words)]

def GetCharacterVocabulary():
  def GetChars(start_char, end_char):
      return [chr(i) for i in range(ord(start_char), ord(end_char) + 1)]
  #if capital_included:
   #  all_chars = ['unk'] + GetChars('0', '9') + GetChars('a', 'z')   + GetChars('A', 'Z')
  #else:
   #  all_chars = ['unk'] + GetChars('0', '9') + GetChars('a', 'z')
  all_chars=['unk'] + GetChar()
  #RETURNS VOCABULARY, CHARS
  #return {char: i for i, char in enumerate(all_chars)}, all_chars
  return {char:i for i,char in enumerate(all_chars)},all_chars

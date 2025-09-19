def get_num_words(string):
  chars = string.split()
  return len(chars)

def get_times_chars(string):
  chars_list = string.split()
  chars = {}

  for word in chars_list:
    for char in word.lower():
      if char in chars:
        chars[char] += 1
      
      if char not in chars:
        chars[char] = 1 
  
  return chars
  
def sort_on(items):
    return items["num"]

def sorted_chars(chars):
  new_array = chars.items()
  new_array_list = []

  for item in new_array:
    if (item[0].isalpha()):
      map_prop = item[0]
      map_key = item[1]
      new_map = {"char": map_prop, "num": map_key}
      new_array_list.append(new_map)
      
      new_array_list.sort(reverse=True, key=sort_on)

  return new_array_list
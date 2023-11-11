#신규 아이디 추천
import re

def solution(new_id):
  
    # Step 1
    new_id = new_id.lower()
    
    # Step 2
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    
    # Step 3
    new_id = re.sub('\.+', '.', new_id)
    
    # Step 4
    new_id = new_id.strip('.')
    
    # Step 5
    if new_id == '':
        new_id = 'a'
    
    # Step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    
    # Step 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
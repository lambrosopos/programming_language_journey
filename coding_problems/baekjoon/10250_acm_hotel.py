total_len = int(input())

def pad_left(target_str: str):
    if len(target_str) == 2:
        return target_str
    
    return "0" + target_str
    
def get_info(levels: int, rooms: int, guest_num: int) -> int:
    level_no = guest_num % levels 
    if level_no == 0:
        level_no = levels
        
    room_no = int(guest_num / levels)
    
    if room_no != guest_num / levels:
        room_no += 1
    
    padded_room_no = pad_left(str(room_no))
    return f"{level_no}{padded_room_no}"

for i in range(total_len):
    new_input = [int(_) for _ in input().split()]
    ans = get_info(levels=new_input[0], rooms=new_input[1], guest_num=new_input[2])
    print(ans)

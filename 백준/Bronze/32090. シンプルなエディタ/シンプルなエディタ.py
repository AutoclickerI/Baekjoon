def process_input():

    index = 0
    results = []
    
    while True:
        # データセットのサイズを取得
        N = int(input())
        if N == 0:
            break
        
        index += 1
        # 現在の文字列をリストとして保持
        current_string = []
        # カーソルの位置
        cursor_position = 0
        
        for _ in range(N):
            command = input()
            index += 1
            
            if command.startswith("INSERT"):
                char = command[7]  # INSERT c の形式
                # カーソルの左に挿入
                current_string.insert(cursor_position, char)
                cursor_position += 1  # カーソルを右に移動
                
            elif command == "LEFT _":
                if cursor_position > 0:
                    cursor_position -= 1  # カーソルを左に移動
                    
            elif command == "RIGHT _":
                if cursor_position < len(current_string):
                    cursor_position += 1  # カーソルを右に移動
        
        # 結果の文字列を構築
        results.append(''.join(current_string))
    
    # 出力結果を表示
    for result in results:
        print(result)

# 入力の読み込みと処理
process_input()